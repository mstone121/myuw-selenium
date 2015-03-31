from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from myuw_selenium.test.card_tests_c import CardTest

import time

# General Test Class
class CourseEvalTest(CardTest):

    def setUp(self):
        CardTest.setUp(self)


    def getCardObjects(self):
        card_objects = self.driver.find_elements_by_css_selector("div#CourseCard div.card")

        card_objects_dict = {}
        for element in card_objects:
            class_title = element.get_attribute('data-identifier')
            card_objects_dict[class_title] = element

        return card_objects_dict



class EvalsShownTest(CourseEvalTest):
    def _test(self):
        card_objects = self.getCardObjects()
        
        for course in card_objects.keys():
            self.assertIsInstance(card_objects[course].find_element_by_css_selector("div.myuw-course-eval"), WebElement)

class EvalsNotShownTest(CourseEvalTest):
    def _test(self):
        card_objects = self.getCardObjects()

        for course in card_objects.keys():
            with self.assertRaises(NoSuchElementException):
                card_objects[course].find_element_by_css_selector("div.myuw-course-eval")


class LinksTest(CourseEvalTest):
    def _test(self):
        card_objects = self.getCardObjects()

        courses = {}
        for course in card_objects.keys():
            links = {}
            link_elements = card_objects[course].find_elements_by_css_selector("div.myuw-course-eval a")
            for link in link_elements:
                links[link.text] = link.get_attribute("href")

            courses[course] = links
            
        print(links)
        #self.assertEqual(sorted(self.links), sorted(links))

class CloseDateTest(CourseEvalTest):
    def _test(self):
        card_objects = self.getCardObjects()

        element = card_objects[self.course]

        text = element.find_element_by_css_selector("div.card-related-messages strong").text

        import re
        pattern = re.compile('^All evaluations close on ([A-za-z]{3}) ([0-9]{1,2}).*$')
        match   = re.match(pattern, text)

        month = match.group(1)
        day   = match.group(2)

        print("Month: {0}\nDay: {1}\n".format(month, day))

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        import datetime
        date = datetime.date(2013, months.index(month) + 1, day)

        #self.assertEqual(self.date, date)
