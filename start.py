#!/usr/bin/env python3

import requests

from config import TOKEN, URL, parametrs


def send_telegram(text: str, photo):
    # method = URL + TOKEN + "/sendMessage"
    method = URL + TOKEN + "/sendPhoto"
    parametrs['caption'] = text
    parametrs['photo'] = photo

    r = requests.post(method, data=parametrs)

    if r.status_code != 200:
        raise Exception("post_text error")


if __name__ == '__main__':
    send_telegram("hello world!", 'https://sun9-80.userapi.com/s/v1/if2/PV1I3x_pib5fxsL9cTpSns8lABE'
                                  '-chw479fuzIR0XPPTflO70x-l1EfuGbXYhQGydSfIwsR18h2nswUtvSgK8PnO.jpg?size=554x600'
                                  '&quality=96&type=album')
