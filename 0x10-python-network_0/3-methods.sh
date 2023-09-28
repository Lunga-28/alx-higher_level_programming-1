#!/bin/bash
# displays all HTTP methods that the server accepts
curl -sI "$1" | grep "Allow" | cut -d' ' -f 2-
