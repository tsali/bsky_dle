#!/usr/bin/env python3

import os
import sys
import subprocess
import requests
from datetime import datetime, timedelta, timezone
from tqdm import tqdm
from dateutil import parser as dtparser

# ---------------------------
# CONFIGURATION
# ---------------------------
TOKEN = "BEARER TOKEN" # Replace with your actual Bluesky bearer token
HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}
API_BASE = "https://bsky.social/xrpc"
CDN_IMG = "https://cdn.bsky.app/img/feed_fullsize/plain"
VIDEO_BASE = "https://video.bsky.app/watch"

# ---------------------------
# FUNCTIONS
# ---------------------------

def resolve_did(handle):
    resp = requests.get(f"{API_BASE}/com.atproto.identity.resolveHandle", params={"handle": handle})
    resp.raise_for_status()
    return resp.json().get("did")

def fetch_page(did, cursor=None):
    params = {
        "repo": did,
        "collection": "app.bsky.feed.post",
        "limit": 100
    }
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(f"{API_BASE}/com.atproto.repo.listRecords", headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()

def extract_urls(records, did, since_dt=None):
    urls = []
    for rec in records:
        val = rec.get("value", {})
        created = val.get("createdAt")
        if since_dt:
            post_dt = dtparser.parse(created)
            if post_dt < since_dt:
                continue  # skip old posts

        embed = val.get("embed")
        if not embed:
            continue

        etype = embed.get("$type")
        if etype == "app.bsky.embed.images":
            for img in embed.get("images", []):
                cid = img["image"]["ref"]["$link"]
                url = f"{CDN_IMG}/{did}/{cid}@jpeg"
                urls.append(("image", url))

        elif etype == "app.bsky.embed.recordWithMedia":
            media = embed.get("media", {})
            if media.get("$type") == "app.bsky.embed.video":
                cid = media["video"]["ref"]["$link"]
                video_url = f"{VIDEO_BASE}/{did}/{cid}/720p/video.m3u8"
                urls.append(("video", video_url))
    return urls

def download_image(url, out_dir):
    filename = os.path.join(out_dir, os.path.basename(url).replace("@", "."))
    if os.path.exists(filename):
        return
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, "wb") as f:
            for chunk in r.iter_content(1024 * 8):
                f.write(chunk)
        print(f"✅ Image: {filename}")
    else:
        print(f"❌ Failed to download image: {url} (HTTP {r.status_code})")

def download_video(url, out_dir):
    filename = os.path.join(out_dir, os.path.basename(url).split("?")[0].replace("/", "_") + ".mp4")
    if os.path.exists(filename):
        return
    try:
        subprocess.run(["yt-dlp", "-o", filename, url], check=True)
        print(f"✅ Video: {filename}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to download video: {url}")

# ---------------------------
# MAIN
# ---------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bsky_media_downloader.py <handle> [days]")
        sys.exit(1)

    handle = sys.argv[1]
    days = int(sys.argv[2]) if len(sys.argv) > 2 else None
    since_dt = datetime.now(timezone.utc) - timedelta(days=days) if days else None

    print(f"📡 Resolving DID for {handle}...")
    did = resolve_did(handle)
    print(f"✅ DID: {did}")

    os.makedirs(handle, exist_ok=True)
    cursor = None

    while True:
        page = fetch_page(did, cursor)
        records = page.get("records", [])
        if not records:
            break

        media_urls = extract_urls(records, did, since_dt)
        for mtype, url in tqdm(media_urls, desc="Downloading"):
            if mtype == "image":
                download_image(url, handle)
            elif mtype == "video":
                download_video(url, handle)

        cursor = page.get("cursor")
        if not cursor:
            break

    print("🏁 Done.")

if __name__ == "__main__":
    main()
