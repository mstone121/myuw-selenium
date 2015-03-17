from selenium.webdriver.remote.webelement import WebElement
from myuw_selenium.test.card_tests_c import CardTest

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
            card_objects[course].find_element_by_css_selector("div.card-disclosure").click()
            
            # Get link
            try:
                links[course] = element.find_element_by_css_selector("a.lib_subject_guide").get_attribute('href')
            except NoSuchElementException:
                pass
            

        self.assertEqual(links.sort(), self.links.sort())
