import requests
import json


def load_json_file():
    with open("wallet.json") as f:
        return json.loads(f.read())


def send_http_post(json_obj):
    print('We are going to send {}'.format(json_obj))
    r = requests.post('https://mythologic.fr/minotor/wallets/add', json=json_obj)
    print(r.status_code, r.text)


def main():
    json_obj = load_json_file()
    send_http_post(json_obj)


if __name__ == '__main__':
    main()
