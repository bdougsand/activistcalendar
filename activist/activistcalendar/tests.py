"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from activistcalendar.models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(
            user_name="David Test",
            user_email="david314@gmail.com",
            phone_number="+5934382319",
            website="http://www.foo.org/",
            personal_message="Hello",
            activist_groups=None,
            activist_events=None,
            activist_interests=None
        )

    def test_profile_exists(self):
        david = Profile.objects.get(user_email="david314@gmail.com")
        self.assertEqual(david.user_name, "David Test")
        self.assertEqual(david.user_email, "david314@gmail.com")
        self.assertEqual(david.phone_number, "+5934382319")
        self.assertEqual(david.website, "http://www.foo.org/")
        self.assertEqual(david.phone_number, "+5934382319")
        self.assertEqual(david.website, "http://www.foo.org/")
        self.assertEqual(david.personal_message, "Hello")
        self.assertEqual(david.activist_groups, None)
        self.assertEqual(david.activist_events, None)
        self.assertEqual(david.activist_interests, None)
