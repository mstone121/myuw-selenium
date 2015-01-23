#!/usr/bin/python

from myuw_selenium.test.musettings import *

class link():
    def __init__(self, text, url):
        self.text = text
        self.url = url

    def __repr__(self):
        return('<link "%s" to %s>' %(self.text, self.url))

    def __str__(self):
        return('Link named "%s"' %self.text)

    def __eq__(self, other):
        return(self.text == other.text and self.url == other.url)

    # Comparisons are necessary for sorting
    def __gt__(self, other):
        return(self.text > other.text)

    def __lt__(self, other):
        return(self.text < other.text)



