from flask import Flask, render_template, request, redirect
from shortener import shorten_url, url_map

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = shorten_url(original_url, host=request.host)
        return render_template('index.html', short_url=short_url, original_url=original_url)
    return render_template('index.html', short_url=None)

@app.route('/<short>')
def redirect_to_original(short):
    if short in url_map:
        return redirect(url_map[short])
    return 'Invalid short URL', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
