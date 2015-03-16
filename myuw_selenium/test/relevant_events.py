from myuw_selenium.test.relevant_events_c import *

from myuw_selenium.test.card_tests_c import create_test_from_test


links = [
    { 'See all events from Department of Future Events One calendar.':'http://www.trumba.com/calendar/future_1' },
    { 'Department of Two Events':'http://www.trumba.com/calendar/2_current' },
    { 'Department of Five Events':'http://www.trumba.com/calendar/5_current' },
    { 'Department of Future Events One':'http://www.trumba.com/calendar/future_1' }
]

testcal1_links = {}
testcal1_links.update(links[0])

testcal2_links = {}
testcal2_links.update(links[1])
testcal2_links.update(links[2])
testcal2_links.update(links[3])

testcal2_links_2 = {}
testcal2_links_2.update(links[1])
testcal2_links_2.update(links[2])

messages = [
    """No events in the next 14 days. 1 events from Department of Future Events One in the next 30 days.""",

    """No events in the next 14 days. 8 events from 3 calendars in the next 30 days.
    Department of Future Events One
    Department of Two Events
    Department of Five Events""",

    """See all events from Department of Future Events One calendar.""",

    """See all events from:
    Department of Five Events
    Department of Two Events
    Department of Future Events One"""
]


test_data = [ 
    # Card Hidden
    { 'date':'2013-03-10', 'user':'testcal1', 'test_name':'no_card_cal',    'test':NoCardShownTest },
    { 'date':'2013-03-10', 'user':'javerage', 'test_name':'no_card_no_cal', 'test':NoCardShownTest },

    # Card Shown
    { 'date':'2013-04-21', 'user':'testcal1', 'test_name':'card', 'test':CardShownTest },
    
    # Disclosure Tests
    { 'date':'2013-04-15', 'user':'testcal2', 'test_name':'disclosure',    'test':DisclosureTest },
    { 'date':'2013-04-18', 'user':'testcal2', 'test_name':'no_disclosure', 'test':NoDisclosureTest },

    # Calendar Link Tests
    { 'date':'2013-04-25', 'user':'testcal1', 'test_name':'full_cal_no_disclosure', 'test':LinksTest, 'links':testcal1_links },
    { 'date':'2013-04-18', 'user':'testcal2', 'test_name':'mult_cal_no_disclosure', 'test':LinksTest, 'links':testcal2_links },
    { 'date':'2013-04-15', 'user':'testcal2', 'test_name':'mult_cal_disclosure',    'test':LinksTest, 'links':testcal2_links_2 },
    
    # Message Tests
    { 'date':'2013-04-15', 'user':'testcal1', 'test_name':'no_14_some_30_one_cal',   'test':MessageTest, 'message':messages[0] },
    { 'date':'2013-04-01', 'user':'testcal2', 'test_name':'no_14_some_30_multi_cal', 'test':MessageTest, 'message':messages[1] },
    { 'date':'2013-04-25', 'user':'testcal1', 'test_name':'some_14_one_cal',         'test':MessageTest, 'message':messages[2] },
    { 'date':'2013-04-16', 'user':'testcal2', 'test_name':'some_14_multi_cal',       'test':MessageTest, 'message':messages[3] },

    # Events Tests
    { 'date':'2013-04-16', 'user':'testcal2', 'test_name':'date_order',   'test':EventsTest, 'assert_func':EventsTest.assert_date_order},

    { 'date':'2013-04-15', 'user':'testcal2', 'test_name':'events_count_disc',    'test':EventsTest, 'assert_func':EventsTest.assert_events_count, 'count':7}, # Should have disclosure, see above
    { 'date':'2013-04-18', 'user':'testcal2', 'test_name':'events_count_no_disc', 'test':EventsTest, 'assert_func':EventsTest.assert_events_count, 'count':6}, # Should not have disclosure, see above
    
]

for test in test_data:
    card_tests = create_test_from_test(test)

    index = 1
    for test_class in card_tests:
        vars()['test_' + test['test_name'] + '_' + str(index)] = test_class
        index += 1

del vars()['test_class']

