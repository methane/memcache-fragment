from __future__ import print_function, division, absolute_import

import memcache


def main():
    client = memcache.Client(['localhost:11211'])
    size = 16
    keys = ["key%d" % i for i in range(10000)]

    while size < 16*1024:
        print(size, len(keys))
        data = b'a' * size
        for k in keys:
            client.set(k, data)
        size = size * 4 // 3
        del keys[::8]

main()
