#!/bin/zsh

gunicorn --bind 0.0.0.0:5000 backend.wsgi:app
