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
        assertEqual(self.events, events)
            
class DisclosureTest(RelevantEventsTest):
    def _test(self):
        self.assertTrue(self.openDisclosure(self.getCardObject()))

class LinksTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()
        
        # Get all link elements from bottom of card
        links = card_object.find_elements_by_css_selector("div.myuw-events-calendar-link:last-of-type a")
        links.append(card_object.find_elements_by_css_selector("div.myuw-events-calendar-link-sml a"))
        
        link_data = {}
        for link in links:
            link_data[link.text] = link.get_attribute('href')
            
        self.assertEqual(self.links, link_data)

class MessageTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()

        try:
            message = card_object.find_element_by_css_selector("div.myuw-events-calendar-link-sml").text
        except NoSuchElementException:
            message = card_object.find_element_by_css_selector("div.myuw-events-calendar-link:last-of-type").text
    
        self.assertEqual(self.message, message)
