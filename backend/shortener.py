from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

url_map = {}  # Dictionary to store short -> original mapping

def shorten_url(original_url):
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_map[short] = original_url
    return f"http://localhost:5000/{short}"

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')
    if not original_url:
        return "Missing URL", 400
    short_url = shorten_url(original_url)
    return short_url, 200

@app.route('/<short>')
def redirect_short_url(short):
    original_url = url_map.get(short)
    if original_url:
        return redirect(original_url)
    return "URL not found", 404
