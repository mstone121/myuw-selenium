from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from myuw_selenium.test.card_tests_c import CardTest
import time

# General Test Class
class RelevantEventsTest(CardTest):

    def setUp(self):
        CardTest.setUp(self)
        
        # Card ID
        self.card_name = "EventsCard"

    def getEvents(self):
        card_object = self.getCardObject()
        self.openDisclosure(card_object)

        events = card_object.find_elements_by_css_selector("li.myuw-events-list-item")
        data = {}
        for event in events:
           summary    = event.find_element_by_css_selector("span.myuw-events-title").text
           link       = event.find_element_by_css_selector("span.myuw-events-title a").get_attribute('href')
           start_time = event.find_element_by_css_selector("span.myuw-events-time").text
           location   = event.find_element_by_css_selector("div.myuw-events-location").text

           data[summary] = {}
           data[summary]['link']       = link
           data[summary]['start_time'] = start_time
           data[summary]['location']   = location

        return data

    def openDisclosure(self, card_object):
        try:
            card_object.find_element_by_css_selector("div.card-disclosure a").click()
            return True
        except NoSuchElementException:
            return None

class CardShownTest(RelevantEventsTest):
    def _test(self):
        # Check for element
        card_object = self.getCardObject()

        self.assertIsInstance(card_object, WebElement)
        self.assertTrue(card_object.is_displayed())

class NoCardShownTest(RelevantEventsTest):
    def _test(self):
        # Check element is not displayed
        try:
            card_object = self.driver.find_element_by_id("EventsCard")
            self.assertFalse(card_object.is_displayed(), 'Card is displayed')
        except NoSuchElementException:
            pass

class EventsTest(RelevantEventsTest):
    def _test(self):
        events = self.getEvents()

        print(events)
        # assertEqual(self.events, events)
            
class DisclosureTest(RelevantEventsTest):
    def _test(self):
        self.assertTrue(self.openDisclosure(self.getCardObject()))

class LinksTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()
        links = card_object.find_elements_by_css_selector("div.myuw-events-calendar-link ul.myuw-events-list a")
        
        link_data = {}
        for link in links:
            link_data[link.text] = link.get_attribute('href')

        print(link_data)

        # self.assertEqual(self.links, link_data)

class FutureEventsTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()
        line = card_object.find_element_by_css_selector("div.myuw-events-calendar-link").text.split('.')[0].strip()
    
        events = int(line.split(' ')[0])
        cals   = " ".join(line.split(' ')[3:])

        print(events + "\n")
        print(cals)

        # self.assertEqual(self.events, events)
        # self.assertEqual(self.cals, cals)
