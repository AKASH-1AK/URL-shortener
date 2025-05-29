import random
import string

url_map = {}  # Dictionary to store short -> original mapping

def shorten_url(original_url):
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_map[short] = original_url
    return f"http://your-domain/{short}"  # Replace with actual domain after deployment
