# Test for Summer B term Future Qtr Card
# See JIRA for reference

import os
import sys
import getpass
import unittest

from myuw_selenium.test.card_tests_c import CardTest, create_test_from_test
from myuw_selenium.platforms import LiveServerTestCase

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


class MUWM_3068(CardTest):

    def date_wrapper(self, date):
        self.date = date
        self.setDate()
        self.driver.get(self.live_server_url + '/mobile/landing')


    def assert_fq_cards_bottom(self):
        cards = self.getElements("div#landing_content > div")
        card_id = cards[-1].get_attribute('id')
        assert card_id == 'FutureQuarterCard1', card_id

    def assert_fq_cards_top(self):
        cards = self.getElements("div#landing_content > div")
        for card in cards:
            if "none" in card.get_attribute('style'):
                cards.remove(card)                

        for i in range(len(cards)):
            card = cards[i]
            if card.get_attribute('id') == 'VisualScheduleCard':
                self.fail()
            elif card.get_attribute('id').startswith('FutureQuarterCard'):
                return
            
        # card_0 = cards[0].get_attribute('id')
        # if cards[0].get_attribute('id') != 'GradeCard':            
        #     assert card_0 == 'FutureQuarterCardA', card_0
        # else:
        #     card_1 = cards[1].get_attribute('id')
        #     assert card_1 == 'FutureQuarterCardA', card_1

    def get_data_identifiers(self):
        fq_cards = self.getElements("div#FutureQuarterCardA div.card")
        fq_cards += self.getElements("div#FutureQuarterCard1 div.card")

        data = []
        for element in fq_cards:
            data.append(str(element.get_attribute('data-identifier')).strip())

        return data

    def assert_ids(self, a_term=True, b_term=True, autumn=True):
        data_ids = self.get_data_identifiers()

        if a_term:
            assert 'Summer 2013 a-term' in data_ids, data_ids

        if b_term:
            assert 'Summer 2013 b-term' in data_ids, data_ids

        if autumn:
            assert 'Autumn 2013' in data_ids, data_ids

    def assert_vs_title(self, title):
        vs_title = self.getElement("div#VisualScheduleCard h3#quarter-info").text.strip()

        assert vs_title == title


# Tests
class STEP_02(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-04-26')
        self.assert_fq_cards_top()
        self.assert_ids()
        
class STEP_03(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-04-27')
        self.assert_fq_cards_top()
        self.assert_ids()

class STEP_04(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-04-28')
        self.assert_fq_cards_bottom()
        self.assert_ids()

class STEP_05(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-06-23')        
        self.assert_fq_cards_bottom()
        self.assert_ids()

class STEP_06(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-06-24')
        self.assert_fq_cards_bottom()
        self.assert_ids(a_term=False)
        self.assert_vs_title("Summer 2013 Courses a-term")

class STEP_07(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-07-17')
        self.assert_fq_cards_bottom()
        self.assert_ids(a_term=False)

class STEP_08(MUWM_3068):
    def _test(self):
        for i in range(18, 25):
            self.date_wrapper('2013-07-' + str(i))
            self.assert_fq_cards_top()
            self.assert_ids(a_term=False)

class STEP_09(MUWM_3068):
    def _test(self):
        for date in ['07-25', '07-30', '08-01', '08-15', '08-26']:
            self.date_wrapper('2013-' + date)
            self.assert_fq_cards_bottom()
            self.assert_ids(a_term=False, b_term=False)

class STEP_10(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-08-27')
        self.assert_fq_cards_bottom()
        self.assert_ids(a_term=False, b_term=False)

class STEP_11(MUWM_3068):
    def _test(self):
        self.date_wrapper('2013-08-28')

        cards = self.getElements("div#landing_content > div")
        ids = []

        for card in cards:
            ids.append(card.get_attribute('id'))

        assert 'FutureQuarterCards1' not in ids
        assert 'FutureQuarterCardsA' not in ids        
            



for i in range(2, 12):

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


    
