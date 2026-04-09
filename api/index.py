import os
import random
import string

from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-change-me")

# In-memory storage resets on each deployment instance restart.
url_mapping = {}


def generate_short_id(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None

    if request.method == "POST":
        original_url = request.form.get("original_url", "").strip()

        if not (original_url.startswith("http://") or original_url.startswith("https://")):
            flash("Please enter a valid URL starting with http:// or https://", "error")
            return render_template("index.html", short_url=None)

        short_id = generate_short_id()
        while short_id in url_mapping:
            short_id = generate_short_id()

        url_mapping[short_id] = original_url
        short_url = f"{request.host_url}{short_id}"

    return render_template("index.html", short_url=short_url)


@app.route("/<short_id>")
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)

    if original_url:
        return redirect(original_url)

    return "Invalid short URL!", 404


if __name__ == "__main__":
    app.run(debug=True)
