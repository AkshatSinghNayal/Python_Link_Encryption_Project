from flask import Flask, request, redirect, render_template, url_for, flash
import string
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

# Just using a dictionary to store short links for now
url_mapping = {}


def generate_short_id(num_chars=6):
    # Makes a random string of letters and numbers
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=num_chars))


@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form.get('original_url', '')
        # Check if the URL looks okay
        if not (original_url.startswith('http://') or original_url.startswith('https://')):
            flash("Please enter a valid URL starting with http:// or https://", "error")
            return render_template('index.html', short_url=None)
        # Make a short id that isn't already used
        short_id = generate_short_id()
        while short_id in url_mapping:
            short_id = generate_short_id()
        url_mapping[short_id] = original_url
        # Make the full short URL to show to the user
        short_url = request.host_url + short_id
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', short_url=short_url)


@app.route('/<short_id>')
def redirect_to_url(short_id):
    # Try to find the original URL
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    # If not found, show error
    return "Invalid short URL!", 404


if __name__ == '__main__':
    # Run the app in debug mode so errors show up
    app.run(debug=True)
# ngrok http 5000  # Use ngrok to expose the app to the internet