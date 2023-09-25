import string
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
urls = {}


def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form.get('url')
        if long_url:
            short_code = generate_short_code()
            short_url = short_code
            urls[short_code] = long_url
            return render_template('index.html', short_url=short_url)
        else:
            return render_template('index.html', error_message="Invalid URL. Please provide a valid URL to shorten.")
    return render_template('index.html')


@app.route('/<short_code>')
def redirect_to_url(short_code):
    long_url = urls.get(short_code)
    if long_url:
        return redirect(long_url)
    return "Short URL not found."


if __name__ == '__main__':
    app.run(debug=True)
