#!/usr/bin/python 

import time
from selenium.webdriver.common.keys import Keys
from myuw_selenium.test.myuw_user import testUser, testUserDate
from myuw_selenium.test.musettings import *
from myuw_selenium.test.mudata import *
from myuw_selenium.test.resourcelinks import resLinks
from myuw_selenium.test.records import records
from myuw_selenium.test.academic_card import academic_card_values
from myuw_selenium.test.grade_card import grade_card_values
import selenium
from myuw_selenium.platforms import on_platforms, SeleniumLiveServerTestCase


# User scenario class
# Each user scenario should subclass this, 
# and override the postsetup method

# Tests DON'T subclass this. 
# Rather, they subclass one of the classes that subclasses this one.
# Scroll down near the bottom
class myuw_base_scenario():

    def setUp(self):
        # We still want to call the original setUp since it gives us the driver and stuff
        SeleniumLiveServerTestCase.setUp(self)
        self.setUpExtra()

    # Do our modifications to the test 
    def setUpExtra(self):

        # Default date
        self.dateStr = '2013-04-15'
        self.dateSet = False

        # Get longer messages out of the unit test frameworks
        self.longMessage = True

        # Maximize window
        self.driver.maximize_window()

        # Remove size limit from diffs, useful for 
        # seeing issues with resource pages
        self.maxDiff = None

        # Not really used any more. Used to log in with netid for live or eval data tests. 
        self.usenetid = False

        # The postsetup method is where
        # individual user test classes should
        # define their user and settings
        self.postsetup()

        if not(self.dateSet):
            self.setDate(self.dateStr)
        # Weblogin if necessary
        if self.usenetid:
            self.netidlogin()
        
        # Override if necessary
        if self.username:
            self.chguser(self.username)
        
        # Browse landing, most tests expect to be there when they begin
        self.browse_landing()

    # This is the function that should be overridden in
    # individual user scenarios. 
    # Each US needs to give a user object and a username
    # This is provided as a dummy for legacy reasons. 
    def postsetup(self):
        self.user = testUser(self.driver, self)
        self.username = ''

    # Function to override the username
    # Uses self.user.admin as the url since this might vary
    def chguser(self, username):
        driver = self.driver
        driver.get(self.user.admin)
        time.sleep(.5)
        namebox = driver.find_element_by_name('override_as')
        namebox.send_keys(username + Keys.RETURN)
        time.sleep(.5)

    # Function to navigate to landing page
    def browse_landing(self, username = None):
        driver = self.driver
        driver.get(self.user.landing)
        time.sleep(2.5)
        self.assertIn('MyUW', driver.title)
        self.assertIn('Mobile', driver.title)
        pagetext = driver.find_element_by_tag_name('body').text
        self.assertNotIn('CSRF', pagetext, 'CSRF Verification Failed')

    # Function to browse a resources page
    # respath is the part of the URL after
    # /resource/
    def browse_resources(self, respath):
        d = self.driver
        d.get(self.user.res % respath)
        time.sleep(1.5)

    # Override the date using the new date admin page
    # New date is stored in self.dateStr
    def setDate(self, date):
        d = self.driver
        d.get(self.user.dates)
        time.sleep(.5)
        e = d.find_element_by_xpath('//input[@name="date"]')
        e.send_keys(date + '\n')
        time.sleep(.5)
        self.dateStr = date
        self.dateSet = True

    # End of set up, beginning of actual testing functions

    # Check the card order
    # This is always the same
    # All cards are present in the DOM, but are shown/hidden as needed
    # For example, with the Future Quater Card, it will appear either
    # near the top or at the bottom depending on the date
    def check_card_order(self):
        expected = (
            'FinalExamCard',
            'GradeCard',
            'FutureQuarterCardA',
            'RegStatusCard',
            'VisualScheduleCard',
            'CourseCard',
            'HFSCard',
            'TuitionCard',
            'LibraryCard',
            'AcademicCard',
            'FutureQuarterCard1'
        )

        # All cards fit this xpath
        el = self.driver.find_elements_by_xpath('//div[@id="landing_content"]/div')
        
        for i in range(len(el)):
            e = el[i]
            actualName = e.get_attribute('id')
            expectedName = expected[i]
            self.assertEqual(expectedName, actualName)

    # Checks to make sure notice counts are correct
    # Known issue: Does not check for a lack of notices on users
    # who are not supposed to have any.
    def check_notices_count(self):
        if self.user.critical:
            try:
                e = self.driver.find_element_by_class_name('notice-information')
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Could not find notice bar')
            numCritical = int(e.text.split()[0])
            self.assertEqual(numCritical, self.critical, 'Incorrect number of critical notices on notice bar')

    def check_unread_notices_count(self):
        if self.user.unread:
            try:
                e = self.driver.find_element_by_xpath('//div[@class="notice-unread badge"]')
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Could not find unread notices count')
            numUnread = int(e.text.split()[0])
            self.assertEqual(numUnread, self.user.unread, 'Incorrect number of unread notices on notice bar')

    # Checks to make sure the user has the correct email link
    # Checks for lack of link for users who are not supposed to have it
    def check_email_link(self):
        if self.user.email:
            try:
                link = self.driver.find_element_by_xpath('//div[@id="uwemail"]/a')
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Could not find email link when one was expected')
            self.assertEqual(link.text, self.user.email.text)
            self.assertEqual(link.get_attribute('href'), self.user.email.url)
            self.assertEqual(link.get_attribute('target'), '_blank')
        else:
            try:
                link = self.driver.find_element_by_xpath('//div[@id="uwemail"]/a')
                self.fail('Found email link for a user with no email')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            
    # Checks for presense of registration card, and correct links
    # on the card (this part is broken ATM)
    # You can either specify the reg card title as a string, as a list of reg card titles, 
    # or the legacy 'True' value. 
    def check_reg_card(self):
        if self.user.regcard:
            if type(self.user.regcard) == str:
                regcard = [self.user.regcard]
            elif self.user.regcard == True:
                regcard = ['Registration: Summer 2013']
            else:
                regcard = self.user.regcard

            # Get list of reg cards
            el = self.driver.find_elements_by_xpath('//div[@data-name="RegistrationCard"]')
            if len(el) != len(regcard):
                self.fail('Found %s reg cards when %s were expected' %(len(el), len(regcard)))
            
            for i in range(len(el)):
                e = el[i]
                card = regcard[i]
                title = e.find_element_by_tag_name('h3').text
                self.assertEqual(title, card)

        # If the user is not supposed to have a reg card (self.user.regcard bools to false), 
        # make sure there isn't one present. 
        else:
            el = self.driver.find_elements_by_xpath('//div[@data-name="RegistrationCard"]')
            if len(el) > 0:
                self.fail('Found reg card(s) when none were expected')
            # Broken right now because of show more button
            # TODO: fix
            #if self.reglinks:
            #    links = e.find_elements_by_xpath('./div/div/ul[@class="reg-resources-list"]//a')
            #    for i in range(0, len(self.reglinks)):
            #        self.assertEqual(self.reglinks[i].text, links[i].text, 'Registration card link had the wrong text')
            #        self.assertEqual(self.reglinks[i].url, links[i].get_attribute('href'), 'Registration card link had the wrong URL')

        

    # Checks to make sure course cards are as expected
    def check_schedule(self):

        # Puts found course names in a list
        # Makes sure this list equals the expected values
        if self.user.schedule:
            courseCards = []
            cards = self.driver.find_elements_by_xpath('//div[@id="CourseCard"]//div[@class="card"]')
                
            for card in cards:
                try:
                    courseName = card.find_element_by_class_name('courseIDtitle').text
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find course title on course card')
                courseCards.append(courseName)
            courseCards.sort()
            expectedCourses = list(self.user.courses)
            expectedCourses.sort()
            self.assertEqual(courseCards, expectedCourses)

    # Make sure nothing unexpected appears on the vis sched
    def check_visual_schedule(self):
        if self.user.vSchedule:
            try:
                vsched = self.driver.find_element_by_class_name('visual-schedule')
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Could not find visual schedule when one was expected')
            for course in vsched.find_elements_by_xpath('.//div[@class="visual-course"]'):
                courseTitle = course.find_element_by_tag_name('div').text
                self.assertIn(courseTitle, self.user.vcourses, 'Visual schedule did not have the correct courses')

    # Checks to make sure we have the right husky card balances in the HFS card
    def check_HFS(self):
        if self.user.HFS:
            huskycards = self.driver.find_elements_by_xpath('//div[@id="HFSCard"]//span[@class="card-badge-label"]')
            hfsnames_expected = []
            for i in self.user.HFS:
                hfsnames_expected.append(HFScards[i])
            hfsnames_actual = []
            for e in huskycards:
                hfsnames_actual.append(e.text)
            self.assertEqual(hfsnames_actual, hfsnames_expected, 'HFS card contained the wrong husky cards')

    # Checks the library card for the correct number of holds and
    # checked out items
    def check_library(self):
        if self.user.library:
            try:
                libcard = self.driver.find_element_by_id('LibraryCard')
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Could not find library card when one was expected')

            # Check 'n requested item(s) ready'
            if self.user.libraryholds:
                # The format of this thing keeps changing
                try:
                    holdText = libcard.find_element_by_class_name('card-noncritical-alert').text
                except selenium.common.exceptions.NoSuchElementException: 
                    self.fail('Could not find library holds when it was expected')
                holdParts = holdText.split('\n')[1].split()
                if holdParts[2] == 'items':
                    holdParts[2] = 'item'
                self.assertEqual(holdParts[1:], ['requested', 'item', 'ready'], '"Requested items" text was not correct')
                try:
                    self.assertEqual(int(holdParts[0]), self.user.libraryholds, 'Number of library holds was incorrect')
                except ValueError:
                    self.fail('Wrong format on library card for requested items ready. May not actually be a failure.')

            # User has library items checked out
            if self.user.libraryout:
                try:
                    outText = libcard.find_element_by_xpath('./div/div/div[contains(., "Items out")]').text
                except selenium.common.exceptions.NoSuchElementException: 
                    self.fail('Could not find library items checked out')
                outParts = outText.splitlines()
                self.assertEqual(outParts[0], 'Items out', 'Library # of items checked out had wrong text')
                numout = int(outParts[1].split()[0])
                self.assertEqual(numout, self.user.libraryout, 'Number of library items checked out was wrong')

            # User has a library fine
            # If the user shouldn't have one, it makes sure they don't
            if self.user.libraryfine:
                try:
                    libcard.find_element_by_xpath('.//span[contains(., "%s")]' %self.user.libraryfine)
                except selenium.common.exceptions.NoSuchElementException: 
                    self.fail("Didn't find library fine when one was expected")
            else:
                try:
                    libcard.find_element_by_xpath('.//span[contains(., "You owe")]')
                    self.fail('Found library fine when one was not expected')
                except selenium.common.exceptions.NoSuchElementException: 
                    pass
            
    # Check for correct future quarters
    def check_future_quarters(self):
        # This is the old style test. 
        # You manually set fq_<quartername> to True and it checks for it.
        if self.user.fq_summera or self.user.fq_summerb or self.user.fq_fall:
            cards = self.driver.find_elements_by_xpath('//div[@data-name="FutureCard"]')
            fqnames = []
            for card in cards:
                try:
                    fqnames.append(card.find_element_by_tag_name('h4').text)
                except selenium.common.exceptions.NoSuchElementException: 
                    self.fail('h4 on future quarter card missing')

            if self.user.fq_summera:
                self.assertIn('Summer 2013 A-Term', fqnames, 'Missing Summer A-term card')
            if self.user.fq_summerb:
                self.assertIn('Summer 2013 B-Term', fqnames, 'Missing Summer B-term card')
            if self.user.fq_fall:
                self.assertIn('Autumn 2013', fqnames, 'Missing Autmn card')

        # This is the new style test. You simply supply the names of the expected
        # future quarters. Any extraneous cards found will case the test to fail. 
        if self.user.futureQtrs:
            cards = self.driver.find_elements_by_xpath('//div[@data-name="FutureCard"]')
            fqnames = []
            for card in cards:
                try:
                    fqnames.append(card.find_element_by_tag_name('h4').text)
                except selenium.common.exceptions.NoSuchElementException: 
                    self.fail('h4 on future quarter card missing')

            self.assertEqual(self.user.futureQtrs, fqnames)

    def check_notices_page(self):
        # Not doing this yet because it's broken so the exact expected data
        # is unknown
        pass

    # Check for any generic error cards
    def check_for_errors(self):
        try:
            e = self.driver.find_element_by_class_name('error-card')
            self.fail('Found an error card')
        except selenium.common.exceptions.NoSuchElementException: 
            pass

    # Check for "No registration found" message if expected
    def check_noreg(self):
        if self.user.noregfound:
            try: 
                self.driver.find_element_by_class_name('no_courses_dupe_blocker')
            except selenium.common.exceptions.NoSuchElementException: 
                self.fail('Could not find "No Registration Found" message')
        else:
            try: 
                self.driver.find_element_by_class_name('no_courses_dupe_blocker')
                self.fail('Found "No Registration Found" card when not expected. ')
            except selenium.common.exceptions.NoSuchElementException: 
                pass

    # Check resources links
    def check_resources(self):
        if self.user.resources:
            ares = {}
            eres = {}
            for k in self.user.resources:
                self.browse_resources(k)
                ecats = list(self.user.resources[k].keys())
                acatelements = self.driver.find_elements_by_class_name('category-sub-header')
                acatnames = []
                for e in acatelements:
                    acatnames.append(str(e.text))
                acatnames.sort()
                ecats.sort()
                self.assertEqual(acatnames, ecats, 
                    'The category names on the resources page were not as expected on page %s' %k
                )

                # Check every child element of the div
                # h2s are headers, so start a new category
                # uls will contain a link, so add that to current category
                alinks = {}
                elems = self.driver.find_elements_by_xpath('//div[@class="category-content"]/*')
                #catname = 'nocat'
                for e in elems:
                    if e.tag_name == 'h2':
                        catname = str(e.text)
                        curlist = []
                        alinks[catname] = curlist
                    if e.tag_name == 'ul':
                        linke = e.find_element_by_tag_name('a')
                        linkname = linke.text
                        linkurl = linke.get_attribute('href')
                        curlist.append(link(linkname, linkurl))

                # Changing this
                # Visit every page and collect links, so we can see
                # everything that is wrong
                eres[k] = self.user.resources[k]
                ares[k] = alinks

            self.assertEqual(ares, eres)

                #time.sleep(4)

    # Test for presence of tuition card and correct balance and due date
    # Returns failure on no card, no card values
    def check_tuition(self):
        if self.user.tuition:
            
            try:
                tc = self.driver.find_element_by_xpath('//div[@id="TuitionCard"]')
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Tuition card not found when one was expected')

            if self.user.tuition['balance']:
                self.assertIn('You owe', tc.text, '"You owe" message not found')


            # Check a future date
            if self.user.tuition['due'] == 'future':
                # Lazy check
                self.assertIn('in ', tc.text, '"in X days" message not found on tuition card')
                self.assertIn(' days', tc.text, '"in X days" message not found on tuition card')

            # I don't know what to do here because of broken mock data
            if self.user.tuition['due'] == 'past':
                pass 
                
            if self.user.tuition['due'] == 'today':
                self.assertIn('in 0 days', tc.text, '"in 0 days" message not found on tuition card')
                self.assertIn('Tuition is due today.', tc.text, '"Tuition is due today" message not found on tuition card')
        
    # Test for presence of user profile and correct record details
    # Returns failure on no profile or incorrect data
    def check_records(self):
        if self.user.record:
            # Click button to see records
            try:
                self.driver.find_element_by_id("toggle_my_profile").click()
                time.sleep(3)
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Profile toggle not found when one was expected')

            # Compare expected values to actual values
            if self.user.record['fullname']:
                try:
                    fullname = self.driver.find_element_by_css_selector("div#my_profile span.profile_name").text
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Full name not found when one was expected')

                self.assertEqual(fullname, self.user.record['fullname'])

            if self.user.record['permanentphone'] or self.user.record['permanentaddress']:
                try:
                    addressText = self.driver.find_element_by_css_selector("div#my_profile div.profile-perm-address").text.split('\n')
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find permanent address.')
                    
                if self.user.record['permanentphone']:
                    test_passed = False
                    for elementText in addressText:
                        if elementText.startswith("Phone"):
                            phoneNumber = elementText.split(':')[1].strip()
                            test_passed = True
                            self.assertEqual(phoneNumber, self.user.record['permanentphone'])


                    if test_passed == False:
                        self.fail('Could not find permanent phone number.')

                if self.user.record['permanentaddress']:
                    address = self.user.record['permanentaddress']
                    index = 1
                    
                    if address['apartment']:
                        self.assertEqual(addressText[index], address['apartment'])
                        index = index + 1

                    if address['street']:
                        self.assertEqual(addressText[index], address['street'])
                        index = index + 1

                    index = index + 1 # Jumps over name in address

                    streetAddress = addressText[index].split(' ')
                    self.assertEqual(streetAddress[0][0:4], address['city'])
                    self.assertEqual(streetAddress[1][0:5], address['state'])
                    self.assertEqual(streetAddress[2][0:3], address['zip'])

            if self.user.record['localphone'] or self.user.record['localaddress']:
                try:
                    addressText = self.driver.find_element_by_css_selector("div#my_profile div.profile-local-address").text.split('\n')
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find local address.')
                    
                if self.user.record['localphone']:
                    test_passed = False
                    for elementText in addressText:
                        if elementText.startswith("Phone"):
                            phoneNumber = elementText.split(':')[1].strip()
                            test_passed = True
                            self.assertEqual(phoneNumber, self.user.record['localphone'])

                    if test_passed == False:
                        self.fail('Could not find local phone number.')

                if self.user.record['localaddress']:
                    address = self.user.record['localaddress']
                    index = 1
                    
                    if address['apartment']:
                        self.assertEqual(addressText[index], address['apartment'])
                        index = index + 1
                        
                    if address['street']:
                        self.assertEqual(addressText[index], address['street'])
                        index = index + 1

                    index = index + 1 # Jumps over name in address

                    streetAddress = addressText[index].split(' ')
                    self.assertEqual(streetAddress[0][0:4], address['city'])
                    self.assertEqual(streetAddress[1][0:5], address['state'])
                    self.assertEqual(streetAddress[2][0:3], address['zip'])


    # Check the academic card
    # Checks for presence of card if expected, and correct class, major,
    # minor, and links
    def check_academic_card(self):
        if self.user.academic_card:
            try:
                self.driver.find_element_by_id("AcademicCard")
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Could not find academic card')

            if self.user.academic_card['class']:
                try:
                    userClass = self.driver.find_element_by_css_selector("div#AcademicCard div.class-standing p").text
                    self.assertEqual(userClass, self.user.academic_card['class'])
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find class standing on academic card')


            if self.user.academic_card['major']:
                try:
                    userMajor = self.driver.find_element_by_css_selector("div#AcademicCard div.class-standing ul:first-of-type").text
                    self.assertEqual(userMajor, self.user.academic_card['major'])
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find major on academic card')

            if self.user.academic_card['minor']:
                try:
                    userMinor = self.driver.find_element_by_css_selector("div#AcademicCard div.class-standing ul:last-of-type").text
                    self.assertEqual(userMinor, self.user.academic_card['minor'])
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find minor on academic card')

            # This is currently broken due to needing to click the button to 
            # expand this section
            try:
                self.driver.find_element_by_id("toggle_academic_card_resources").click()
            except selenium.common.NoSuchElementException:
                self.fail('Could not find academic card show/hide toggle')

            if self.user.academic_card['links']:
                try:
                    cardLinks = self.driver.find_elements_by_css_selector("academic_card_resources a")
                    links = []
                    for element in cardLinks:
                        links.append[link(element.text, element.get_attribute('href'))]
                    
                    for link in links:
                        self.assertIn(link, self.user.academic_card['links'])

                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find resource links on card')

    # Check the data on the Final grades card
    # Looks for the "GradeCard" id
    # Extracts data from it, compares it to expected data
    def check_grade_card(self):
        if self.user.grade_card:
            try:
                self.driver.find_element_by_id("GradeCard")
            except selenium.common.exceptions.NoSuchElementException:
                self.fail('Could not find grade card')

            if 'courses' in self.user.grade_card:
                # Check Course Titles
                try:
                    courseElements = self.driver.find_elements_by_css_selector("div#GradeCard div.pull-left span.card-badge-inline-label")
                    courseTitles = []
                    for element in courseElements:
                        courseTitles.append(element.text)
                    
                    expectedCourses = self.user.grade_card['courses'].keys()
                    self.assertEqual(courseTitles.sort(), expectedCourses.sort())
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not get courses from grade card.')

                # Check Course Colors
                try:
                    courseElements = self.driver.find_elements_by_css_selector("div#GradeCard div.pull-left")
                    for element in courseElements:
                        try:
                            courseTitle = element.find_element_by_css_selector("span").text
                        except selenium.common.exceptions.NoSuchElementException:
                            self.fail('Class not found on grade page.')

                        try:
                            courseColor = element.find_element_by_css_selector("div").value_of_css_property('background-color')
                        except selenium.common.exceptions.NoSuchElementException:
                            self.fail('Class color element not found on grade page.')

                        try:
                            courseCard = self.driver.find_element_by_css_selector("div#CourseCard div[data-identifier=\"" + courseTitle + "\"] div:first-of-type").value_of_css_property("border-top").split(' ',2)[2]
                        except selenium.common.exceptions.NoSuchElementException:
                            self.fail('Class card color element not found.')

                        assert courseColor[4:].startswith(courseCard[3:-1]), 'Wrong color found on grade card for course ' + courseTitle + '.'
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find course elements on grade card')

                # Check Course Grades
                try:
                    courseElements = self.driver.find_elements_by_css_selector("div#GradeCard div.card-badge-container li.clearfix")
                    for element in courseElements:
                        try:
                            courseTitle = element.find_element_by_css_selector("div.pull-left span").text
                        except selenium.common.exceptions.NoSuchElementException:
                            self.fail('Could not find course title element on grade card.')
                        
                        try:
                            courseGrade = element.find_element_by_css_selector("div.pull-right span").text
                        except selenium.common.exceptions.NoSuchElementException:
                            self.fail('Could not find course grade on element page.')

                        assert self.user.grade_card['courses'][courseTitle] == courseGrade, courseGrade + ' found where ' + self.user.grade_card['courses'][courseTitle] + ' was expected for course ' + courseTitle + '.'
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find course elements on grade card')

            # Check Submission Deadline
            # To Do: check for particular date, could automate to only check in appropriate times if there was someway of getting the server time
            if 'deadline' in self.user.grade_card:
                try:
                    foundDeadline = False
                    spanElements = self.driver.find_elements_by_css_selector("div#GradeCard span")
                    for elements in spanElements:
                        if element.text.startswith("Note"):
                            foundDeadline = True

                    assert foundDeadline == self.user.grade_card['deadline'], ('Grade submission deadline found when not expected or not found when expected.')

                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find grade submission deadline')

                

            try:
                self.driver.find_element_by_id("toggle_grade_card_resources").click()
            except:
                self.fail('Could not find grade card toggle')

            if self.user.grade_card['links']:
                try:
                    cardLinks = self.driver.find_elements_by_css_selector("grade_card_resources a")
                    links = []
                    for element in cardLinks:
                        links.append[link(element.text, element.get_attribute('href'))]
                    
                    for link in links:
                        assert link in self.user.grade_card['links'], (link + " not found on grade card")
                        
                except selenium.common.exceptions.NoSuchElementException:
                    self.fail('Could not find resource links on card')               


# These are the classes that a test scenario should actually subclass
# Each one of them pulls the desired check_X functions from above, 
# and calls it test_check_X so that the test framework will consider
# it to be a test. 

# Class for normal user scenarios (test a lot of things)
class myuw_user_scenario(myuw_base_scenario):
    # Which tests to run
    tests = (
        #'notices_count',
        'email_link',
        'reg_card',
        'schedule',
        'visual_schedule',
        'HFS',
        'library',
        'future_quarters',
        'notices_page',
        'for_errors',
        'noreg',
        'resources',
        'tuition',
        #'records',
        'academic_card',
        'grade_card',
    )

    for testname in tests:
        vars()['test_check_' + testname] = getattr(myuw_base_scenario, 'check_' + testname)

# Class for date testing scenarios (test mainly date-dependent stuff)
class myuw_date_scenario(myuw_base_scenario):

    tests = (
        'grade_card',
        'card_order',
        'future_quarters',
    )

    for testname in tests:
        vars()['test_check_' + testname] = getattr(myuw_base_scenario, 'check_' + testname)
    
