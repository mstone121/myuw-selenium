from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from myuw_selenium.test.card_tests_c import CardTest
import time

# General Test Class
class TextbookCardTest(CardTest):

    def setUp(self):
        CardTest.setUp(self)

        # Card ID
        self.card_name = "TextbookCard"


class NoCardShownTest(TextbookCardTest):
    def _test(self):
        # Check element is not displayed
        try:
            textbook_card_object = self.driver.find_element_by_id("TextbookCard")
            self.assertFalse(textbook_card_object.is_displayed(), 'Card is displayed')
        except NoSuchElementException:
            pass


class CardShownTest(TextbookCardTest):
    def _test(self):
        # Check for element
        textbook_card_object = self.getCardObject()
        self.assertIsInstance(textbook_card_object, WebElement)
        self.assertTrue(textbook_card_object.is_displayed())

class CoursesTest(TextbookCardTest):
    def _test(self):
        # Get element
        textbook_card_object = self.getCardObject()

        # Get course elements
        course_elements = textbook_card_object.find_elements_by_css_selector("span.textbooks-course-title")

        # Get course titles
        course_titles = []
        for element in course_elements:
            course_titles.append(str(element.text[:-1]))

        self.assertEqual(sorted(course_titles), sorted(self.courses))

class BookCountTest(TextbookCardTest):
    def _test(self):
        # Get element
        textbook_card_object = self.getCardObject()
        
        # Get course elements
        course_elements = textbook_card_object.find_elements_by_css_selector("li.textbooks-list-item")
        
        # Check book counts
        courses_list = []
        for element in course_elements:
            course = element.find_element_by_css_selector("span.textbooks-course-title").text[:-1]
            books  = element.find_element_by_css_selector("span.textbooks-course-books").text

            book_count = self.courses[str(course)]
            if (book_count == 0):
                self.assertEqual(books, 'No books')
            elif (book_count == 1):
                self.assertEqual(books, '1 book')
            else:
                self.assertEqual(books, str(book_count) + ' books')

            courses_list.append(str(course))

        # Check for correct courses (in case page has less courses than data)
        self.assertEqual(sorted(courses_list), sorted(self.courses.keys()))


class CourseColorTest(TextbookCardTest):
    def _test(self):
        # Get course colors
        course_colors = {}
        for course in self.courses:
            colored_element = self.driver.find_element_by_css_selector("div#CourseCard div[data-identifier='" + course + "'] div:first-child")
            course_color = colored_element.value_of_css_property('border-top-color')
            
            course_colors[course] = course_color

        # Get element
        textbook_card_object = self.getCardObject()

        # Get course elements
        course_elements = textbook_card_object.find_elements_by_css_selector("li.textbooks-list-item")

        courses_list = []
        for element in course_elements:
            # Course element
            course = element.find_element_by_css_selector("span.textbooks-course-title").text[:-1]
            courses_list.append(str(course))

            # Colored element
            colored_element = element.find_element_by_css_selector("div:first-child")
            card_color = colored_element.value_of_css_property('background-color')

            self.assertEqual(card_color, course_colors[str(course)])

        # Check for correct courses (in case page has less courses than data)
        self.assertEqual(sorted(courses_list), sorted(self.courses))

class FullPageLink(TextbookCardTest):
    def _test(self):
        # Get element
        textbook_card_object = self.getCardObject()
        
        # Check link exists
        try:
            full_page_link = textbook_card_object.find_element_by_css_selector("a.show_textbooks")
            self.assertIsInstance(full_page_link, WebElement)
        except NoSuchElementException:
            self.fail('No full page link element')

        full_page_link.click()

        self.assertEqual(self.driver.current_url, self.live_server_url + "/mobile/textbooks/current")

class NoFullPageLink(TextbookCardTest):
    def _test(self):
        # Get element
        textbook_card_object = self.getCardObject()

        with self.assertRaises(NoSuchElementException):
            ael = textbook_card_object.find_element_by_css_selector("a.show_textbooks")


class CourseTest(TextbookCardTest):
    def _test(self):
    # Get element
        textbook_card_object = self.getCardObject()

        course_elements = textbook_card_object.find_elements_by_css_selector("li.textbooks-list-item")

        for element in course_elements:
            course = element.find_element_by_css_selector("span.textbooks-course-title").text[:-1]
            if (course == self.course):
                # Check books label
                books = element.find_element_by_css_selector("span.textbooks-course-books").text            
                if (self.books == 0):
                    self.assertEqual(books, 'No books')
                elif (self.books == 1):
                    self.assertEqual(books, '1 book')
                else:
                    self.assertEqual(books, str(self.books) + ' books')

                # Check required
                if self.required:
                    required = element.find_element_by_css_selector("span.textbooks-course-required").text
                    self.assertEqual(required[1], str(self.required))
