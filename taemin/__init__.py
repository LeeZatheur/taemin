#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.1"

#from bot import Taemin
import conf
import database
import logging
import logging.handlers
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Env(object):
    def __init__(self):
        self.conf = conf.TaeminConf().config
        db_conf = self.conf.get("database", {})

        self.db = database.DataBase(db_conf.get("type", "mysql"),
                           name=db_conf.get("name", "/etc/taemin/taemin.db"),
                           user=db_conf.get("user", ""),
                           password=db_conf.get("password", ""),
                           host=db_conf.get("host", "localhost"))

        self.log = self.init_logger()
        sys.excepthook = self.handler_exception

    def handler_exception(self, type, value, tb):
        self.log.exception("Uncaught exception: {0}".format(str(value)))

    def init_logger(self):
        filename = self.conf.get("general", {}).get("log_file", "/var/log/taemin.log")
        level = logging.INFO

        logger = logging.getLogger(__name__)
        logger.setLevel(level)
        handler = logging.handlers.TimedRotatingFileHandler(filename, when="midnight", backupCount=3)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

env = Env()
