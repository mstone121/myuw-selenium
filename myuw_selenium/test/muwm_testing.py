#!/usr/bin/python

# Matt's MYUW Mobile test

# What these tests will check for:
# Landing page:
# * Correct number of critical notices 
# * Correct number of unread notices 
# * Correct email link, or lack thereof
# * Presense of registration card, if expected
# * Correct link names and URLs of registration resource links
# * Correct course card titles
# * Correct visual schedule course titles
# * Correct HFS husky card names
# * Library card present if expected
# * Correct number of library holds ready, if expected
# * Correct number of checked out items, if expected
# * Correct value of library fine, if expected
# * Presense of each expected future quarter
# * Lack of error messages
# * Check "No registration found" if expected
# * Check name and URLs of resource page links
# TODO: Notices page, tuition 

# Test cases/suites available:
# * myuw_<user>: Run all tests for a user
# * myuw_<user>.test: Run a particular test for a user
# * myuw_<user>._test_fast: Run all tests for that user 
#        combined into one test. Executes faster, but will
#        stop on first failed test
# * myuw_mock: Run all tests on mock data users
# * myuw_mock_fast: Run fast test on all mock users
# * myuw_prod: Run all tests on production users
# * myuw_prod_fast: Run fast test on all prod users
# If you create more users, be sure to add them to the 
# appropriate lists at the bottom, just above the suites. 

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import time
import sys
import os
from myuw_selenium.platforms import on_platforms, SeleniumLiveServerTestCase

# Myuw specific stuff
#import netid
#from myuw import link
from myuw_selenium.test.myuw_user import testUser, testUserDate
from myuw_selenium.test.musettings import *
from myuw_selenium.test.mudata import *
from myuw_selenium.test.resourcelinks import resLinks
from myuw_selenium.test.records import records
from myuw_selenium.test.academic_card import academic_card_values
from myuw_selenium.test.grade_card import grade_card_values

from muwm_cases import myuw_user_scenario, myuw_date_scenario

# Set up a virtual display if we're on a supported system
# and the DISPLAY variable does not appear to be set. 
p = sys.platform

if p in ('win32', 'mac', 'darwin'):
    pass
else:
    if os.environ.get('DISPLAY'):
        pass
    else:
        import pyvirtualdisplay
        vd = pyvirtualdisplay.Display(visible = 0, size = (800, 600))
        vd.start()
            


# Function to run all individual checks quickly
# (without restarting browser every time)
def _test_fast(self):
    if self.__class__ != myuw_user_scenario:
        #self.browse_landing()
        self.user.run_all_tests()


# Function to run an individual test
# Hacks required due to tests providing a test
# object but the check_* functions requiring
# the user object
def g_test_call_func(self):
    name = self._testMethodName[5:]
    return getattr(self.user, name)()
    



# Mock data user scenarios

@on_platforms()
class myuw_jbothell_date1(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            critical = 4, 
            unread = 10, 
            email = emails['live'], 
            regcard = True, 
            regholds = 1, 
            reglinks = (links['bts'], links['reg']), 
            schedule = True, 
            vSchedule = True,
            courses = ('BCWRIT 500 A', 'BISSEB 259 A', 'BESS 102 A', 'BESS 102 AB'), 
            tuition = {'balance' : True, 'due' : 'future'},
            HFS = ('stu',), 
            library = True, 
            libraryholds = 1, 
            textbooks = ('BISSEB 259 A', 'BCWRIT 500', 'BESS 102 A', 'BESS 102 AB'),
            resources = resLinks['bothell'],
            record = records['jbothell'],
            academic_card = academic_card_values['jbothell']
        )
        self.username = 'jbothell'
        self.setDate('2013-04-12')
             
'''
# jbothell user scenario
#class myuw_jbothell(SeleniumLiveServerTestCase):
@on_platforms()
class myuw_jbothell(myuw_user_scenario, SeleniumLiveServerTestCase):


    def postsetup(self):
        self.user = testUser(self.driver, self, 
            critical = 4, 
            unread = 10, 
            email = emails['live'], 
            regcard = True, 
            regholds = 1, 
            reglinks = (links['bts'], links['reg']), 
            schedule = True, 
            vSchedule = True,
            courses = ('BCWRIT 500 A', 'BISSEB 259 A', 'BESS 102 A', 'BESS 102 AB'), 
            tuition = {'balance' : True, 'due' : 'future'},
            HFS = ('stu',), 
            library = True, 
            libraryholds = 1, 
            textbooks = ('BISSEB 259 A', 'BCWRIT 500', 'BESS 102 A', 'BESS 102 AB'),
            resources = resLinks['bothell'],
            record = records['jbothell'],
            academic_card = academic_card_values['jbothell']
        )
        self.username = 'jbothell'
    
    def test_blah(self):
        pass
# javerage user scenario
@on_platforms()
class myuw_javerage(myuw_user_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            critical = 5, 
            unread = 11, 
            email = emails['gmail'], 
            regcard = True, 
            regholds = 1, 
            reglinks = (links['sts'], links['reg']), 
            schedule = True, 
            vSchedule = True,
            courses = ('PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A'), 
            #tuition = 'duefuture', 
            HFS = ('stu', 'staff', 'din'), 
            library = True, 
            libraryholds = 1, 
            libraryout = 1, 
            fq_fall = ('ENGL 207 A',), 
            fq_summera = ('ELCBUS 451',), 
            fq_summerb = ('TRAIN 101',),
            resources = resLinks['seattle'],
            record = records['javerage'],
            academic_card = academic_card_values['javerage'],
            #grade_card = grade_card_values['javerage']
        )
        # TODO: Add textbooks
        self.username = 'javerage'
@on_platforms()
class myuw_jinter(myuw_user_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self,
            critical = 4,
            unread = 13, 
            email = False,
            regcard = False,
            schedule = False,
            vSchedule = False,
            #tuition = 'nofuture',
            HFS = ('staff',),
            library = True,
            libraryout = 1 ,
            libraryfine = '$3.25',
            resources = resLinks['seattle'],
            record = records['jinter']
        )        
        self.username = 'jinter'

@on_platforms()
class myuw_jnew(myuw_user_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            critical = 2, 
            unread = 18, 
            email = False,
            regcard = False,
            schedule = True,
            vSchedule = True,
            courses = ('TRAIN 101 A',),
            #tuition = 'nopast',
            HFS = ('stu', 'din'),
            library = True,
            libraryfine = '$10.00',
            resources = resLinks['seattle'],
            record = records['jnew']
        )
        self.username = 'jnew'

@on_platforms()
class myuw_none(myuw_user_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self,
            regcard = True,
            noregfound = True,
            HFS = (),
            record = records['none']
        )
        self.username = 'none'
'''

@on_platforms()
class myuw_none_date1(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = 'Registration: Spring 2013', 
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-02-01')

@on_platforms()
class myuw_none_date2(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = 'Registration: Spring 2013', 
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-02-15')


@on_platforms()
class myuw_none_date3(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = 'Registration: Spring 2013', 
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-03-04')

@on_platforms()
class myuw_none_date4(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-03-11')

@on_platforms()
class myuw_none_date5(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-04-01')

@on_platforms()
class myuw_none_date6(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = 'Registration: Summer 2013',
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-04-08')

@on_platforms()
class myuw_none_date7(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = ['Registration: Summer 2013'],
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-04-22')

@on_platforms()
class myuw_none_date8(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = ['Registration: Autumn 2013','Registration: Summer 2013'],
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-05-23')

@on_platforms()
class myuw_none_date9(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = 'Registration: Autumn 2013',
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-05-30')


@on_platforms()
class myuw_none_date10(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-07-01')


@on_platforms()
class myuw_none_date11(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = ['Registration: Winter 2014'],
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-10-25')

@on_platforms()
class myuw_none_date12(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            tuition = {'balance' : False, 'due' : 'future'},
            HFS = (), 
            records = records['none'],
            noregfound = True,
        )
        self.username = 'none'
        self.setDate('2013-12-02')

@on_platforms()
class myuw_javerage_date1(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            noregfound = False
            
        )
        self.username = 'javerage'
        self.setDate('2013-07-01')

@on_platforms()
class myuw_javerage_date2(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            noregfound = False,
            futureQtrs = ['Spring 2013']
            
        )
        self.username = 'javerage'
        self.setDate('2013-02-15')

@on_platforms()
class myuw_javerage_date3(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            noregfound = False,
            futureQtrs = []
            
        )
        self.username = 'javerage'
        self.setDate('2013-04-01')

@on_platforms()
class myuw_javerage_date4(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            noregfound = False,
            futureQtrs = ['Summer 2013 A-Term', 'Summer 2013 B-Term', 'Autumn 2013']
            
        )
        self.username = 'javerage'
        self.setDate('2013-04-08')

@on_platforms()
class myuw_javerage_date5(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            noregfound = False,
            futureQtrs = ['Autumn 2013',]
            
        )
        self.username = 'javerage'
        self.setDate('2013-06-24')

@on_platforms()
class myuw_javerage_date6(myuw_date_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            regcard = False,
            noregfound = False,
            futureQtrs = []
            
        )
        self.username = 'javerage'
        self.setDate('2013-09-25')


'''
@on_platforms()
class myuw_eight(myuw_user_scenario, SeleniumLiveServerTestCase):
    def postsetup(self):
        self.user = testUser(self.driver, self, 
            critical = 7,
            unread = 10,
            email = emails['gmail'],
            regcard = False, 
            reglinks = (links['tts'], links['tqs'], links['reg']),
            schedule = True,
            vSchedule = True,
            courses = ('PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A', 'ASL 101 A', 'ROLING 310 A', 'ARCTIC 200 A'),
            tuition = {'balance' : True, 'due' : 'today'},
            HFS = ('stu', 'din'),
            library = True,
            libraryholds = False,
            libraryout = 2,
            libraryfine = '$5.00',
            fq_summera = ('ELCBUS 451 A', 'B BIO 180 A'),
            fq_summerb = ('TRAIN 101 A', 'B BIO 180 A'),
            fq_fall = ('ENGL 207 A',),
            textbooks = ('PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A', 'ASL 101 A', 'ROLING 310 A', 'ARCTIC 200 A'),
            resources = resLinks['tacoma'],
            record = records['eight'],
            academic_card = academic_card_values['eight'],
            #grade_card = grade_card_values['eight']
        )

        self.username = 'eight'
# TODO: tuition due date stuff
'''

'''
# Test suites:
mock_users = (myuw_eight, myuw_jinter, myuw_none, myuw_jnew, myuw_javerage, myuw_jbothell)
test_one = (myuw_javerage,)

def myuw_mock_fast():
    suite = unittest.TestSuite()
    for c in mock_users:
        suite.addTest(c('_test_fast'))
    return(suite)

def myuw_mock():
    suite = unittest.TestSuite()
    for c in mock_users:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(c))
    return(suite)

def myuw_test_one():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_one[0]))
    return(suite)
    
'''
if __name__ == "__main__":
    #unittest.main(warnings = 'ignore')
    unittest.main()
