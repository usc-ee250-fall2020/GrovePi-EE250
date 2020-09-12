import requests
import socket

# Reddit API: https://github.com/reddit-archive/reddit/wiki/API

def qotd_init():
    headers = {
        # Reddit's API rules require a unique User-Agent. For this lab, please leave this as is
        'User-Agent': 'usc.ee250.lab8.' + socket.gethostname()
    }

    params = {
    }

    response = requests.get('http://www.reddit.com/r/quotes/random.json',
                            params=params, headers=headers)

    if response.status_code == 200: # Status: OK
        data = response.json()

        # TODO: Extract the quote from the data. Use pretty printing to help you decipher the json
        quote = 'Quote'

        print(quote)
        return quote

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None


QOTD_APP = {
    'name': 'Quote of the Day',
    'init': qotd_init
}


if __name__ == '__main__':
    qotd_init()
