#!/bin/bash

gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 setup:server