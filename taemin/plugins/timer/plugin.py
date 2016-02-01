#!/usr/bin/env python2
# -*- coding: utf8 -*-

from threading import Thread
import time
import re

class Timer(Thread):
    def __init__(self, taemin, _time, chan, msg = ""):
        Thread.__init__(self)
        self.taemin = taemin
        self._time = _time
        self.users = []
        self.chan = chan
        if msg == "":
            self.msg = "Il est l'OR !!!"
        else:
            self.msg = msg

    def run(self):
        time.sleep(self._time)
        self.taemin.connection.privmsg(self.chan, self.msg)

class TaeminTimer(object):
    helper = {"timer": "Dit un mot dans x seconde. Usage: !timer seconde message"}

    def __init__(self, taemin):
        self.taemin = taemin
        self.nb_timer = 0

    def on_pubmsg(self, serv, msg):
        if msg.key != "timer":
            return
        chan = msg.chan.name

        m = re.search("^(\d+)\s*(.*)$", msg.value)
        if m:
            self.nb_timer += 1
            _time = int(m.group(1))
            msg = m.group(2)
            if msg == "":
                msg = "Il est l'OR !!!"

            msg = "[Timer %d] Fin : %s" % (self.nb_timer, msg)
            timer = Timer(self.taemin, _time, chan, msg)
            timer.start()
            serv.privmsg(chan, "[Timer %d] Démarre pour %s secondes" % (self.nb_timer, _time))
        else:
            serv.privmsg(chan, "[Timer] Usage : Temps (en s) + message (facultatif), ex : !timer 666 Pouet")

