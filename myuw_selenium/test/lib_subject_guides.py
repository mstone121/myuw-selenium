from myuw_selenium.test.lib_subject_guides_c import *
from myuw_selenium.test.card_tests_c import create_test_from_test


links = {
    'javerage' : {
        'PHYS 121 A' : 'http://guides.lib.washington.edu/physics_astronomy',
        'PHYS 121 AC': 'http://guides.lib.washington.edu/physics_astronomy',
        'PHYS 121 AQ': 'http://guides.lib.washington.edu/physics_astronomy',
        'TRAIN 100 A': 'http://www.lib.washington.edu/subject/',
        'TRAIN 101 A': 'http://www.lib.washington.edu/subject/',
    },

    'jnew' : {
        'TRAIN 101 A' : 'http://www.lib.washington.edu/subject/',
    },

    'eight' : {
        'PHYS 121 A' : 'http://guides.lib.washington.edu/physics_astronomy',
        'PHYS 121 AC': 'http://guides.lib.washington.edu/physics_astronomy',
        'PHYS 121 AQ': 'http://guides.lib.washington.edu/physics_astronomy',
    },
}

test_data = [ 
    # Link Tests
    { 'user':'javerage', 'test_name':'javerage_links', 'test':LinkTest, 'links': links['javerage'] },
    { 'user':'jnew',     'test_name':'jnew_links',     'test':LinkTest, 'links': links['jnew']     },
    { 'user':'eight',    'test_name':'eight_links',    'test':LinkTest, 'links': links['eight']    },

    # Navigate Tests
    { 'user':'javerage', 'test_name':'javerage_navigate', 'test':NavigateTest, 'links': links['javerage'] },
    { 'user':'jnew',     'test_name':'jnew_navigate',     'test':NavigateTest, 'links': links['jnew']     },
    { 'user':'eight',    'test_name':'eight_navigate',    'test':NavigateTest, 'links': links['eight']    },

]


for test in test_data:
    card_tests = create_test_from_test(test)

    index = 1
    for test_class in card_tests:
        vars()['test_' + test['test_name'] + '_' + str(index)] = test_class
        index += 1

del vars()['test_class']

