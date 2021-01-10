import requests


def push_ts_id_old(ts_id):
    url = f'https://www.google-analytics.com/collect?v=1&t=event&tid=UA-186989395-1&cid=555&ec=wax-transactions&ea=latest-irreversible&el={ts_id}'
    print(f'Push ts id {ts_id}')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    return requests.get(url, headers=headers)
