#!/usr/bin/env bash

# Este script será executado pelo Vercel
echo "BUILD START"
pip install -r requirements.txt
py manage.py collectstatic --no-input --clear # Ação crucial
echo "BUILD END"