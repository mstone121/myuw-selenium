#!/bin/python

# myuw mobile user class

from myuw_selenium.test.mudata import *
from myuw_selenium.test.musettings import *
import selenium.common.exceptions
import time

# Class for a user
class testUser():
    def __init__(self, driver, test, **kwargs):
        self.driver = driver
        self.test = test

        self.urlbase = test.live_server_url

        # This is a hacky way of doing this but it beats typing everything twice    
        self.critical = 0
        self.unread = 0
        self.email = False
        self.regcard = False
        self.regcard2 = False
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
        for k, v in kwargs.items():
            if v is not None:
                setattr(self,k, v)
            #self.__setattr__(k, v)
        
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

        



    # Run every check
    # Comment a line out here if you don't want it to run
    def run_all_tests(self):
    # Function to run all individual checks
        for test in self.all_tests:
            test(self)

class testUserDate(testUser):
    pass
