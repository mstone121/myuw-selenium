from myuw_selenium.test.course_eval_c import *
from myuw_selenium.test.card_tests_c import create_test_from_test

import datetime


tests = [
    # Javerage
    { 'user':'javerage',
      'date':'2013-06-10', 
      'test_name':'Javerage: Eval Shown', 
      'test':EvalsShownTest,    
      'courses':['TRAIN 100 A', 'TRAIN 101 A']
  },

    { 'user':'javerage', 
      'date':'2013-05-01',
      'test_name':'Javerage: No Eval',
      'test':EvalsNotShownTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A']
  },

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Links Test',
      'test':LinksTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A'],
      'links':{
          'TRAIN 100 A' : {
              'Rate JAMES AVERAGE STUDENT':'https://uw.iasysdev.org/survey/136617',
          },
          'TRAIN 101 A' : {
              'Rate EIGHT CLASS STUDENT':'https://uw.iasysdev.org/survey/136617',
              'Rate BILL AVERAGE TEACHER':'https://uw.iasysdev.org/survey/1337',
          }
      }
  },           

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Close Date', 
      'test':CloseDateTest,    
      'courses':['TRAIN 100 A', 'TRAIN 101 A'],
      'dates': {
          'TRAIN 100 A': datetime.date(2013, 3, 20),
          'TRAIN 101 A': datetime.date(2013, 3, 20)
      }
  },

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Instructor Name',
      'test':InstructorNameTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A'],
      'names': {
          'TRAIN 100 A': ['JAMES AVERAGE STUDENT'],
          'TRAIN 101 A': ['EIGHT CLASS STUDENT', 'BILL AVERAGE TEACHER']
      }
  },

    # Jbothell
    { 'user':'jbothell',
      'date':'2013-06-10', 
      'test_name':'Jbothell: Eval Shown', 
      'test':EvalsShownTest,    
      'courses':['BCWRIT 500 A']
  },

    { 'user':'jbothell', 
      'date':'2013-05-01',
      'test_name':'Jbothell: No Eval',
      'test':EvalsNotShownTest,
      'courses':['BCWRIT 500 A']
  },

    { 'user':'jbothell',
      'date':'2013-06-10',
      'test_name':'Jbothell: Links Test',
      'test':LinksTest,
      'courses':['BCWRIT 500 A'],
      'links':{
          'BCWRIT 500 A' : {
              'Rate Jim Bags':'https://uw.iasysdev.org/survey/136617',
          },
      }
  },           

    { 'user':'jbothell',
      'date':'2013-06-10',
      'test_name':'Jbothell: Close Date', 
      'test':CloseDateTest,    
      'courses':['BCWRIT 500 A'],
      'dates': {
          'BCWRIT 500 A': datetime.date(2013, 3, 20),
      }
  },

    { 'user':'jbothell',
      'date':'2013-06-10',
      'test_name':'Jbothell: Instructor Name',
      'test':InstructorNameTest,
      'courses':['BCWRIT 500 A'],
      'names': {
          'BCWRIT 500 A': ['Jim Bags'],
      }
  },

]

for test in tests:
    vars()['test_' + test['test_name']] = create_test_from_test(test)[0]

del vars()['test']
del vars()['tests']
