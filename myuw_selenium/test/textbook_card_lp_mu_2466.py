from myuw_selenium.test.textbook_card_lp_c import *

test_data = [ 
    # --Card show/hide

    # None, 2013 spring: no card Shown
    { 'date':'2013-04-05', 'User':'none', 'test_name': 'no_card_for_user_none', 'test': NoCardTest },

    # Javerage: card show/hide
    # Spring 2013
    { 'date':'2013-03-26', 'User':'javerage', 'test_name':'javerage_spring_pre',   'test':NoCardTest },
    { 'date':'2013-03-27', 'User':'javerage', 'test_name':'javerage_spring_start', 'test':CardTest },
    { 'date':'2013-04-07', 'User':'javerage', 'test_name':'javerage_spring_end',   'test':CardTest },
    { 'date':'2013-04-08', 'User':'javerage', 'test_name':'javerage_spring_post',  'test':NoCardTest },
    # Autumn 2013
    { 'date':'2013-08-27', 'User':'javerage', 'test_name':'javerage_autumn_pre',   'test':NoCardTest },
    { 'date':'2013-08-28', 'User':'javerage', 'test_name':'javerage_autumn_start', 'test':CardTest },
    { 'date':'2013-10-01', 'User':'javerage', 'test_name':'javerage_autumn_end',   'test':CardTest },
    { 'date':'2013-10-02', 'User':'javerage', 'test_name':'javerage_autumn_post',  'test':NoCardTest },
    # Summer A 2013
    { 'date':'2013-06-23', 'User':'javerage', 'test_name':'javerage_summer_pre',   'test':NoCardTest },
    { 'date':'2013-06-24', 'User':'javerage', 'test_name':'javerage_summer_start', 'test':CardTest },
    { 'date':'2013-06-30', 'User':'javerage', 'test_name':'javerage_summer_end',   'test':CardTest },
    { 'date':'2013-07-01', 'User':'javerage', 'test_name':'javerage_summer_post',  'test':NoCardTest },
    # Winter 2013
    { 'date':'2012-12-18', 'User':'javerage', 'test_name':'javerage_winter_pre',   'test':NoCardTest },
    { 'date':'2012-12-19', 'User':'javerage', 'test_name':'javerage_winter_start', 'test':CardTest },
    { 'date':'2013-01-13', 'User':'javerage', 'test_name':'javerage_winter_end',   'test':CardTest },
    { 'date':'2013-01-14', 'User':'javerage', 'test_name':'javerage_winter_post',  'test':NoCardTest },


    # --Eight: course colors
    { 'user':'eight', 'date':'2013-04-05', 'test_name':'eight_colors', 'courses':['PHYS 121 A', 'PHYS 121 AC', 'PHYS 121 AQ', 'TRAIN 100 A', 'TRAIN 101 A', 'ASL 101 A', 'ROLING 310 A', 'ARCTIC 200 A'], 'test':CourseColorTest },


    # --Books:

    # Eight, 2013 spring
    # Single required book
    { 'user':'eight', 'date':'2013-04-05', 'test_name':'eight_single_required', 'course':'ARCTIC 200 A', 'books':1, 'required':1, 'test':CourseTest },
    # No books
    { 'user':'eight', 'date':'2013-04-05', 'test_name':'eight_no_books', 'course':'ASL 101 A', 'books':0, 'required':0, 'test':CourseTest },

    # Javerage, 2013 spring
    # >1 required
    { 'user':'javerage', 'date':'2013-04-05', 'test_name':'javerage_gt_one_required', 'course':'PHYS 121 AQ', 'books':2, 'required':2, 'test':CourseTest },

    # Javerage, 2013 winter
    # 2 books, 1 required
    { 'user':'javerage', 'date':'2013-01-11', 'test_name':'javerage_two_books_one_req', 'course':'EMBA 503 A', 'books':2, 'required':1, 'test':CourseTest },
    # 1 book, not required
    { 'user':'javerage', 'date':'2013-01-11', 'test_name':'javerage_one_books_no_req', 'course':'EMBA 590 A', 'books':1, 'required':0, 'test':CourseTest },


    # --Full textbook page

    # javerage: winter 2013
    { 'user':'javerage', 'date':'2013-01-05', 'test_name':'javerage_winter_full_page', 'test':FullPageLink },
    # javerage: spring 2013
    { 'user':'javerage', 'date':'2013-04-05', 'test_name':'javerage_spring_full_page', 'test':FullPageLink },
    # javerage: summer A 2013
    { 'user':'javerage', 'date':'2013-06-29', 'test_name':'javerage_summer_a_full_page', 'test':FullPageLink },

    # No full page
    # javerage: autumn 2013
    { 'user':'javerage', 'date':'2013-10-01', 'test_name':'javerage_no_full_page', 'test':NoFullPageLink }
]
    
for test in test_data:
    card_tests = create_test_from_test(test)

    index = 1
    for test_class in card_tests:
        vars()['test_' + test['test_name'] + '_' + str(index)] = test_class
        index += 1

del vars()['test_class']
