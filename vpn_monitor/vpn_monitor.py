#coding: utf-8

#author: Reed Xia(huaqin2005@gmail.com)

import smtplib
import config
import requests
# import urllib.request as urllib2
import time
import base64
import socket
import traceback


last_email_sent_time = None
error_info = None
catch_exception = False


def send_email(text):
    global last_email_sent_time
    if last_email_sent_time is None:
        last_email_sent_time = time.localtime()
    else:
        now = time.localtime()
        if now.tm_hour - last_email_sent_time.tm_hour > 2:
            last_email_sent_time = now # only send out email at the first time or 1 h later
        else:
            print("Less than 1 hour since last email alert, no email this time. - " + get_time())
            return

    print("Try to send email - " + get_time())
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

    try:
        server = smtplib.SMTP()
        print(host_server)
        print(body)
        server.connect(host_server, config.sent_port)
        server.starttls()
        server.login(config.email_account, base64.b64decode(config.email_pw.decode()).decode())
        server.sendmail(from_, to, body)
        server.quit()
        print("Finish sending email - " + get_time())
    except Exception as err:
        print("Exception on sending email at" + get_time())
        print(err.args)
        # raise


def connect_to(url):
    try:
        # urllib2.urlopen(url, timeout = 10)
        requests.get(url, timeout=3)
        return True
    # except socket.timeout as timeout_error:
    #     return False
    except Exception as err:
        # print("Exception - " + get_time())
        # print('----------------------------------------------------')
        # print(err.__dir__())
        # print('----------------------------------------------------')
        # traceback.print_tb()
        # print('----------------------------------------------------')
        traceback.print_exc()
        # print('----------------------------------------------------')
        global error_info
        global catch_exception
        error_info = str(traceback.format_stack())
        catch_exception = True
        return False


def check_network(url):
    bad_network = 0
    for i in range(4):
        if not connect_to(url):
            print("[" + str(i) + "] " + "check_network: fail to open " + url + " at " + get_time())
            bad_network += 1
            time.sleep(5)
        else:
            break
    if bad_network == 4:
        return False
    else:
        return True


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_email_text():
    global catch_exception
    if not catch_exception:        
        return "Hello! Google is disconnected at " + get_time()
    else:
        catch_exception = False
        return "Hello! Exception is found at " + get_time() + "\n" + error_info

if __name__ == '__main__':
    print("VPN Monitor is started at " + get_time())
    while True:
        if not check_network(config.google_url):
            send_email(get_email_text())
        else:
            print("Google is ok at " + get_time())
        time.sleep(90)
