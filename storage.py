import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()


def read():
    if not os.path.exists(storage_path):
        return None

    with open(storage_path, 'r') as f:
        data = f.read()
        if data == None:
            return {}
        else:
            return data


def func_write(key, value):
    info = json.loads(read())

    if key not in info:
        info[key] = [value]
    else:
        values = info.get(key)
        if values is list:
            info[key] = values.append(value)
        else:
            info[key] = [values, value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(info))


def keys(key):
    info_2 = json.loads(read())
    return info_2.get(key)


if args.key:
    ','.join(keys(args.key))
elif args.key != None and args.val != None:
    print(func_write(args.key, args.val))
else:
    print(None)
