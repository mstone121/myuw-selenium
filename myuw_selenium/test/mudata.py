#!/usr/bin/python
# Class for commonly used links
# Uses the link class, which supports both link text and url
# Also has husky card names

from myuw_selenium.test.myuw import link

# Dict of email links
emails = {
    'live': link('UW Outlook', 'https://www.outlook.com/myuw.net'),
    'gmail': link('UW Gmail', 'http://gmail.uw.edu/')
}


# Dict of other links
links = {
    'bts': link('Bothell Time Schedules', 'http://www.uwb.edu/registration/time'),
    'sts': link('Seattle Time Schedules', 'http://www.washington.edu/students/timeschd/'),
    'reg': link('Registration', 'https://sdb.admin.washington.edu/students/uwnetid/register.asp'),
    'tts': link('Tacoma Time Schedules', 'http://www.washington.edu/students/timeschd/T/'),
    'tqs': link('Tacoma Time Schedule Quick Search', 'http://www.tacoma.washington.edu/enrollment_apps/timeschedule/search.cfm')
}

# Dict of different possible husky cards
HFScards = {
    'stu': 'Student Husky Card',
    'din': 'Resident Dining', 
    'staff': 'Employee Husky Card'
}
