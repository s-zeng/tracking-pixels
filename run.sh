#!/usr/bin/env bash

gunicorn -w 1 -b :80 "tracking:app"
