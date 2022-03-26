#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--alternative',
                    help='change name on the server to an alternative name')
parser.add_argument('-r', '--random-alternative',
                    help='change name on the server to a random name', action="store_true")
parser.add_argument("--quiet", '-q', help="do not output things",
                    action="store_true")
parser.add_argument('-l', '--link', help='get file from a link on the server')

parser.add_argument('filename', nargs='?', help='name of file to copy into server')

args = parser.parse_args()
