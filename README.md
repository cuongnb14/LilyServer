# Lily Server

server for chatbot Lyli

LICENSE: MIT

## Setup

Install lib: 
``` 
pip3 install -r requirements/local.txt
pip3 install -e git+https://github.com/tranhuucuong91/Py3kAiml.git#egg=pip
```

Run server: `python3 manage.py runserver`

Access: `localhost:8000/webapp`

## Process message

`message -> AIML -> ACTION::[param1]::[param2]... -> action handle -> message response`


## ACTION Type

- Fine in wiki: 
