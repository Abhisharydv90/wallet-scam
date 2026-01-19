#!/bin/bash
pip install -r requirements.txt
python backend/database.py
nohup gunicorn -w 4 -b 0.0.0.0:5000 backend.main:app > app.log 2>&1 &
nohup python scripts/collect_profit.py > profit.log 2>&1 &
