#!/usr/bin/env python2
# -*- coding: utf8 -*-

from io import open
import yaml
import os
import glob
from taemin import config

class TaeminConf(object):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    def __init__(self, filename=None):
        if not filename:
            filename = config.conf_dir + "/taemin.yml"
        self.config = {}
        self.add_to_conf(filename)
        self.plugin_confs = self.check_for_conf()
        for conf in self.plugin_confs:
            self.add_to_conf(conf)

        self.add_to_conf(filename)


    def add_to_conf(self, conf_file):
        with open(conf_file, 'r', encoding='utf-8') as stream:
            self.config.update(yaml.load(stream), allow_unicode=True)

    def check_for_conf(self):
        conf_file = []
        for path in self.config.get("plugins", {}).iterkeys():
            dirpath = os.path.dirname(path.replace(".", "/"))
            conf_file.extend(glob.glob(os.path.join(self.__location__, dirpath,  "*.yml")))
        return conf_file

if __name__ == "__main__":
    print(TaeminConf().config)
