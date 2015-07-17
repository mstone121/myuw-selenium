# Test for Summer final grades card
# See JIRA for details

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


class MUWM_3085(CardTest):

    def _test(self):
        self.driver.get(self.live_server_url + '/mobile/landing')

        self.thank_you_card()
        self.checklist()
        self.assert_card_not_displayed("div#SummerEFSCard")
        self.assert_card_not_displayed("div#CriticalInfoCard")
        self.assert_card_not_displayed("div#InternationalStuCard")
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
        assert divs[1].text.strip() == "The Office of the Registrar has received payment for the following fees:\nNew Student Enrollment & Orientation Fee", divs[1].text


    def checklist(self):
        card = self.getElement("div#ToRegisterCard")
        assert card.is_displayed()

        assert card.find_element_by_css_selector("h3").text.strip() == "To Register For Classes"

        assert card.find_element_by_css_selector("strong").text.strip() == "Register on Mon, Apr 1 through MyPlan or the registration screen."

        links  = card.find_elements_by_css_selector("ul.card_list a")
        assert links[0].text == "How to register"
        assert links[1].text == "How to choose courses"
        assert links[0].get_attribute('href') == "https://depts.washington.edu/sislearn/registration-resources/"
        assert links[1].get_attribute('href') == "http://www.washington.edu/uaa/advising/academic-planning/choosing-courses/overview/"        

vars()['test_muwm_3085'] = create_test_from_test(
        {
            'user' : 'jbothell',
            'test_name' : 'muwm_3085',
            'test': MUWM_3085,
        }
    )[0]


    
