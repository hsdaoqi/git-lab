from app import build_request

assert build_request("  Git Lab  ") == {"query": "Git Lab", "limit": 5}
print("PASS")