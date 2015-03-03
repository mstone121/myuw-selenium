from myuw_selenium.test.textbook_card_lp_c import *

test_data = [ 
    # Card Hidden
    { 'date':'2013-03-26', 'user':'javerage', 'test_name':'before_grade_submission_deadline', 'test':NoCardTest },
    { 'date':'2013-04-08', 'user':'eight',    'test_name':'after_first_week_of_quarter',      'test':NoCardTest },
    { 'date':'2013-03-22', 'user':'jbothell', 'test_name':'before_end_of_finals_week',        'test':NoCardTest },
    { 'date':'2013-07-26', 'user':'javerage', 'test_name':'summer_b_term_no_card',            'test':NoCardTest },

    # Card Shown
    { 'date':'2013-03-27', 'user':'javerage', 'test_name':'after_grade_submission_deadline', 'test':CardTest },
    { 'date':'2013-04-01', 'user':'eight',    'test_name':'first_week_of_quarter',           'test':CardTest },
    { 'date':'2013-04-07', 'user':'jbothell', 'test_name':'first_week_of_quarter',           'test':CardTest },

    # Correct Course
    {'user':'javerage', 'date':'2013-04-05', 'test_name':'javerage_course', 'courses':['PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A'],                                              'test':CoursesTest },
    {'user':'jbothell', 'date':'2013-04-05', 'test_name':'jbothell_course', 'courses':['BISSEB 259 A', 'BCWRIT 500 A', 'BESS 102 A', 'BESS 102 AB'],                                                           'test':CoursesTest },
    {'user':'jnew',     'date':'2013-04-05', 'test_name':'jnew_course',     'courses':['TRAIN 101 A'],                                                                                                         'test':CoursesTest },
    {'user':'eight',    'date':'2013-04-05', 'test_name':'eight_course',    'courses':['PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A', 'ASL 101 A', 'ROLING 310 A', 'ARCTIC 200 A'], 'test':CoursesTest },

    # Correct Book Counts
    {'user':'javerage', 'date':'2013-04-05', 'test_name':'javerage_book_count', 'courses':{'PHYS 121 A':0 , 'PHYS 121 AC':0, 'PHYS 121 AQ':2, 'TRAIN 100 A':0, 'TRAIN 101 A':0},                                                   'test':BookCountTest },
    {'user':'jbothell', 'date':'2013-04-05', 'test_name':'jbothell_book_count', 'courses':{'BISSEB 259 A':1, 'BCWRIT 500 A':1, 'BESS 102 A':1, 'BESS 102 AB':0},                                                                   'test':BookCountTest },
    {'user':'jnew',     'date':'2013-04-05', 'test_name':'jnew_book_count',     'courses':{'TRAIN 101 A':1},                                                                                                                       'test':BookCountTest },
    {'user':'eight',    'date':'2013-04-05', 'test_name':'eight_book_count',    'courses':{'PHYS 121 A':0, 'PHYS 121 AC':1, 'PHYS 121 AQ':0, 'TRAIN 100 A':0, 'TRAIN 101 A':0, 'ASL 101 A':0, 'ROLING 310 A':0, 'ARCTIC 200 A':1}, 'test':BookCountTest },

    # Correct Course Colors
    {'user':'javerage', 'date':'2013-04-05', 'test_name':'javerage_color', 'courses':['PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A'],                                              'test':CourseColorTest },
    {'user':'jbothell', 'date':'2013-04-05', 'test_name':'jbothell_color', 'courses':['BISSEB 259 A', 'BCWRIT 500 A', 'BESS 102 A', 'BESS 102 AB'],                                                           'test':CourseColorTest },
    {'user':'jnew',     'date':'2013-04-05', 'test_name':'jnew_color',     'courses':['TRAIN 101 A'],                                                                                                         'test':CourseColorTest },
    {'user':'eight',    'date':'2013-04-05', 'test_name':'eight_color',    'courses':['PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A', 'ASL 101 A', 'ROLING 310 A', 'ARCTIC 200 A'], 'test':CourseColorTest },

    # Full Page Textbook Link
    {'user':'javerage', 'date':'2013-04-05', 'test_name':'javerage_full_page', 'test':FullPageLink },

    # No Full Page Textbook Link
    {'user':'javerage', 'date':'2013-10-01', 'test_name':'javerage_no_full_page', 'test':NoFullPageLink }
]

for test in test_data:
    card_tests = create_test_from_test(test)

    index = 1
    for test_class in card_tests:
        vars()['test_' + test['test_name'] + '_' + str(index)] = test_class
        index += 1

del vars()['test_class']

