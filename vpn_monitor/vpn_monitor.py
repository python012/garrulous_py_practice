#coding: utf-8

#author: Reed Xia(huaqin2005@gmail.com)

import smtplib
import config
import requests
import time
import base64
import sys
import traceback
import logging

last_email_sent_time = None
error_info = ""
catch_exception = False
logger = logging.getLogger("VPN monitor")
logger.setLevel(level=logging.DEBUG)

# file handler
file_handler = logging.FileHandler(time.strftime("%Y-%m-%d_%A_%H%M%S", time.localtime()) + '.log')
file_handler.setLevel(level=logging.DEBUG)
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# stream handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
stream_handler.setFormatter(log_format)
logger.addHandler(stream_handler)


def send_email(text):
    global last_email_sent_time
    if last_email_sent_time is None:
        last_email_sent_time = time.localtime()
    else:
        now = time.localtime()
        if now.tm_hour - last_email_sent_time.tm_hour > 2:
            last_email_sent_time = now # only send out email at the first time or 1 h later
        else:
            logger.info("Less than 1 hour since last email alert, no email this time. - " + get_time())
            return

    logger.info("Try to send email - " + get_time())
    host_server = config.host_server
    subject = config.subject + " - " + get_time()
    # to = config.to
    # from_ = config.from_
    body = "\r\n".join((
            "From: %s" % config.from_,
            "To: %s" % config.to,
            "Subject: %s" % subject,
            "",
            text))

    try:
        server = smtplib.SMTP()
        server.connect(host_server, config.sent_port)
        server.starttls()
        server.login(config.email_account, base64.b64decode(config.email_pw.decode()).decode())
        server.sendmail(config.from_, config.to, body)
        server.quit()
        logger.info("Finish sending email - " + get_time())
    except Exception as err:
        logger.error("Exception on sending email at" + get_time())
        logger.error(err.args)
        # raise


def connect_to(url):
    try:
        requests.get(url, timeout=10)
        return True
    except Exception as err:
        logger.error(err.args)
        global error_info
        error_info = err.args
        return False


def check_network(url):
    bad_network = 0
    for i in range(4):
        if not connect_to(url):
            logger.warning("[" + str(i) + "] " + "check_network: fail to open " + url + " at " + get_time())
            bad_network += 1
            time.sleep(5)
        else:
            break
    if bad_network == 4:
        return False
    else:
        return True


def get_time():
    return time.strftime("%Y-%m-%d %A %H:%M:%S", time.localtime()) #2018-11-19 Monday 18:59:12


def get_email_text():
    return "Hello! Google is disconnected at " + get_time() + "\n\nException info:\n\n" + str(error_info)


if __name__ == '__main__':
    logger.info("VPN Monitor is started at " + get_time())
    while True:
        if not check_network(config.google_url):
            send_email(get_email_text())
            error_info = ""
        else:
            logger.info("Google is ok at " + get_time())
        time.sleep(90)
