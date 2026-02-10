import os


def get_yt_cookies() -> str:
    cookies = f"SAPISID={os.getenv('SAPISID')};"
    cookies += f"__Secure-1PAPISID={os.getenv('SAPISID')};"
    cookies += f"__Secure-1PSIDTS={os.getenv('PSIDTS')};"
    cookies += f"__Secure-1PSID={os.getenv('PSID')};"
    return cookies


def extract_yt_pl_code(raw_url: str) -> str:
    if "browse" in raw_url:
        return raw_url.split("/")[-1][2:]
    elif "playlist" in raw_url:
        return raw_url.split("=")[1]
    return ""