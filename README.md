# Python Link Encryption Project

This project is a Flask-based URL encrypter.

## Project Structure

```text
api/
	index.py
	templates/
		index.html
	static/
		style.css
requirements.txt
vercel.json
```

## Run Locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python api/index.py
```

4. Open http://127.0.0.1:5000

## Deploy To Vercel

1. Push this repository to GitHub.
2. In Vercel, create a new project and import this repository.
3. Vercel will detect the Python setup from vercel.json.
4. Add environment variable:

```text
FLASK_SECRET_KEY=your-long-random-secret
```

5. Deploy.

## Important Note

URL mappings are currently stored in memory, so data is not persistent across serverless instance restarts.
For production persistence, replace in-memory storage with a database such as Redis, PostgreSQL, or DynamoDB.
