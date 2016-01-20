#!/usr/bin/env python2
# -*- coding: utf8 -*-

class TaeminSayNo(object):
    def __init__(self, taemin):
        self.taemin = taemin
        self.non_keyword = self.taemin.conf.get("SayNo", {}).get("non_keyword", [])
        self.non_nick = self.taemin.conf.get("SayNo", {}).get("non_keyword", [])

    def on_pubmsg(self, serv, canal, message, **kwargs):
        if self._say_no(message):
            serv.privmsg(canal, "NON")

    def _say_no(self, message):
        test = False
        for nick in self.non_nick:
            if nick.lower() in message.lower():
                test |= True
        if not test:
            return False

        test = False
        for key in self.non_keyword:
            test |= key in message

        return test


