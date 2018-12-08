import paramiko


def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print(str(stdout.read(), encoding='utf-8'))

    except Exception as e:
        print("Issue:", e)
    finally:
        ssh.close()

if __name__ == "__main__":
    
    ssh2("167.99.10.90", "root", "*mypwd**", "uname -a;pwd;ifconfig")