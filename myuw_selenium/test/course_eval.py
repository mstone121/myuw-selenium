from myuw_selenium.test.course_eval_c import *
from myuw_selenium.test.card_tests_c import create_test_from_test


tests = [
    { 'user':'javerage', 'test_name':'Eval Shown', 'test':EvalsShownTest,    'courses':['TRAIN 100 A'] },
    { 'user':'javerage', 'test_name':'No Eval'   , 'test':EvalsNotShownTest, 'courses':['PHYS 121 A']  },
    { 'user':'javerage', 'test_name':'Links Test', 'test':LinksTest,         'courses':['TRAIN 100 A'] },
    { 'user':'javerage', 'test_name':'Close Date', 'test':CloseDateTest,     'courses':['TRAIN 100 A'] },
]

for test in tests:
    vars()['test_' + test['test_name']] = create_test_from_test(test)[0]

del vars()['test']
del vars()['tests']
