# server copy (cs command)
copy a file from your local machine into server and get a link.

alternatively, download a link from web on your server and get a link so you can somehow proxy downloading a file.

## install
1. edit `server_copy.py` file:

set `server_dir` to servername with the directory you want to copy files into. for instance:  

```bash
erfan@server.com:/home/erfan/Downloads/
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

