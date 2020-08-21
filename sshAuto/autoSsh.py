import paramiko
import os
import subprocess

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.75', username = 'root', password='Pactera@ht123')
    containerName = 's'

    # command_stdout = subprocess.Popen(['docker', 'ps'], stdout=subprocess.PIPE).communicate()#这个命令可用

    # stdin, stdout, stderr = ssh.exec_command('docker ps|grep {containerName}'.format(containerName=containerName))
    # stdin, stdout, stderr = ('docker ps -a |grep {containerName}'.format(containerName=containerName))
    # stdin, stdout, stderr = ssh.exec_command('docker ps -a |grep htapirasal1help')
    # stdin, stdout, stderr = ssh.exec_command('docker ps|grep bertencodeapi_dd')
    # docker ps --format "table {{.ID}}\t{{.Names}}"|awk '{print $1}'
    str_docker_lookup = 'docker ps -a |grep {containerName}'.format(containerName=containerName)+"|awk '{print $1}'"
    out_bytes = subprocess.check_output(str_docker_lookup, shell=True).decode("utf-8") 
    results =  [x for x in out_bytes.split('\n') if x]


    # res1，ret,resy = subprocess.Popen('docker ps -q|grep sqlserver2019',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
    # while True:
    #     line = res.stdout.readline()
    #     if not line:
    #         break
    #     #the real code does filtering here
    #     print(line.rstrip())
    # result = res.stdout.readline()
    # result = res.stdout.readlines()


    # r = os.popen('docker ps -q |grep htapirasal1help')  
    # text = r.readlines()  
    # r.close() 

    # completed = subprocess.run('docker ps -q',shell=True)
    # print(completed.returncode)
    # status = stdout.channel.recv_exit_status()
    # print(status)
    # stdin, stdout, stderr = ssh.exec_command('lsof -i:9000')
    # portTryCount = 1
    # while stdout.channel.recv_exit_status() == 0:
    #     stdin, stdout, stderr = ssh.exec_command('lsof -i:9100')
        
    # stdin, stdout, stderr = ssh.exec_command('ps -ef')
    print(stdout)
    ssh.close()
except Exception as e:
    print(e)
try:
    pass
except expression as identifier:
    pass
finally:
    ssh.close()

