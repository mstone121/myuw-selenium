# Encoding (for special characters)
# coding=UTF-8

from myuw_selenium.test.course_eval_c import *
from myuw_selenium.test.card_tests_c import create_test_from_test

import datetime

temp_name = "BILL AVERAGE TEACHER"
#temp_name = "Nancy O\'Brien-Abël"


tests_javerage_spring = [
    { 'user':'javerage',
      'date':'2013-06-10', 
      'test_name':'Javerage: Eval appear on card', 
      'test':EvalsShownTest,    
      'courses':['TRAIN 100 A', 'TRAIN 101 A', 'PHYS 121 AQ', 'PHYS 121 AQ']
    },

    # { 'user':'javerage', 
    #   'date':'2013-05-31',
    #   'test_name':'Javerage: No evals shown before a week before last day of instruction',
    #   'test':EvalsNotShownTest,
    #   'courses':['TRAIN 100 A', 'TRAIN 101 A', 'PHYS 121 AQ']
    # },

    # { 'user':'javerage', 
    #   'date':'2013-06-19',
    #   'test_name':'Javerage: No eval after shown grade submission deadline',
    #   'test':EvalsNotShownTest,
    #   'courses':['TRAIN 100 A', 'TRAIN 101 A', 'PHYS 121 AQ']
    # },
    

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Links are correct (display text and url)',
      'test':LinksTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A', 'PHYS 121 AQ'],
      'links':{
          'TRAIN 100 A' : {
              'JAMES AVERAGE STUDENT':'https://uw.iasysdev.org/survey/136617',
              temp_name:'https://uw.iasysdev.org/survey/1337',
          },
          'TRAIN 101 A' : {
              'EIGHT CLASS STUDENT':'https://uw.iasysdev.org/survey/136617',
          },
          'PHYS 121 AQ' : {
              'JAMES AVERAGE STUDENT':'https://uw.iasysdev.org/survey/136617',
          }
      }
    },           

    { 'user':'javerage',
      'date':'2013-06-10',
      'system_time' : ( 2013, 4, 5, 7, 0, 0, 0 ),
      'test_name':'Javerage: Close date is correct', 
      'test':CloseDateTest,    
      'courses':['TRAIN 100 A', 'TRAIN 101 A', 'PHYS 121 AQ'],
      'dates': {
          'TRAIN 100 A': [datetime.date(2013, 4, 5), datetime.date(2013, 5, 13)],
          'TRAIN 101 A': [datetime.date(2013, 4, 5), datetime.date(2013, 5, 13)],
          'PHYS 121 AQ': [datetime.date(2013, 4, 5), datetime.date(2013, 5, 13)]
      }
    },

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Instructor name is correct',
      'test':InstructorNameTest,
      'courses':['TRAIN 100 A', 'TRAIN 101 A', 'PHYS 121 AQ'],
      'names': {
          'TRAIN 100 A': ['JAMES AVERAGE STUDENT', temp_name],
          'TRAIN 101 A': ['EIGHT CLASS STUDENT'],
          'PHYS 121 AQ': ['JAMES AVERAGE STUDENT']
      }
    },

    { 'user':'javerage',
      'date':'2013-06-10',
      'test_name':'Javerage: Tab access test',
      'test':TabAccessTest,
      'courses':['TRAIN 101 A', 'PHYS 121 AQ', 'TRAIN 100 A']
    },
]

tests_javerage_summer_a = [
    { 'user':'javerage',
      'date':'2013-07-26', 
      'test_name':'Javerage (Summer A-term): Eval appears on card', 
      'test':EvalsShownTest,    
      'courses':['ELCBUS 451 A']
    },

    { 'user':'javerage', 
      'date':'2013-07-23',
      'test_name':'Javerage (Summer A-term): No eval shown a before open date',
      'test':EvalsNotShownTest,
      'courses':['ELCBUS 451 A']
    },

    { 'user':'javerage', 
      'date':'2013-07-30',
      'test_name':'Javerage (Summer A-term): No eval shown after close date',
      'test':EvalsNotShownTest,
      'courses':['ELCBUS 451 A',]
    },
    

    { 'user':'javerage',
      'date':'2013-07-26',
      'test_name':'Javerage (Summer A-term): Links are correct (display text and url)',
      'test':LinksTest,
      'courses':['ELCBUS 451 A'],
      'links':{
          'ELCBUS 451 A' : {
              'JAMES AVERAGE STUDENT':'https://uw.iasystem.org/survey/130808',
          }
      }
    },           

    { 'user':'javerage',
      'date':'2013-07-26',
      'system_time' : ( 2013, 7, 24, 7, 0, 0, 0 ),
      'test_name':'Javerage (Summer A-term): Close date is correct', 
      'test':CloseDateTest,    
      'courses':['ELCBUS 451 A'],
      'dates': {
          'ELCBUS 451 A': [datetime.date(2013, 7, 24), datetime.date(2013, 7, 29)]
      }
    },

    { 'user':'javerage',
      'date':'2013-07-26',
      'test_name':'Javerage (Summer A-term): Instructor name is correct',
      'test':InstructorNameTest,
      'courses':['ELCBUS 451 A'],
      'names': {
          'ELCBUS 451 A': ['JAMES AVERAGE STUDENT']
      }
    },

    { 'user':'javerage',
      'date':'2013-07-26',
      'test_name':'Javerage (Summer A-term): Tab access test',
      'test':TabAccessTest,
      'courses':['ELCBUS 451 A']
    },
]

tests_javerage_summer_b = [
    { 'user':'javerage',
      'date':'2013-08-25', 
      'test_name':'Javerage (Summer B-term): Eval appears on card', 
      'test':EvalsShownTest,    
      'courses':['TRAIN 102 A']
    },

    { 'user':'javerage', 
      'date':'2013-08-22',
      'test_name':'Javerage (Summer B-term): No eval shown before open date',
      'test':EvalsNotShownTest,
      'courses':['TRAIN 102 A']
    },

    { 'user':'javerage', 
      'date':'2013-08-28',
      'test_name':'Javerage (Summer B-term): No eval shown after quarter switch',
      'test':EvalsNotShownTest,
      'courses':['TRAIN 102 A']
    },
    

    { 'user':'javerage',
      'date':'2013-08-25',
      'test_name':'Javerage (Summer B-term): Links are correct (display text and url)',
      'test':LinksTest,
      'courses':['TRAIN 102 A'],
      'links':{
          'TRAIN 102 A' : {
              'TRAIN 102 A':'https://uw.iasystem.org/survey/130810',
          },
      }
    },           

    { 'user':'javerage',
      'date':'2013-08-25',
      'system_time' : ( 2013, 8, 27, 7, 0, 0, 0 ),
      'test_name':'Javerage (Summer B-term): Close date is correct', 
      'test':CloseDateTest,    
      'courses':['TRAIN 102 A'],
      'dates': {
          'TRAIN 102 A': [datetime.date(2013, 8, 23), datetime.date(2013, 8, 29)]
      }
    },

    { 'user':'javerage',
      'date':'2013-08-25',
      'test_name':'Javerage (Summer B-term): Instructor name is correct',
      'test':InstructorNameTest,
      'courses':['TRAIN 102 A'],
      'names': {
          'TRAIN 102 A': ['EIGHT CLASS STUDENT'],
      }
    },

    { 'user':'javerage',
      'date':'2013-08-25',
      'test_name':'Javerage (Summer B-term): Tab access test',
      'test':TabAccessTest,
      'courses':['TRAIN 102 A']
    },
]

tests_jbothell = [
    { 'user':'jbothell',
      'date':'2013-06-10', 
      'test_name':'Jbothell: Eval appears on card', 
      'test':EvalsShownTest,    
      'courses':['BCWRIT 500 A']
    },

    { 'user':'jbothell', 
      'date':'2013-05-31',
      'test_name':'Jbothell: No eval shown a before a week before last day of instruction',
      'test':EvalsNotShownTest,
      'courses':['BCWRIT 500 A']
    },

    { 'user':'jbothell',
      'date':'2013-06-19',
      'test_name':'Jbothell: No eval shown grade submission deadline',
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
      'system_time' : ( 2013, 5, 12, 7, 0, 0, 0 ),
      'test_name':'Jbothell: Close date is correct', 
      'test':CloseDateTest,    
      'courses':['BCWRIT 500 A'],
      'dates': {
          'BCWRIT 500 A': [datetime.date(2013, 4, 5), datetime.date(2013, 5, 13)]
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
]

tests_eight = [
    { 'user':'eight',
      'date':'2013-06-10', 
      'test_name':'Eight: Eval appears on card', 
      'test':EvalsShownTest,    
      'courses':['T ARTS 110 A']
    },

    { 'user':'eight', 
      'date':'2013-05-31',
      'test_name':'Eight: No eval shown a before a week before last day of instruction',
      'test':EvalsNotShownTest,
      'courses':['T ARTS 110 A']
    },

    { 'user':'eight',
      'date':'2013-06-19',
      'test_name':'Eight: No eval shown after grade submission deadline',
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
              'EIGHT CLASS STUDENT':'https://uwt.iasystem.org/survey/143301',
          },
      }
    },           

    { 'user':'eight',
      'date':'2013-06-10',
      'system_time' : ( 2013, 6, 12, 7, 0, 0, 0 ),
      'test_name':'Eight: Close date is correct', 
      'test':CloseDateTest,    
      'courses':['T ARTS 110 A'],
      'dates': {
          'T ARTS 110 A': [datetime.date(2013, 6, 6), datetime.date(2013, 6, 13)]
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

netids = [
    tests_javerage_spring,
    tests_javerage_summer_a,
    tests_javerage_summer_b,
#    tests_jbothell,
    tests_eight,
]

to_run = [
    EvalsShownTest,
    EvalsNotShownTest,
    LinksTest,
#    CloseDateTest,
    InstructorNameTest,
#    TabAccessTest,
]
    
for tests in netids:
    for test in tests:
        if (test['test'] in to_run):
            vars()['test_' + test['test_name']] = create_test_from_test(test)[0]

del vars()['test']
del vars()['tests']
