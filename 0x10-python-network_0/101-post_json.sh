#!/bin/bash
# sends a JSON POST request to a URL
curl -sH "Content-Type: application/json" -X POST -d @"$2" "$1"
