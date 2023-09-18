import requests, json

version = '1.0'

def load():
    return json.loads(requests.get('https://jovedb-10.noahwilhoite.repl.co/db').text)


def save(data):
    requests.post('https://jovedb-10.noahwilhoite.repl.co/db', json.dumps(db))
