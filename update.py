
import urllib.request
from pathlib import Path

SOURCE = (
    "https://raw.githubusercontent.com/"
    "Au1rxx/free-vpn-subscriptions/main/"
    "output/v2ray-base64.txt"
)

request = urllib.request.Request(
    SOURCE,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(request, timeout=30) as response:
    data = response.read()

if not data.strip():
    raise RuntimeError("Source is empty")

Path("subscription.txt").write_bytes(data)
print("Subscription updated")
