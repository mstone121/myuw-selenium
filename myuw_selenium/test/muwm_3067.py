# Test for Summer final grades card
# See JIRA for reference

import os
import sys
import getpass
import unittest

from myuw_selenium.test.card_tests_c import CardTest, create_test_from_test
from myuw_selenium.platforms import LiveServerTestCase
from selenium.common.exceptions import TimeoutException

username = None
password = None

# try:
#     username = os.environ['MYUW_USERNAME']
# except KeyError:
#     username = input("Username: ")

# try:
#     password = os.environ['MYUW_PASSWORD']
# except KeyError:
#     password = getpass.getpass()

os.remove('db.sqlite3')
    
from django.core.management import execute_from_command_line


execute_from_command_line(['manage.py', 'syncdb'])


class MUWM_3067(CardTest):

    def date_wrapper(self, date):
        self.date = date
        self.setDate()
        self.driver.get(self.live_server_url + '/mobile/landing')


    def assert_no_card(self):
        try:
            card = self.getElement("div#GradeCard")
            assert "display: none" in card.get_attribute('style')        
        except TimeoutException:
            pass               

    def assert_classes(self, classes):
        elements = self.getElements("div#GradeCard span.card-badge-inline-label")
        texts = []
        for klass in elements:
            texts.append(klass.text.strip())

        for klass in classes:
            assert klass in texts, texts

# Tests
class STEP_01(MUWM_3067):
    def _test(self):
        self.date_wrapper('2013-07-24')
        self.assert_no_card()
        
class STEP_02(MUWM_3067):
    def _test(self):
        self.date_wrapper('2013-07-25')
        self.assert_classes(['ELCBUS 451'])        
        
class STEP_03(MUWM_3067):
    def _test(self):
        self.date_wrapper('2013-08-23')
        self.assert_classes(['ELCBUS 451'])

class STEP_04(MUWM_3067):
    def _test(self):
        self.date_wrapper('2013-08-24')
        self.assert_classes(['ELCBUS 451', 'TRAIN 101', 'TRAIN 102'])    

class STEP_05(MUWM_3067):
    def _test(self):
        self.date_wrapper('2013-09-24')        
        self.assert_classes(['ELCBUS 451', 'TRAIN 101', 'TRAIN 102'])
        
class STEP_06(MUWM_3067):
    def _test(self):
        self.date_wrapper('2013-09-25')
        self.assert_no_card()


for i in range(1, 7):

    if i < 10:
        s = '0' + str(i)
    else:
        s = str(i)
        
    vars()['test_step_' + s] = create_test_from_test(
        {
            'user' : 'javerage',
            'test_name' : 'step_' + s,
            'test': vars()['STEP_' + s],
        }
    )[0]


    
