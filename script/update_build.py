#!/usr/bin/python

import sys

# libraries to pip install:
from paramiko import SSHClient, AutoAddPolicy, Transport, SFTPClient

# Host parameters
print(sys.argv)
x, host, username, password = sys.argv
port = '22'
ftp_port = '21'

# Ftp Connection
transport = Transport((host, int(ftp_port)))
transport.connect(username=username, password=password)
sftp = SFTPClient.from_transport(transport)

# Connecting to host
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)

# Executing commands
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo test')

print(ssh_stdout)

