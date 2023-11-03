from flask import Flask, request, redirect, render_template
import string
import random

app = Flask(__name__)
url_storage = {}  # This will be used to store the links, like a database

def gen_url_short():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(10))  # Random short URL generator

@app.route('/shorten', methods=['POST'])
def short_url_fun():
    main_url = request.form['main_url']
    for short_url, stored_url in url_storage.items():
        if stored_url == main_url:
            return render_template('index.html', shortened_url=short_url, original_url=stored_url)

    short_url = gen_url_short()
    url_storage[short_url] = main_url
    return render_template('index.html', shortened_url=short_url, original_url=main_url)


@app.route('/', methods=['GET'])
def index():
    # You should replace these sample URLs with your actual data
    shortened_url = "https://yourshortenedurl.com/abc123"
    redirected_url = "https://originalurl.com/longurl"
    return render_template('index.html', shortened_url=shortened_url, redirected_url=redirected_url)

@app.route('/<short_url>')
def redirect_fun(short_url):
    if short_url in url_storage:
        main_url = url_storage[short_url]
        return redirect(main_url)
    else:
        return "URL not found"

@app.route('/redirect', methods=['GET', 'POST'])
def redirect_form():
    if request.method == 'POST':
        short_url = request.form['short_url']
        original_url = url_storage.get(short_url)
        if original_url is None:
            original_url = "URL not found"
        return render_template('redirect.html', shortened_url=short_url, original_url=original_url)
    return render_template('redirect.html', shortened_url=None, original_url=None)


if __name__ == '__main__':
    app.run(debug=True)
