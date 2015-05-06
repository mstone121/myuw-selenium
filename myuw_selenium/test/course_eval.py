# Encoding (for special characters)
# coding=UTF-8

from myuw_selenium.test.course_eval_c import *
from myuw_selenium.test.card_tests_c import create_test_from_test

import datetime


tests = [
    # Javerage
    { 'user':'javerage',
      'date':'2013-06-10', 
      'test_name':'Javerage: Eval shown between a week before finals week and the end of finals week', 
      'test':EvalsShownTest,    
      'courses':['TRAIN 100 A', 'TRAIN 101 A']
  },

    { 'user':'javerage', 
      'date':'2013-06-02',
      'test_name':'Javerage: No eval shown a before a week before finals week',
      'test':EvalsNotShownTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A']
  },

    { 'user':'javerage', 
      'date':'2013-06-15',
      'test_name':'Javerage: No eval shown after finals week',
      'test':EvalsNotShownTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A']
  },
    

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Links are correct (display text and url)',
      'test':LinksTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A'],
      'links':{
          'TRAIN 100 A' : {
              'Rate JAMES AVERAGE STUDENT':'https://uw.iasysdev.org/survey/136617',
          },
          'TRAIN 101 A' : {
              'Rate EIGHT CLASS STUDENT':'https://uw.iasysdev.org/survey/136617',
              'Rate Nancy O\'Brien-Abël':'https://uw.iasysdev.org/survey/1337',
          }
      }
  },           

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Close date is correct', 
      'test':CloseDateTest,    
      'courses':['TRAIN 100 A', 'TRAIN 101 A'],
      'dates': {
          'TRAIN 100 A': datetime.date(2013, 3, 20),
          'TRAIN 101 A': datetime.date(2013, 3, 20)
      }
  },

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Instructor name is correct',
      'test':InstructorNameTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A'],
      'names': {
          'TRAIN 100 A': ['JAMES AVERAGE STUDENT'],
          'TRAIN 101 A': ['EIGHT CLASS STUDENT', 'Nancy O\'Brien-Abël']
      }
  },

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Tab access test',
      'test':TabAccessTest,
      'courses':['TRAIN 101 A', 'TRAIN 100 A']
    },


    # Jbothell
    { 'user':'jbothell',
      'date':'2013-06-10', 
      'test_name':'Jbothell: Eval shown between a week before finals week and the end of finals week', 
      'test':EvalsShownTest,    
      'courses':['BCWRIT 500 A']
  },

    { 'user':'jbothell', 
      'date':'2013-06-02',
      'test_name':'Jbothell: No eval shown a before a week before finals week',
      'test':EvalsNotShownTest,
      'courses':['BCWRIT 500 A']
  },

    { 'user':'jbothell',
      'date':'2013-06-15',
      'test_name':'Jbothell: No eval shown after finals week',
      'test':EvalsNotShownTest,
      'courses':['BCWRIT 500 A']
    },

    { 'user':'jbothell',
      'date':'2013-06-10',
      'test_name':'Jbothell: Links are correct (text and url)',
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
      'test_name':'Jbothell: Close date is correct', 
      'test':CloseDateTest,    
      'courses':['BCWRIT 500 A'],
      'dates': {
          'BCWRIT 500 A': datetime.date(2013, 3, 20),
      }
  },

    { 'user':'jbothell',
      'date':'2013-06-10',
      'test_name':'Jbothell: Instructor name is correct',
      'test':InstructorNameTest,
      'courses':['BCWRIT 500 A'],
      'names': {
          'BCWRIT 500 A': ['Jim Bags'],
      }
  },

    { 'user':'jbothell',
      'date':'2013-06-10',
      'test_name':'Jbothell: Tab access test',
      'test':TabAccessTest,
      'courses':['BCWRIT 500 A']
    },

    # Eight
    { 'user':'eight',
      'date':'2013-06-10', 
      'test_name':'Eight: Eval shown between a week before finals week and the end of finals week', 
      'test':EvalsShownTest,    
      'courses':['T ARTS 110 A']
  },

    { 'user':'eight', 
      'date':'2013-06-02',
      'test_name':'Eight: No eval shown a before a week before finals week',
      'test':EvalsNotShownTest,
      'courses':['T ARTS 110 A']
  },

    { 'user':'eight',
      'date':'2013-06-15',
      'test_name':'Eight: No eval shown after finals week',
      'test':EvalsNotShownTest,
      'courses':['T ARTS 110 A']
    },

    { 'user':'eight',
      'date':'2013-06-10',
      'test_name':'Eight: Links are correct (text and url)',
      'test':LinksTest,
      'courses':['T ARTS 110 A'],
      'links':{
          'T ARTS 110 A' : {
              'Rate EIGHT CLASS STUDENT':'https://uwt.iasystem.org/survey/143301',
          },
      }
  },           

    { 'user':'eight',
      'date':'2013-06-10',
      'test_name':'Eight: Close date is correct', 
      'test':CloseDateTest,    
      'courses':['T ARTS 110 A'],
      'dates': {
          'T ARTS 110 A': datetime.date(2013, 3, 20),
      }
  },

    { 'user':'eight',
      'date':'2013-06-10',
      'test_name':'Eight: Instructor name is correct',
      'test':InstructorNameTest,
      'courses':['T ARTS 110 A'],
      'names': {
          'T ARTS 110 A': ['JAMES INTERNATIONAL STUDENT', 'EIGHT CLASS STUDENT'],
      }
  },

    { 'user':'eight',
      'date':'2013-06-10',
      'test_name':'Eight: Tab access test',
      'test':TabAccessTest,
      'courses':['T ARTS 110 A']
    },
    
]

to_run = [
    EvalsShownTest,
    EvalsNotShownTest,
    LinksTest,
    CloseDateTest,
    InstructorNameTest,
    TabAccessTest,
]
    

for test in tests:
    if (test['test'] in to_run):
        vars()['test_' + test['test_name']] = create_test_from_test(test)[0]

del vars()['test']
del vars()['tests']
