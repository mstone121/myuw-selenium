#!/bin/python

# myuw mobile user class

from myuw_selenium.test.mudata import *
from myuw_selenium.test.musettings import *
import selenium.common.exceptions
import time

# Class for a user
# MyUW test user class
# This constructor assumes sensible defaults for anything not
# explicitly defined, as shown below
# Arguments:
# driver: the driver to use. Not used anymore. 
# test: the test object to use. Not used anymore. 
# urlbase: the base URL to use to construct the other URLs
# critical: number of critical notices
# unread: number of unread notices
# email: which email link the user should have. These are in mudata.py
# regcard: either a regcard to look for (the title of the card), or a list of titles to check for. 
# regholds: number of holds on registration
# reglinks: registration card links to check for. Should be link objects. 
# schedule: whether the user has a current schedule or not
#    If schedule is true, then it is expected that you will supply 'courses'
# courses: list of course names to check for, e.g. 'BCWRIT 500 A'
# futureQrts: list of future quarters to check for, in the order they would appear on the page, eg ['Spring 2013']
# vSchedule: whether to check for vis schedule or not
#    This checks to make sure the courses found on the vsched are the same as those in 'courses'
# noregfound: whether or not the user should have a 'no registration found' card
# resources: what resource links the user should have
#    These are in resourcelinks.py
# record: Whether to check for myrecords. Either False to not check, or a records object which the other Matt did so I have no clue what the correct format is. 
# academic card: either False to not check, or a dictionary with stuff
# grade_card: see above
# tuition: same
# HFS: what HFS cards the user should have (or False to note check). 
#    Values are 'stu' (student), 'din' (dining), and 'staff'. 
# library: Whether or not there should be a library card
# libraryholds: # of library holds
# libraryout: # of checked out items
# libraryfine: whether or not the user has a library fine 
# regMsgs: registration messages
# textbooks: name of classes for which the user should have textbooks
#    same format as courses
# fq_fall: classes for future quarter fall
# fq_summera, fq_summerb: as above

# Please note that the actual test functions have been moved to muwm_cases.py

class testUser():
    def __init__(self, driver, test, **kwargs):
        
        self.driver = driver
        self.test = test
        self.urlbase = test.live_server_url

        # Default values
        self.critical = 0
        self.unread = 0
        self.email = False
        self.regcard = False
        self.regholds = 0
        self.reglinks = ()
        self.schedule = False
        self.courses = ()
        self.futureQtrs = ()
        self.vSchedule = False
        self.noregfound = False

        self.resources = {}
        self.record = False

        self.academic_card = False
        self.grade_card = False
        
        self.tuition = False
        self.HFS = False
        self.library = False
        self.libraryholds = 0
        self.libraryout = 0
        self.libraryfine = False
        self.regMsgs = False
        self.textbooks = ()

        self.fq_fall = ()
        self.fq_summera = ()
        self.fq_summerb = ()

        # Set everything up from the constructor
        # Anything not done here will keep its default value from above
        # Why can't we just set defaults in the arguments for __init__?
        # Because those won't show up in *args/**kwargs, so we can't
        # set everything automatically like this. 
        for k, v in kwargs.items():
            if v is not None:
                setattr(self,k, v)
        
        # If the landing/admin/resource URL suffixes are 
        # defined, combine them with the urlbase to get the
        # full url. Otherwise, use the defaults. 
        try: 
            self.landing = self.urlbase + self.landingsuffix 
        except:
            self.landing = self.urlbase + landing

        try:
            self.admin = self.urlbase + self.adminsuffix
        except:
            self.admin = self.urlbase + admin

        try:
            self.res = self.urlbase + self.ressuffix
        except:
            self.res = self.urlbase + res

        try:
            self.dates = self.urlbase + self.datesuffix
        except:
            self.dates = self.urlbase + dates
        



        # Workadound for MUWM-1930
        # Bug fixed, workaround no longer needed
        #if self.courses:
        #    self.vcourses = []
        #    for courseName in self.courses:
        #        nameSplit = courseName.split()
        #        name = ' '.join(nameSplit[:-1]) + nameSplit[-1]
        #        self.vcourses.append(name)

        # With the bug fixed, just copy the list
        if self.courses:
            self.vcourses = list(self.courses)

        



# Not used yet
# Probably won't use it since there's no real reason to have a different class for this. 
class testUserDate(testUser):
    pass
