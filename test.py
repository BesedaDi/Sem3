import os
import tempfile
import json
import os
import tempfile
import json
import argparse


def pars_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', dest='key_name')
    parser.add_argument('--val', dest='value')
    return parser.parse_args()


def read_storage():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        storage = json.load(f)
    return storage


def rec_storage(storage):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(storage, f)


args = pars_arg()
storage = dict()
key = args.key_name
val = args.value
storage_file_name = os.path.join(os.path.dirname(__file__), 'storage.data')
if key != None and val != None:
    if not os.path.exists(storage_file_name):
        lst = []
        if key not in storage:
            storage[key] = val
        else:
            for k, v in storage.items():
                if key == k:
                    lst.append(val)
                    storage[key] = lst
                    storage[key] = lst.append(v)
        print('Key "{}" = {}'.format(key, val))
        print(storage)
        print('123456789')

        rec_storage(storage)
    else:
        storage = read_storage()
        lst = []
        if key not in storage:
            storage[key] = val
        else:
            for k, v in storage.items():
                if key == k:
                    lst.append(val)
                    storage[key] = lst
                    storage[key] = lst.append(v)
        print('Key "{}" = {}'.format(key, val))
        rec_storage(storage)
    print(storage)
elif key != None:
    storage = read_storage()
    print(storage)

    el = ''
    for k, v in storage.items():
        print(k, v)
        if k == key:
            el = v
            print(v)
    if el == '':
        print(None)
