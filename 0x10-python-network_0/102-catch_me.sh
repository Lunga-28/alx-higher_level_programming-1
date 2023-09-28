#!/bin/bash
# send request to url and get response
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: School" -d "user_id=98"
