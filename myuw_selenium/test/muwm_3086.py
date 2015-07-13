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


class MUWM_3086(CardTest):

    def _test(self):
        self.driver.get(self.live_server_url + '/mobile/landing')

        self.assert_card_not_displayed("div#ThankYouCard")
        self.checklist()
        self.summer_efs()
        self.critical_info()
        self.int_stu_res()
        self.driver.get(self.live_server_url + '/mobile/landing')
        self.assert_card_not_displayed("div#ThankYouCard")

    def assert_card_not_displayed(self, selector):
        try:
            assert not self.getElement(selector).is_displayed()
        except TimeoutException:
            pass

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

        bullets = card.find_elements_by_css_selector("div.notice-content span:first-of-type")
        assert bullets[0].text.strip() == "Attend Advising & Orientation and Class Registration"
        assert bullets[1].text.strip() == "You have completed the International Student Services Online Information Session."
        assert bullets[2].text.strip() == "Your Measles Immunization Form has been received and processed."
        assert bullets[3].text.strip() == "You have registered for an Advising & Orientation Session."

    def summer_efs(self):
        card = self.getElement("div#SummerEFSCard")
        assert card.is_displayed()
        
        assert card.find_element_by_css_selector("h3").text.strip() == "Consider Early Fall Start"
        assert card.find_element_by_css_selector("div.notice-content").text.strip() == "Early Fall Start is a single 5-credit intensive course held over four weeks before autumn quarter begins. Benefit from a small class size, an early introduction to college life, and a lighter course load during autumn quarter. The language courses may be particularly helpful to international students! Learn more about Early Fall Start and register."

    def critical_info(self):
        card = self.getElement("div#CriticalInfoCard")
        assert card.is_displayed()

        assert card.find_element_by_css_selector("h3").text.strip() == "Update Critical Information"

        titles = card.find_elements_by_css_selector("span.notice-title")
        assert titles[0].text.strip() == "Set Up UW Email"
        assert titles[1].text.strip() == "Update Student Directory"
        assert titles[2].text.strip() == "Non-Resident Classification"

    def int_stu_res(self):
        card = self.getElement("div#InternationalStuCard")
        assert card.is_displayed()

        assert card.find_element_by_css_selector("h3").text.strip() == "International Student Resources"
        assert card.find_element_by_css_selector("div.notice-content").text.strip() == "The Foundation for International Understanding Through Students (FIUTS) welcomes you to the University of Washington! Visit the FIUTS website for information about international Student Orientation and the wide variety of services for international students."


vars()['test_muwm_3086'] = create_test_from_test(
        {
            'user' : 'jinter',
            'test_name' : 'muwm_3086',
            'test': MUWM_3086,
        }
    )[0]


    
