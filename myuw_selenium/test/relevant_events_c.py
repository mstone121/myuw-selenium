from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from myuw_selenium.test.card_tests_c import CardTest


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

    def removeWhitespace(self, str):
        import re
        pat = re.compile(r'\s+')
        return pat.sub('', str)

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

class NoDisclosureTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()
        
        with self.assertRaises(NoSuchElementException):
            card_object.find_element_by_css_selector("div.card-disclosure a")

class LinksTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()
        self.openDisclosure(card_object)
    
        # Get all link elements from bottom of card
        links = card_object.find_elements_by_css_selector("div.myuw-events-calendar-link:last-of-type a")
        links.extend(card_object.find_elements_by_css_selector("div.myuw-events-calendar-link-sml a"))
        
        link_data = {}
        for link in links:
            link_data[str(link.text)] = str(link.get_attribute('href'))
            
        self.assertEqual(sorted(self.links), sorted(link_data))

class MessageTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()
        self.openDisclosure(card_object)

        try:
            message = card_object.find_element_by_css_selector("div.myuw-events-calendar-link-sml").text
        except NoSuchElementException:
            message = card_object.find_element_by_css_selector("div.myuw-events-calendar-link:last-of-type").text
    
        self.assertEqual(self.removeWhitespace(self.message), self.removeWhitespace(str(message)))

class EventsTest(RelevantEventsTest):
    def _test(self):
        card_object = self.getCardObject()
        self.openDisclosure(card_object)

        events = card_object.find_elements_by_css_selector("li.myuw-events-list-item")

        event_data = []
        for event in events:
            data = {}
            data['date']  = event.find_element_by_css_selector("div.myuw-events-date").text
            data['time']  = event.find_element_by_css_selector("span.myuw-events-time").text
            data['title'] = event.find_element_by_css_selector("span.myuw-events-title").text
            data['loc']   = event.find_element_by_css_selector("div.myuw-events-location").text

            event_data.append(data)

        self.assert_func(event_data)

    def assert_date_order(self, data):
        import datetime

        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dev']

        date_list = []
        year = int(self.date[:4])

        for event in data:
            date_string = event['date']
            date_string = date_string.split(' ')
            month = month_list.index(date_string[0]) + 1
            day   = int(date_string[1])

            time = event['time']
            time = time.split(':')
            hour = int(time[0])

            time = time[1].split(' ')
            minute = int(time[0])
            
            if time[1] == "PM":
                hour += 12
            
            date_list.append(datetime.datetime(year, month, day, hour, minute))

            
        self.assertEqual(date_list, sorted(date_list))

    def assert_events_count(self, data):
        self.assertEqual(len(data), self.count)
        

