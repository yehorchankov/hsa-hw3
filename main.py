import time

from utils import web, ga


def main():
    prev_ts_id = None
    while True:
        ts = web.get_latest_ts()
        ts_id = ts.get('transaction_id') if ts else prev_ts_id
        prev_ts_id = ts_id if ts_id is not None else prev_ts_id
        print(ga.push_ts_id_old(ts_id))
        time.sleep(10)


if __name__ == '__main__':
    main()
