#!/usr/bin/env bash

gunicorn -w 1 -b :5227 "tracking:app"
