import random
import string

url_map = {}

def shorten_url(original_url, host='localhost'):
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_map[short] = original_url
    return f"http://{host}/{short}"
