# server copy (cs command)
copy a file from your local machine into server and get a link.

alternatively, download a link from web on your server and get a link so you can somehow proxy downloading a file.

## install
1. edit `server_copy.py` file:

set `server_name` to servername with the username. for instance:  

```bash
erfan@server.com
```

set `server_directory_name` to directory you want to copy files into. for instance:  

```bash
/home/erfan/Downloads/
```

set `server_access_dir` to the link connected to the directory. for instance:  

```bash
https://server.com/files/
```

for doing this, you need to set a reverse proxy or alias in your webserver application (nginx, apache,...).  

2. run script `install.sh`:  

```bash
./install.sh
```

## usage

run this with `cs` command:

```bash
cs --help
```

to copy a file into server:

```bash
cs filename
```

to give an alternative name to file in the server use `-a` option. to have a random alternative name use `-r` option.

