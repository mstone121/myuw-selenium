from myuw_selenium.platforms import on_platforms, SeleniumLiveServerTestCase

@on_platforms()
class CardOrderTest(SeleniumLiveServerTestCase):
    """
    Tests the order and display of cards at various times in the quarter.
    """

    def test_card_order(self):
        from time import sleep

        dates = [
            { 'date': "2013-04-07", 'user': 'none' }, # Needs to be none to have no registrations, otherwise RegStatusCard is hidden
            { 'date': "2013-04-08", 'user': 'none' }, # Needs to be none to have no registrations, otherwise RegStatusCard is hidden
            { 'date': "2013-04-21", 'user': 'none' }, # Needs to be none to have no registrations, otherwise RegStatusCard is hidden
            { 'date': "2013-04-22", 'user': 'none' }, # Needs to be none to have no registrations, otherwise RegStatusCard is hidden
            { 'date': "2013-04-25", 'user': 'none' }, # Needs to be none to have no registrations, otherwise RegStatusCard is hidden
            { 'date': "2013-04-26", 'user': 'none' }, # Needs to be none to have no registrations, otherwise RegStatusCard is hidden
            { 'date': "2013-04-29", 'user': 'none' }, # Needs to be none to have no registrations, otherwise RegStatusCard is hidden
            { 'date': "2013-05-30", 'user': 'none' }, # Same!
            { 'date': "2013-03-10", 'user': 'none' }, # Need to go back in time, otherwise autumn makes this break - Same though
            { 'date': "2013-03-11", 'user': 'none' }, # Need to go back in time, otherwise autumn makes this break
            { 'date': "2013-04-01", 'user': 'javerage' },
            { 'date': "2013-04-02", 'user': 'javerage' }, # Same!
            { 'date': "2013-04-03", 'user': 'javerage' }, # Future quarter moves to position 1
            { 'date': "2013-04-25", 'user': 'javerage' }, # Same!

            { 'date': "2013-06-07", 'user': 'javerage' }, # Same (ish)!
            { 'date': "2013-06-08", 'user': 'javerage' },
            { 'date': "2013-06-13", 'user': 'javerage' }, # Same!
            { 'date': "2013-06-15", 'user': 'javerage' },
            { 'date': "2013-08-27", 'user': 'javerage' }, # Need to go to the future - spring's grade submission deadline is always today actual.
            { 'date': "2013-08-28", 'user': 'javerage' }, # Need to go to the future - spring's grade submission deadline is always today actual.
            { 'date': "2013-09-24", 'user': 'javerage' }, # Same
            { 'date': "2013-09-25", 'user': 'javerage' },
        ]

        correct_cards = [
            [u'VisualScheduleCard', u'CourseCard', u'TuitionCard'], #  'date': "2013-04-07", 'user': 'none'
            [u'SummerRegStatusCardA', u'VisualScheduleCard', u'CourseCard', u'TuitionCard'],
            [u'SummerRegStatusCardA', u'VisualScheduleCard', u'CourseCard', u'TuitionCard'],
            [u'VisualScheduleCard', u'CourseCard', u'TuitionCard', u'SummerRegStatusCard1'],
            [u'VisualScheduleCard', u'CourseCard', u'TuitionCard', u'SummerRegStatusCard1'],
            [u'RegStatusCard', u'VisualScheduleCard', u'CourseCard', u'TuitionCard', u'SummerRegStatusCard1'],
            [u'RegStatusCard', u'VisualScheduleCard', u'CourseCard', u'TuitionCard', u'SummerRegStatusCard1'], #  'date': "2013-04-29", 'user': 'none'
            [u'RegStatusCard', u'VisualScheduleCard', u'CourseCard', u'TuitionCard'],
            [u'RegStatusCard', u'VisualScheduleCard', u'CourseCard', u'TuitionCard'],
            [u'VisualScheduleCard', u'CourseCard', u'TuitionCard'],

            [u'FutureQuarterCardA', u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard'],
            [u'FutureQuarterCardA', u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard'],
            [u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard', 'FutureQuarterCard1'],
            [u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard', 'FutureQuarterCard1'],

            [u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard', 'FutureQuarterCard1'],
            [u'GradeCard', u'FinalExamCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard', 'FutureQuarterCard1'],
            [u'GradeCard', u'FinalExamCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard', 'FutureQuarterCard1'],
            [u'GradeCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard', 'FutureQuarterCard1'],
            [u'GradeCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard', u'AcademicCard', 'FutureQuarterCard1'],
            [u'GradeCard', u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard'],
            [u'GradeCard', u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard'],
            [u'VisualScheduleCard', u'CourseCard', u'HFSCard', u'TuitionCard', u'LibraryCard'],
        ]

        index = 0
        for val in dates:
            date = val["date"]
            user = val["user"]

            self.driver.get(self.live_server_url + '/users/')
            element = self.driver.find_element_by_xpath("//input[@name='override_as']")
            element.clear()
            element.send_keys(user)
            element.submit()

            self.driver.get(self.live_server_url + '/mobile/admin/dates/')
            element = self.driver.find_element_by_xpath("//input[@name='date']")
            element.clear()
            element.send_keys(date)
            element.submit()
            self.driver.get(self.live_server_url + '/mobile/landing/')
            # XXX - this is lame.  need to add something to wait on here instead
            sleep(2)
            title = self.driver.title
            self.assertEquals(self.driver.title, "MyUW Mobile Home")

            divs = self.driver.find_elements_by_css_selector("#landing_content > div")

            displayed = []
            for div in divs:
                if div.get_attribute("style") != "display: none;":
                    displayed.append(div.get_attribute("id"))

            cards = correct_cards[index]

            self.assertEquals(len(cards), len(displayed), "Set %s has right number of cards (%s, %s)" % (index, ",".join(cards), ",".join(displayed)))

            for i in range(0, len(cards)-1):
                self.assertEquals(cards[i], displayed[i], "Set %s has correct card %s" % (index, i))

            index = index + 1