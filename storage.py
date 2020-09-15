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
storage = read_storage()
key = args.key_name
val = args.value
if key != None and val != None:
    if key not in storage:
        storage[key] = list(str(val))
    else:
        for k, v in storage.items():
            if key == k:
                if isinstance(v, list):
                    storage[key].append(v)
                else:
                    storage[key] = list(val)
                    storage[key].append(v)

    print(storage)
    print('Key "{}" = {}'.format(key, val))

    # print(storage)

    rec_storage(storage)

elif key != None:
    storage = read_storage()

    if key in storage.keys():
        for k, v in storage.items():
            if k == key:
                print(v)

    else:
        print(None)
