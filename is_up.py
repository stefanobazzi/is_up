#!/usr/bin/env python3

from __future__ import print_function

import socket
import time
import argparse


def connect(host, port, timeout):
    s = socket.socket()
    while timeout:
        try:
            s.connect((host, port))
            print("{}:{} is up".format(host, port))
            s.close()
            return
        except socket.error:
            print("{}:{} is down".format(host, port))
            timeout -= 1
            time.sleep(1)
    print("{}:{} is not reachable, timeout expired".format(host, port))


def main():
    parser = argparse.ArgumentParser(description='Try to connect to host:port \
                                                  until timeout expires')
    parser.add_argument('host', type=str, help='Host IP address')
    parser.add_argument('port', type=int, help='Host port')
    parser.add_argument('--timeout', type=int, default=60,
                        help='Timeout in seconds')

    args = parser.parse_args()
    connect(args.host, args.port, args.timeout)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
