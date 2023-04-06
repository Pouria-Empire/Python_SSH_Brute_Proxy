# Python_SSH_Brute_Proxy
Implement an example SSH Multithread brute frocer in  python using socks5 proxy list

This Python script is used to connect to a SSH server with multiple usernames, passwords, and proxies. It takes the list of usernames, passwords, and proxies from text files, and the list of SSH servers from a separate file. The script uses the paramiko library for establishing SSH connections and the requests library for checking the availability of the proxies.

#Requirements
Python 3.x
paramiko library
requests library
#Usage
Make sure you have all the required libraries installed.
Create the text files containing the list of usernames, passwords, proxies, and SSH servers. Make sure each item is separated by a new line.
Create a text file named ip.txt containing the list of SSH servers you want to connect to. Each server should be separated by a new line.
Run the script by running the following command in your terminal:
Copy code
$ python ssh_connect.py

The script will start connecting to each SSH server using the given usernames, passwords, and proxies. If a proxy is not available, it will try the next one until it finds a working proxy. If it fails to connect to a server using all the provided credentials, it will move on to the next server in the ip.txt file.
The script will print the successful connections on the console and also write them to a file named result.txt.
Note
The proxy list is optional. You can leave the proxies.txt file empty if you don't want to use a proxy.
The script may take a long time to complete if you have a large number of SSH servers and/or a large number of credentials.
