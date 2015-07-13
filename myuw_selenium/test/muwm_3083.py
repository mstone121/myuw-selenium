# Test for Summer final grades card
# See JIRA for reference

import os
import sys
import getpass
import unittest

from myuw_selenium.test.card_tests_c import CardTest, create_test_from_test
from myuw_selenium.platforms import LiveServerTestCase
from selenium.common.exceptions import TimeoutException

# Clear DB
os.remove('db.sqlite3')
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'syncdb'])


class MUWM_3083(CardTest):

    def _test(self):
        self.driver.get(self.live_server_url + '/mobile/landing')

        self.thank_you_card()
        self.checklist()
        self.summer_efs()
        self.critical_info()
        self.no_int_res_card()
        self.reload_no_thank_you()

    def thank_you_card(self):
        card = self.getElement("div#ThankYouCard")
        assert card.is_displayed()

        assert card.find_element_by_css_selector("h3").text.strip() == "Payment Received, Thank You"

        divs = card.find_elements_by_css_selector("div.thankyou div")
        assert divs[0].text.strip() == "Thank you for confirming your intention to enroll at the University of Washington for autumn quarter 2014. Your new Student Enrollment and Orientation Fee has been accepted and recorded."
        assert divs[1].text.strip() == "The Office of the Registrar has received payment for the following fees: New Student Enrollment & Orientation Fee"

    def checklist(self):
        card = self.getElement("div#ToRegisterCard")
        assert card.is_displayed()

        bullets = card.find_elements_by_css_selector("div.notice-content span.notice-title")
        assert bullets[0].text.strip() == "Register for Required Online Information Session for International Students"
        assert bullets[1].text.strip() == "Submit Measles Immunization"
        assert bullets[2].text.strip() == "Register for Advising /O Orientation and Class Registration"

    def summer_efs(self):
        card = self.getElement("div#SummerEFSCard")
        assert card.is_displayed()
        
        headings = card.find_elements_by_css_selector("h3")
        assert headings[0].text.strip() == "Review Critical Summer Registration Info"
        assert headings[1].text.strip() == "Consider Early Fall Start"

    def critical_info(self):
        card = self.getElement("div#CriticalInfoCard")
        assert card.is_displayed()

        assert card.find_element_by_css_selector("h3").text.strip() == "Update Critical Information"

        titles = card.find_elements_by_css_selector("span.notice-title")
        assert titles[0].text.strip() == "Set Up UW Email"
        assert titles[1].text.strip() == "Update Student Directory"

    def no_int_res_card(self):
        try:
            card = self.getElement("div#InternationalStuCard")
            assert not card.is_displayed()
        except TimeoutException:
            pass

    def reload_no_thank_you(self):
        self.driver.get(self.live_server_url + '/mobile/landing')
        try:
            card = self.getElement("div#ThankYouCard")
            assert not card.is_displayed()
        except TimeoutException:
            pass


vars()['test_muwm_3083'] = create_test_from_test(
        {
            'user' : 'javerage',
            'test_name' : 'muwm_3083',
            'test': MUWM_3083,
        }
    )[0]


    
