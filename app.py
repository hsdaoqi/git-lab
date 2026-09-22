DEFAULT_LIMIT = 5


def normalize_query(text):
    return text.strip()


def build_request(text):
    return {"query": normalize_query(text), "limit": DEFAULT_LIMIT}


if __name__ == "__main__":
    print(build_request("  Git Lab  "))