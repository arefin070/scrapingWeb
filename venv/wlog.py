import logging

def set_customer_log_info(filename):
    logging.basicConfig(filename=filename , level= logging.INFO)

def report(e:Exception):
    logging.exception(str(e))
