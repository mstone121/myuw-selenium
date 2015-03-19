from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from myuw_selenium.test.card_tests_c import CardTest

import time

# General Test Class
class LibSubjectGuidesTest(CardTest):

    def setUp(self):
        CardTest.setUp(self)


    def getCardObjects(self):
        card_objects = self.driver.find_elements_by_css_selector("div#CourseCard div.card")

        card_objects_dict = {}
        for element in card_objects:
            class_title = element.get_attribute('data-identifier')
            card_objects_dict[class_title] = element

        return card_objects_dict


    
class LinkTest(LibSubjectGuidesTest):
    def _test(self):
        card_objects = self.getCardObjects()

        links = {}
        for course in card_objects.keys():
            # Open disclosure
            card_objects[course].find_element_by_css_selector("div.card-disclosure a").click()
            
            # Get link
            try:
                links[course] = str(card_objects[course].find_element_by_css_selector("a.lib_subject_guide").get_attribute('href'))
            except NoSuchElementException:
                pass
            
                 
        for link in self.links.keys():
            self.assertEqual(links[link], self.links[link])


class NavigateTest(LibSubjectGuidesTest):
    def _test(self):
        card_objects = self.getCardObjects()

        for course in self.links.keys():
            # Open disclosure
            card_objects[course].find_element_by_css_selector("div.card-disclosure a").click()

            # Go to page
            card_objects[course].find_element_by_css_selector("a.lib_subject_guide").click()
            self.assertEqual(str(self.driver.current_url), self.links[course])

            # Return to landing page
            self.driver.back()
            time.sleep(2)
            self.assertEqual(str(self.driver.current_url), self.live_server_url + '/mobile/landing/')

            # Reload card objects
            card_objects = self.getCardObjects()
            
