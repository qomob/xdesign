#!/usr/bin/env python3
"""Sync local XDesign files to GitHub repo qomob/xdesign using gh api."""
import os
import sys
import json
import base64
import subprocess
import time
import urllib.request
import urllib.error

LOCAL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = "qomob"
REPO = "xdesign"
BRANCH = "main"
API_BASE = f"https://api.github.com/repos/{OWNER}/{REPO}"

SKIP_DIRS = {'.git', '.trae', '.ruff_cache', '.sync', '__pycache__', '.DS_Store'}
SKIP_FILES = {'.gitignore', '.DS_Store'}

def gh_api_get(path):
    url = f"{API_BASE}/contents/{path}?ref={BRANCH}" if path else f"{API_BASE}/contents?ref={BRANCH}"
    req = urllib.request.Request(url)
    token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise

def gh_api_put(path, content_b64, message, sha=None):
    url = f"{API_BASE}/contents/{path}"
    body = {
        "message": message,
        "content": content_b64,
        "branch": BRANCH,
    }
    if sha:
        body["sha"] = sha
    token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    req = urllib.request.Request(url, method="PUT",
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        })
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())

def collect_files():
    """Collect all files to upload, returning list of (local_rel_path, repo_path)."""
    files = []
    for dirpath, dirnames, filenames in os.walk(LOCAL_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn in SKIP_FILES:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, LOCAL_ROOT)
            files.append(rel)
    return sorted(files)

def file_sha(repo_path):
    """Get current SHA of a file in the repo, or None if it doesn't exist."""
    data = gh_api_get(repo_path)
    if data and isinstance(data, dict) and "sha" in data:
        return data["sha"]
    return None

def upload_file(rel_path, commit_msg=None):
    full = os.path.join(LOCAL_ROOT, rel_path)
    repo_path = rel_path.replace(os.sep, "/")
    with open(full, "rb") as f:
        raw = f.read()
    content_b64 = base64.b64encode(raw).decode()
    sha = file_sha(repo_path)
    msg = commit_msg or f"sync: update {repo_path}" if sha else f"sync: add {repo_path}"
    result = gh_api_put(repo_path, content_b64, msg, sha=sha)
    return result["commit"]["sha"], "updated" if sha else "created"

def main():
    files = collect_files()
    print(f"Found {len(files)} files to sync.")

    updated = 0
    created = 0
    errors = []
    commit_shas = []

    for i, rel in enumerate(files):
        repo_path = rel.replace(os.sep, "/")
        try:
            commit_sha, action = upload_file(rel)
            commit_shas.append(commit_sha)
            if action == "updated":
                updated += 1
            else:
                created += 1
            print(f"  [{i+1}/{len(files)}] {action}: {repo_path} ({commit_sha[:7]})")
        except Exception as e:
            errors.append((rel, str(e)))
            print(f"  [{i+1}/{len(files)}] ERROR: {rel}: {e}")

    print(f"\nDone. Created: {created}, Updated: {updated}, Errors: {len(errors)}")
    if errors:
        print("Errors:")
        for p, e in errors:
            print(f"  {p}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
