#!/bin/python

# myuw mobile user class

from myuw_selenium.test.mudata import *
from myuw_selenium.test.musettings import *
import selenium.common.exceptions
import time

# Class for a user
class testUser():
    def __init__(self, driver, test, **kwargs):
        self.driver = driver
        self.test = test

        self.urlbase = test.live_server_url

        # This is a hacky way of doing this but it beats typing everything twice    
        self.critical = 0
        self.unread = 0
        self.email = False
        self.regcard = False
        self.regcard2 = False
        self.regholds = 0
        self.reglinks = ()
        self.schedule = False
        self.courses = ()
        self.futureQtrs = ()
        self.vSchedule = False
        self.noregfound = False

        self.resources = {}
        self.record = False

        self.academic_card = False
        self.grade_card = False
        
        self.tuition = False
        self.HFS = False
        self.library = False
        self.libraryholds = 0
        self.libraryout = 0
        self.libraryfine = False
        self.regMsgs = False
        self.textbooks = ()

        self.fq_fall = ()
        self.fq_summera = ()
        self.fq_summerb = ()

        # Set everything up from the constructor
        for k, v in kwargs.items():
            if v is not None:
                setattr(self,k, v)
            #self.__setattr__(k, v)
        
        # If the landing/admin/resource URL suffixes are 
        # defined, combine them with the urlbase to get the
        # full url. Otherwise, use the defaults. 
        try: 
            self.landing = self.urlbase + self.landingsuffix 
        except:
            self.landing = self.urlbase + landing

        try:
            self.admin = self.urlbase + self.adminsuffix
        except:
            self.admin = self.urlbase + admin

        try:
            self.res = self.urlbase + self.ressuffix
        except:
            self.res = self.urlbase + res

        try:
            self.dates = self.urlbase + self.datesuffix
        except:
            self.dates = self.urlbase + dates
        



        # Workadound for MUWM-1930
        # Bug fixed, workaround no longer needed
        #if self.courses:
        #    self.vcourses = []
        #    for courseName in self.courses:
        #        nameSplit = courseName.split()
        #        name = ' '.join(nameSplit[:-1]) + nameSplit[-1]
        #        self.vcourses.append(name)

        # With the bug fixed, just copy the list
        if self.courses:
            self.vcourses = list(self.courses)


    # Checks to make sure notice counts are correct
    # Known issue: Does not check for a lack of notices on users
    # who are not supposed to have any
    def check_notices_count(self):
        if self.critical:
            try:
                e = self.driver.find_element_by_class_name('notice-information')
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Could not find notice bar')
            numCritical = int(e.text.split()[0])
            self.test.assertEqual(numCritical, self.critical, 'Incorrect number of critical notices on notice bar')

    def check_unread_notices_count(self):
        if self.unread:
            try:
                e = self.driver.find_element_by_xpath('//div[@class="notice-unread badge"]')
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Could not find unread notices count')
            numUnread = int(e.text.split()[0])
            self.test.assertEqual(numUnread, self.unread, 'Incorrect number of unread notices on notice bar')

    # Checks to make sure the user has the correct email link
    # Checks for lack of link for users who do not have it
    def check_email_link(self):
        if self.email:
            try:
                link = self.driver.find_element_by_xpath('//div[@id="uwemail"]/a')
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Could not find email link when one was expected')
            self.test.assertEqual(link.text, self.email.text)
            self.test.assertEqual(link.get_attribute('href'), self.email.url)
            self.test.assertEqual(link.get_attribute('target'), '_blank')
        else:
            try:
                link = self.driver.find_element_by_xpath('//div[@id="uwemail"]/a')
                self.test.fail('Found email link for a user with no email')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            
    # Checks for presense of registration card, and correct links
    # on the card
    # You can either specify the reg card title as a string, as a list of reg card titles, 
    # or the legacy 'True' value. 
    def check_reg_card(self):
        if self.regcard:
            if type(self.regcard) == str:
                regcard = [self.regcard]
            elif self.regcard == True:
                regcard = ['Registration: Summer 2013']
            else:
                regcard = self.regcard
            #time.sleep(.5) # TODO: do this better
            el = self.driver.find_elements_by_xpath('//div[@data-name="RegistrationCard"]')

            if len(el) != len(regcard):
                self.test.fail('Found %s reg cards when %s were expected' %(len(el), len(regcard)))
            
            for i in range(len(el)):
                e = el[i]
                card = regcard[i]
                title = e.find_element_by_tag_name('h3').text
                self.test.assertEqual(title, card)

        else:

            el = self.driver.find_elements_by_xpath('//div[@data-name="RegistrationCard"]')
            if len(el) > 0:
                self.test.fail('Found reg card(s) when none were expected')
            # Broken right now because of show more button
            # TODO: fix
            #if self.reglinks:
            #    links = e.find_elements_by_xpath('./div/div/ul[@class="reg-resources-list"]//a')
            #    for i in range(0, len(self.reglinks)):
            #        self.test.assertEqual(self.reglinks[i].text, links[i].text, 'Registration card link had the wrong text')
            #        self.test.assertEqual(self.reglinks[i].url, links[i].get_attribute('href'), 'Registration card link had the wrong URL')

        

    # Checks to make sure course cards are as expected
    def check_schedule(self):
        if self.schedule:
            courseCards = []
            cards = self.driver.find_elements_by_xpath('//div[@id="CourseCard"]//div[@class="card"]')
                
            for card in cards:
                try:
                    courseName = card.find_element_by_class_name('courseIDtitle').text
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find course title on course card')
                courseCards.append(courseName)
            courseCards.sort()
            expectedCourses = list(self.courses)
            expectedCourses.sort()
            self.test.assertEqual(courseCards, expectedCourses)

    # Make sure nothing unexpected appears on the vis sched
    def check_visual_schedule(self):
        if self.vSchedule:
            #vsched = self.driver.find_element_by_xpath('//div[@class="visual-schedule twelve-hour"]')
            try:
                vsched = self.driver.find_element_by_class_name('visual-schedule')
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Could not find visual schedule when one was expected')
            for course in vsched.find_elements_by_xpath('.//div[@class="visual-course"]'):
                courseTitle = course.find_element_by_tag_name('div').text
                self.test.assertIn(courseTitle, self.vcourses, 'Visual schedule did not have the correct courses')
                # TODO: Check to make sure course card has the correct links

    # Checks to make sure we have the right husky card balances in the HFS card
    def check_HFS(self):
        if self.HFS:
            huskycards = self.driver.find_elements_by_xpath('//div[@id="HFSCard"]//span[@class="card-badge-label"]')
            hfsnames_expected = []
            for i in self.HFS:
                hfsnames_expected.append(HFScards[i])
            hfsnames_actual = []
            for e in huskycards:
                hfsnames_actual.append(e.text)

            self.test.assertEqual(hfsnames_actual, hfsnames_expected, 'HFS card contained the wrong husky cards')

    # Checks the library card for the correct number of holds and
    # checked out items
    def check_library(self):
        if self.library:
            try:
                libcard = self.driver.find_element_by_id('LibraryCard')
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Could not find library card when one was expected')

            # Check 'n requested item(s) ready'
            if self.libraryholds:
                # The format of this thing keeps changing
                try:
                    holdText = libcard.find_element_by_class_name('card-noncritical-alert').text
                except selenium.common.exceptions.NoSuchElementException: 
                    self.test.fail('Could not find library holds when it was expected')
                holdParts = holdText.split('\n')[1].split()
                if holdParts[2] == 'items':
                    holdParts[2] = 'item'
                self.test.assertEqual(holdParts[1:], ['requested', 'item', 'ready'], '"Requested items" text was not correct')
                try:
                    self.test.assertEqual(int(holdParts[0]), self.libraryholds, 'Number of library holds was incorrect')
                except ValueError:
                    self.test.fail('Wrong format on library card for requested items ready')

            if self.libraryout:
                try:
                    outText = libcard.find_element_by_xpath('./div/div/div[contains(., "Items out")]').text
                except selenium.common.exceptions.NoSuchElementException: 
                    self.test.fail('Could not find library items checked out')
                outParts = outText.splitlines()
                self.test.assertEqual(outParts[0], 'Items out', 'Library # of items checked out had wrong text')
                numout = int(outParts[1].split()[0])
                self.test.assertEqual(numout, self.libraryout, 'Number of library items checked out was wrong')

            if self.libraryfine:
                try:
                    libcard.find_element_by_xpath('.//span[contains(., "%s")]' %self.libraryfine)
                except selenium.common.exceptions.NoSuchElementException: 
                    self.test.fail("Didn't find library fine when one was expected")
            else:
                try:
                    libcard.find_element_by_xpath('.//span[contains(., "You owe")]')
                    self.test.fail('Found library fine when one was not expected')
                except selenium.common.exceptions.NoSuchElementException: 
                    pass
            
    # Check for correct future quarters
    def check_future_quarters(self):
        if self.fq_summera or self.fq_summerb or self.fq_fall:
            cards = self.driver.find_elements_by_xpath('//div[@data-name="FutureCard"]')
            fqnames = []
            for card in cards:
                try:
                    fqnames.append(card.find_element_by_tag_name('h4').text)
                except selenium.common.exceptions.NoSuchElementException: 
                    self.test.fail('h4 on future quarter card missing')

            if self.fq_summera:
                self.test.assertIn('Summer 2013 A-Term', fqnames, 'Missing Summer A-term card')
            if self.fq_summerb:
                self.test.assertIn('Summer 2013 B-Term', fqnames, 'Missing Summer B-term card')
            if self.fq_fall:
                self.test.assertIn('Autumn 2013', fqnames, 'Missing Autmn card')

        if self.futureQtrs:
            cards = self.driver.find_elements_by_xpath('//div[@data-name="FutureCard"]')
            fqnames = []
            for card in cards:
                try:
                    fqnames.append(card.find_element_by_tag_name('h4').text)
                except selenium.common.exceptions.NoSuchElementException: 
                    self.test.fail('h4 on future quarter card missing')

            self.test.assertEqual(self.futureQtrs, fqnames)

    def check_notices_page(self):
        # Not doing this yet because it's broken so the exact expected data
        # is unknown
        pass

    # Check for any generic error messages
    def check_for_errors(self):
        try:
            e = self.driver.find_element_by_class_name('error-card')
            self.test.fail('Found an error card')
        except selenium.common.exceptions.NoSuchElementException: 
            pass

    # Check for "No registration found" message
    def check_noreg(self):
        if self.noregfound:
            try: 
                self.driver.find_element_by_class_name('no_courses_dupe_blocker')
            except selenium.common.exceptions.NoSuchElementException: 
                self.test.fail('Could not find "No Registration Found" message')

    # Check resources links
    def check_resources(self):
        if self.resources:
            ares = {}
            eres = {}
            for k in self.resources:
                self.test.browse_resources(k)
                ecats = list(self.resources[k].keys())
                acatelements = self.driver.find_elements_by_class_name('category-sub-header')
                acatnames = []
                for e in acatelements:
                    acatnames.append(str(e.text))
                acatnames.sort()
                ecats.sort()
                self.test.assertEqual(acatnames, ecats, 
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
                eres[k] = self.resources[k]
                ares[k] = alinks

            self.test.assertEqual(ares, eres)

                #time.sleep(4)

    # Test for presence of tuition card and correct balance and due date
    # Returns failure on no card, no card values
    def check_tuition(self):
        if self.tuition:
            
            try:
                tc = self.driver.find_element_by_xpath('//div[id="TuitionCard"]')
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Tuition card not found when one was expected')

            if self.tuition['balance']:
                self.test.assertIn('You owe', tc.text, '"You owe" message not found')


            # Check a future date
            if self.tuition['due'] == 'future':
                # Lazy check
                self.test.assertIn('in ', tc.text, '"in X days" message not found on tuition card')
                self.test.assertIn(' days', tc.text, '"in X days" message not found on tuition card')

            # I don't know what to do here because of broken mock data
            if self.tuition['due'] == 'past':
                pass 
                
            if self.tuition['due'] == 'today':
                self.test.assertIn('in 0 days', tc.text, '"in 0 days" message not found on tuition card')
                self.test.assertIn('Tuition is due today.', tc.text, '"Tuition is due today" message not found on tuition card')
        
    # Test for presence of user profile and correct record details
    # Returns failure on no profile or incorrect data
    def check_records(self):
        if self.record:
            
            try:
                self.driver.find_element_by_id("toggle_my_profile").click()
                time.sleep(3)
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Profile toggle not found when one was expected')

            if self.record['fullname']:
                try:
                    fullname = self.driver.find_element_by_css_selector("div#my_profile span.profile_name").text
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Full name not found when one was expected')

                self.test.assertEqual(fullname, self.record['fullname'])

            if self.record['permanentphone'] or self.record['permanentaddress']:
                try:
                    addressText = self.driver.find_element_by_css_selector("div#my_profile div.profile-perm-address").text.split('\n')
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find permanent address.')
                    
                if self.record['permanentphone']:
                    test_passed = False
                    for elementText in addressText:
                        if elementText.startswith("Phone"):
                            phoneNumber = elementText.split(':')[1].strip()
                            test_passed = True
                            self.test.assertEqual(phoneNumber, self.record['permanentphone'])


                    if test_passed == False:
                        self.test.fail('Could not find permanent phone number.')

                if self.record['permanentaddress']:
                    address = self.record['permanentaddress']
                    index = 1
                    
                    if address['apartment']:
                        self.test.assertEqual(addressText[index], address['apartment'])
                        index = index + 1

                    if address['street']:
                        self.test.assertEqual(addressText[index], address['street'])
                        index = index + 1

                    index = index + 1 # Jumps over name in address

                    streetAddress = addressText[index].split(' ')
                    self.test.assertEqual(streetAddress[0][0:4], address['city'])
                    self.test.assertEqual(streetAddress[1][0:5], address['state'])
                    self.test.assertEqual(streetAddress[2][0:3], address['zip'])

            if self.record['localphone'] or self.record['localaddress']:
                try:
                    addressText = self.driver.find_element_by_css_selector("div#my_profile div.profile-local-address").text.split('\n')
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find local address.')
                    
                if self.record['localphone']:
                    test_passed = False
                    for elementText in addressText:
                        if elementText.startswith("Phone"):
                            phoneNumber = elementText.split(':')[1].strip()
                            test_passed = True
                            self.test.assertEqual(phoneNumber, self.record['localphone'])

                    if test_passed == False:
                        self.test.fail('Could not find local phone number.')

                if self.record['localaddress']:
                    address = self.record['localaddress']
                    index = 1
                    
                    if address['apartment']:
                        self.test.assertEqual(addressText[index], address['apartment'])
                        index = index + 1
                        
                    if address['street']:
                        self.test.assertEqual(addressText[index], address['street'])
                        index = index + 1

                    index = index + 1 # Jumps over name in address

                    streetAddress = addressText[index].split(' ')
                    self.test.assertEqual(streetAddress[0][0:4], address['city'])
                    self.test.assertEqual(streetAddress[1][0:5], address['state'])
                    self.test.assertEqual(streetAddress[2][0:3], address['zip'])



    def check_academic_card(self):
        if self.academic_card:
            try:
                self.driver.find_element_by_id("AcademicCard")
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Could not find academic card')

            if self.academic_card['class']:
                try:
                    userClass = self.driver.find_element_by_css_selector("div#AcademicCard div.class-standing p").text
                    self.test.assertEqual(userClass, self.academic_card['class'])
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find class standing on academic card')


            if self.academic_card['major']:
                try:
                    userMajor = self.driver.find_element_by_css_selector("div#AcademicCard div.class-standing ul:first-of-type").text
                    self.test.assertEqual(userMajor, self.academic_card['major'])
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find major on academic card')

            if self.academic_card['minor']:
                try:
                    userMinor = self.driver.find_element_by_css_selector("div#AcademicCard div.class-standing ul:last-of-type").text
                    self.test.assertEqual(userMinor, self.academic_card['minor'])
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find minor on academic card')

            try:
                self.driver.find_element_by_id("toggle_academic_card_resources").click()
            except selenium.common.NoSuchElementException:
                self.test.fail('Could not find academic card show/hide toggle')

            if self.academic_card['links']:
                try:
                    cardLinks = self.driver.find_elements_by_css_selector("academic_card_resources a")
                    links = []
                    for element in cardLinks:
                        links.append[link(element.text, element.get_attribute('href'))]
                    
                    for link in links:
                        self.test.assertIn(link, self.academic_card['links'])

                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find resource links on card')

    def check_grade_card(self):
        if self.grade_card:
            try:
                self.driver.find_element_by_id("GradeCard")
            except selenium.common.exceptions.NoSuchElementException:
                self.test.fail('Could not find grade card')

            if 'courses' in self.grade_card:
                # Check Course Titles
                try:
                    courseElements = self.driver.find_elements_by_css_selector("div#GradeCard div.pull-left span.card-badge-inline-label")
                    courseTitles = []
                    for element in courseElements:
                        courseTitles.append(element.text)
                    
                    expectedCourses = self.grade_card['courses'].keys()
                    self.test.assertEqual(courseTitles.sort(), expectedCourses.sort())
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not get courses from grade card.')

                # Check Course Colors
                try:
                    courseElements = self.driver.find_elements_by_css_selector("div#GradeCard div.pull-left")
                    for element in courseElements:
                        try:
                            courseTitle = element.find_element_by_css_selector("span").text
                        except selenium.common.exceptions.NoSuchElementException:
                            self.test.fail('Class not found on grade page.')

                        try:
                            courseColor = element.find_element_by_css_selector("div").value_of_css_property('background-color')
                        except selenium.common.exceptions.NoSuchElementException:
                            self.test.fail('Class color element not found on grade page.')

                        try:
                            courseCard = self.driver.find_element_by_css_selector("div#CourseCard div[data-identifier=\"" + courseTitle + "\"] div:first-of-type").value_of_css_property("border-top").split(' ',2)[2]
                        except selenium.common.exceptions.NoSuchElementException:
                            self.test.fail('Class card color element not found.')

                        assert courseColor[4:].startswith(courseCard[3:-1]), 'Wrong color found on grade card for course ' + courseTitle + '.'
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find course elements on grade card')

                # Check Course Grades
                try:
                    courseElements = self.driver.find_elements_by_css_selector("div#GradeCard div.card-badge-container li.clearfix")
                    for element in courseElements:
                        try:
                            courseTitle = element.find_element_by_css_selector("div.pull-left span").text
                        except selenium.common.exceptions.NoSuchElementException:
                            self.test.fail('Could not find course title element on grade card.')
                        
                        try:
                            courseGrade = element.find_element_by_css_selector("div.pull-right span").text
                        except selenium.common.exceptions.NoSuchElementException:
                            self.test.fail('Could not find course grade on element page.')

                        assert self.grade_card['courses'][courseTitle] == courseGrade, courseGrade + ' found where ' + self.grade_card['courses'][courseTitle] + ' was expected for course ' + courseTitle + '.'
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find course elements on grade card')

            # Check Submission Deadline
            # To Do: check for particular date, could automate to only check in appropriate times if there was someway of getting the server time
            if 'deadline' in self.grade_card:
                try:
                    foundDeadline = False
                    spanElements = self.driver.find_elements_by_css_selector("div#GradeCard span")
                    for elements in spanElements:
                        if element.text.startswith("Note"):
                            foundDeadline = True

                    assert foundDeadline == self.grade_card['deadline'], ('Grade submission deadline found when not expected or not found when expected.')

                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find grade submission deadline')

                

            try:
                self.driver.find_element_by_id("toggle_grade_card_resources").click()
            except:
                self.test.fail('Could not find grade card toggle')

            if self.grade_card['links']:
                try:
                    cardLinks = self.driver.find_elements_by_css_selector("grade_card_resources a")
                    links = []
                    for element in cardLinks:
                        links.append[link(element.text, element.get_attribute('href'))]
                    
                    for link in links:
                        assert link in self.grade_card['links'], (link + " not found on grade card")
                        
                except selenium.common.exceptions.NoSuchElementException:
                    self.test.fail('Could not find resource links on card')               

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

        el = self.driver.find_elements_by_xpath('//div[@id="landing_content"]/div')
        
        for i in range(len(el)):
            e = el[i]
            actualName = e.get_attribute('id')
            expectedName = expected[i]
            self.test.assertEqual(expectedName, actualName)
        


    all_tests = (
        #check_notices_count, 
        #check_unread_notices_count, 
        check_email_link, 
        check_schedule, 
        check_visual_schedule, 
        check_HFS, 
        check_library, 
        check_future_quarters, 
        check_notices_page,
        check_for_errors,
        check_resources,
        #check_records,
        check_academic_card,
        check_grade_card,
        check_reg_card, 
    )

    # Run every check
    # Comment a line out here if you don't want it to run
    def run_all_tests(self):
    # Function to run all individual checks
        for test in self.all_tests:
            test(self)

class testUserDate(testUser):
    all_tests = (
        #testUser.all_tests[1],
        #testUser.all_tests[2],
        #testUser.all_tests[5], 
        #testUser.all_tests[7], 
        #testUser.all_tests[9],
        #testUser.all_tests[10],
        #testUser.all_tests[11], 
        testUser.check_grade_card,
        testUser.check_card_order,
        testUser.check_future_quarters,
    )
