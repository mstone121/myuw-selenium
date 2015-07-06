# Test for Summer B term Future Qtr Card
# See JIRA for reference

import os
import getpass
import unittest

from myuw_selenium.tests.card_tests_c import CardTest


username = None
password = None

try:
    username = os.environ['MYUW_USERNAME']
except KeyError:
    username = input("Username: ")

try:
    password = os.environ['MYUW_PASSWORD']
except KeyError:
    password = getpass.getpass()

os.remove('db.sqlite3')
    
from django.core.management import execute_from_command_line


execute_from_command_line(['manage.py', 'syncdb'])


class MUWM_3068(CardTest):

    def date_wrapper(self, date):
        self.date = date
        self.setDate()
        self.driver.get(self.live_server_url + '/mobile/landing')


    def step_2(self):
        self.date_wrapper('2013-04-26')

        cards = self.getElements("div#landing_content > div")

        assert cards[0].get_attribute('id') == 'FutureQuarterCardA'
        
        fq_cards = self.getElements("div#FutureQuarterCardA div.card")

        assert fq_cards[0].get_attribute('data-identifier') == 'Summer 2013 a-term'
        assert fq_cards[1].get_attribute('data-identifier') == 'Summer 2013 b-term'
        assert fq_cards[2].get_attribute('data-identifier') == 'Autumn 2013'

    def step_3(self):
        self.date_wrapper('2013-04-27')

        cards = self.getElements("div#landing_content > div")

        assert cards[0].get_attribute('id') == 'FutureQuarterCardA'

    def step_4(self):
        self.date_wrapper('2013-04-28')

        cards = self.getElements("div#landing_content > div")

        assert cards[

    
