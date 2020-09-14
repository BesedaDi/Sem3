import os
import tempfile
import json
import argparse

def pars_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', dest='key_name')
    parser.add_argument('--val', dest='value')
    return parser.parse_args()

def read_storage(file_name):
    with open(file_name) as f:
        storage = json.load(f)

    return storage

def rec_storage(storage):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(storage, f)

def work():
    args = pars_arg()
    storage = dict()
    key = args.key_name
    val = args.value
    if key not in storage:
        storage[key] = val
    else:
        

    print('Key "{}" = {}'.format(key, val))
    rec_storage(storage)




