# Test for Summer B term Future Qtr Card
# See JIRA for reference

import os
import getpass
import unittest

from myuw_selenium.tests.card_tests_c import CardTest

username = None
password = None

try:
    username = os.environ['MYUW_USERNAME']
except KeyError:
    username = input("Username: ")

try:
    password = os.environ['MYUW_PASSWORD']
except KeyError:
    password = getpass.getpass()
    
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'syncdb'])



class MUWM_3068(CardTest):

    def step_2(self):
        

    
