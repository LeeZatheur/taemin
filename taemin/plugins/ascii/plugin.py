#!/usr/bin/env python2
# -*- coding: utf8 -*-

class TaeminAscii(object):
    def __init__(self, taemin):
        self.taemin = taemin

    def on_pubmsg(self, serv, msg):
        chan = msg.chan.name

        if msg.key == "taeminnie":
            serv.privmsg(chan, "  \\o/")
            serv.privmsg(chan, "   |")
            serv.privmsg(chan, "  / \\")

        elif msg.key == "shinee":
            serv.privmsg(chan, " <<<< SHINEE >>>>")
            serv.privmsg(chan, " \\o  o/\\o/\\o  o/")
            serv.privmsg(chan, "  |\\/|  |  |\\/|")
            serv.privmsg(chan, " / \\/ \\/ \\/ \\/ \\")

