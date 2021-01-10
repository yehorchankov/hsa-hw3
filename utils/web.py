from datetime import timedelta
import datetime

import requests


def get_latest_ts(limit=100, offset=1000, now=None, latest_tran=None):
    if offset < 0:
        return latest_tran

    now = (datetime.datetime.utcnow() - timedelta(minutes=3)).isoformat() if not now else now
    request = f'https://wax.cryptolions.io/v2/history/get_actions?limit={limit}&simple=true&checkLib=true&before={now}&skip={offset}'

    try:
        response = requests.get(request).json()['simple_actions']
    except Exception as e:
        print(e)
        return latest_tran

    if all([r['irreversible'] for r in response]):
        # If all transactions in this batch are irrev, move to the next batch
        return get_latest_ts(limit, offset - limit, now, response[0])
    elif any([r['irreversible'] for r in response]):
        # If some transactions are irrev, find latest
        latest_tran = list(filter(lambda x: x['irreversible'], response))[0]
        return latest_tran
    else:
        return latest_tran
