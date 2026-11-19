# COCO AI Global — Python deployment starter

A responsive futuristic blue/purple AI + crypto website prototype built with Flask.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Deploy on Render
1. Create a GitHub repository and upload these project files.
2. In Render, choose **New > Web Service** and connect the repository.
3. Render can detect `render.yaml`; otherwise use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Deploy. Render will provide a public URL.

## Important
This is a front-end prototype. Market figures and AI replies are illustrative.
There is no real user authentication, wallet connection, deposit, withdrawal,
staking, referral payout, or token reward functionality.

Before enabling any financial feature, define the exact 2X cap (whether it
includes principal or means profit on top), obtain legal/compliance advice,
audit smart contracts, and implement secure server-side accounting and
transaction controls. Never store seed phrases or private keys.
