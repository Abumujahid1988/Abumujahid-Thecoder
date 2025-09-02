# Mood Journal – AI Emotion Tracker

A simple Flask + MySQL app that analyzes journal entries via Hugging Face Inference API and visualizes mood trends with Chart.js.

## Setup
1. Create DB: `mysql -u root -p < schema.sql`
2. Copy `.env.example` to `.env` and set credentials + `HUGGINGFACE_API_TOKEN`.
3. Create venv & install deps: `pip install -r requirements.txt`
4. Run: `python app.py` and open http://127.0.0.1:5000

## Usage
- Write an entry, press **Analyze & Save**.
- The trend chart updates with per‑day average emotion scores (0..1).
- Recent entries list shows the top emotion and the top 3 scores.

## Troubleshooting
- If you get 500s on analyze: check your HF token and internet access.
- On MySQL auth errors: verify `DB_USER/DB_PASSWORD` in `.env` and that the user has rights on `mood_journal`.
- On Windows, install MySQL Connector C++ via installer if `mysql-connector-python` fails to build.

## License
MIT for coursework and demos.
