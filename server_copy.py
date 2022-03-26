#!/usr/bin/python3

import argparse
import random
import os
import sys

server_name = ''
server_directory_name = ''
server_dir = server_name + ':' + server_directory_name
server_access_dir = ''

def copy_file():
    filename = args.filename

    if args.alternative != None:
        new_filename = args.alternative

    elif args.random_alternative == True:
        if len(filename.split('.')) > 1:
            new_filename = str(random.randint(0, 10000))+'.'+filename.split('.')[-1]
        else:
            new_filename = str(random.randint(0, 10000))
    else:
        new_filename = filename

    exit_code = os.system(f'scp {filename} {server_dir}{new_filename}')

    if exit_code == 0:
        print(server_access_dir+new_filename)
    else:
        sys.exit(1)

def copy_link():

    link = args.link

    if args.alternative != None:
        new_filename = args.alternative

    elif args.random_alternative == True:
            new_filename = str(random.randint(0, 10000))
    
    elif args.filename != None:
        new_filename = args.filename
    else:
        print('please specify a filename')
        sys.exit(1)

    command_remote = f'wget -O {server_directory_name}{new_filename} "{link}"'
    command_filename = '/tmp/copy_remote_command.sh'
    with open(command_filename, 'w') as command_file:
        print('#!/usr/bin/bash', file=command_file)
        print(command_remote, file=command_file)

    exit_code = os.system(f'ssh {server_name} bash -s < {command_filename} ')
    if exit_code == 0:
        print(server_access_dir+new_filename)
    else:
        sys.exit(1)


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

if args.link != None:
    print(args.link)
    copy_link()

elif args.filename != None:
    print(args.filename)
    copy_file()
