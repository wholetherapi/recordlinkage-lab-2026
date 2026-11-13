"""Unit tests for Cindermill Recordlink."""

import unittest

from cindermill_recordlink.matcher import decide


class MatcherTest(unittest.TestCase):
    def test_identical_records(self):
        left = {"email": "a@example.com", "phone": "555-0100", "surname": "Smith", "postcode": "AB1 2CD", "name": "Alice Smith", "address": "1 Main St"}
        right = dict(left)
        self.assertTrue(decide(left, right))

    def test_clearly_different_records(self):
        left = {"email": "a@example.com", "phone": "555-0100", "surname": "Smith", "postcode": "AB1 2CD", "name": "Alice Smith", "address": "1 Main St"}
        right = {"email": "b@example.org", "phone": "888-9999", "surname": "Jones", "postcode": "ZZ9 9ZZ", "name": "Bob Jones", "address": "9 Other Rd"}
        self.assertFalse(decide(left, right))


if __name__ == "__main__":
    unittest.main()
