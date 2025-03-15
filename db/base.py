from tinydb import TinyDB, Query
import os
from datetime import datetime

if not os.path.exists("db/system_diagnostics.json"):
    open("db/system_diagnostics.json", "w").close()


db = TinyDB('db/system_diagnostics.json')
print(db)
diagnostics_table = db.table('diagnostics')


def create_diagnostics(data: dict):

    res = diagnostics_table.insert({
        'timestamp': datetime.timestamp(datetime.now()),
        'cpu_usage': data['cpu'],
        'memory_usage': data['mem'],
        'disk_usage': data['disk'],
        'bytes_sent_MB': data["bytes_sent_MB"],
        'bytes_recv_MB': data['bytes_recv_MB']
    })


def get_diagnostics(inteval: int):
    all_entries = diagnostics_table.all()
    res = all_entries[-inteval:]
    print(res)
    return res


