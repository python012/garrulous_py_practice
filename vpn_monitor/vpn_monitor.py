#coding: utf-8

import smtplib
import config
import urllib.request as urllib2
import time
import base64

email_is_sent = False
error_info = None
catch_exception = False

def send_email(text):
    print("Start to send email - " + get_time())
    host_server = config.host_server
    subject = config.subject + " - " + get_time()
    to = config.to
    from_ = config.from_
    body = "\r\n".join((
            "From: %s" % from_,
            "To: %s" % to,
            "Subject: %s" % subject,
            "",
            text))

    server = smtplib.SMTP()
    server.connect(host_server, config.sent_port)
    server.starttls()
    server.login(config.email_account, \
            base64.b64decode(config.email_pw.decode()).decode())
    server.sendmail(from_, to, body)
    server.quit()
    print("Finish sending email - " + get_time())


def connect_to(url):
    try:
        urllib2.urlopen(url, timeout = 10)
        return True
    except urllib2.URLError as urlerr:
        return False
    except Exception as err:
        print("Exception - " + get_time())
        global error_info
        global catch_exception
        error_info = str(err)
        catch_exception = True
        return False


def check_network(url):
    bad_network = 0
    for i in range(4):
        if not connect_to(url):
            print("[" + str(i) + "] " + "check_network: fail to open " + url + " at " + get_time())
            bad_network += 1
        time.sleep(5)
    if bad_network == 4:
        return False
    else:
        return True


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_email_text():
    global catch_exception
    if not catch_exception:        
        return "VPN Monitor: Google is disconnected at " + get_time()
        # + "\nConnected to Baidu status: " + str(baidu_status)
    else:
        catch_exception = False
        return "VPN Monitor: Exception is found at " + get_time() + "\n" + error_info

if __name__ == '__main__':
    time_interval = 30
    print("VPN Monitor is started at " + get_time())
    while True:
        if not check_network(config.google):
            #baidu_status = check_network(config.baidu)
            # global email_is_sent
            # if not email_is_sent:
            send_email(get_email_text())
            email_is_sent = True
            time_interval = 60 * 30
        else:
            time_interval = 30
            print("Google is ok at " + get_time())
        time.sleep(time_interval)
