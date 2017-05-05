# -*- coding: UTF-8 -*-

"""Unit tests for brew."""

from __future__ import unicode_literals
import sys
import unittest
from .. import brew, BrewException

class TestBrew(unittest.TestCase):
    """Class to hold all the tests for this package."""

    # The first eight are the same used by Perl's Text::Brew test suite.
    # The remainder are additional capability tests.

    def test_brew01(self):
        """Test edit distance between 'foo' and 'foo'."""
        expected = (0, ['MATCH', 'MATCH', 'MATCH'])
        self.assertTrue(brew.distance("foo", "foo", "both") == expected)

    def test_brew02(self):
        """Test edit distance between 'foo' and 'bar'."""
        expected = (3, ['SUBST', 'SUBST', 'SUBST'])
        self.assertTrue(brew.distance("foo", "bar", "both") == expected)

    def test_brew03(self):
        """Test edit distance between 'foo' and 'foobar'."""
        expected = (3, ['MATCH', 'MATCH', 'MATCH', 'INS', 'INS', 'INS'])
        self.assertTrue(brew.distance("foo", "foobar", "both") == expected)

    def test_brew04(self):
        """Test edit distance between 'foobar' and 'foo'."""
        expected = (3, ['MATCH', 'MATCH', 'MATCH', 'DEL', 'DEL', 'DEL'])
        self.assertTrue(brew.distance("foobar", "foo", "both") == expected)

    def test_brew05(self):
        """Test edit distance between 'abcd' and 'bcd'."""
        expected = (1, ['DEL', 'MATCH', 'MATCH', 'MATCH'])
        self.assertTrue(brew.distance("abcd", "bcd", "both") == expected)

    def test_brew06(self):
        """Test edit distance between 'bcd' and 'abcd'."""
        expected = (1, ['INS', 'MATCH', 'MATCH', 'MATCH'])
        self.assertTrue(brew.distance("bcd", "abcd", "both") == expected)

    def test_brew07(self):
        """Test edit distance between 'abde' and 'abcde'."""
        expected = (1, ['MATCH', 'MATCH', 'INS', 'MATCH', 'MATCH'])
        self.assertTrue(brew.distance("abde", "abcde", "both") == expected)

    def test_brew08(self):
        """Test edit distance between 'abcde' and 'abde'."""
        expected = (1, ['MATCH', 'MATCH', 'DEL', 'MATCH', 'MATCH'])
        self.assertTrue(brew.distance("abcde", "abde", "both") == expected)

    def test_brew09(self):
        """Test edit distance between 'Parrot' and an empty string."""
        expected = (6, ['DEL', 'DEL', 'DEL', 'DEL', 'DEL', 'DEL'])
        self.assertTrue(brew.distance("Parrot", "", "both") == expected)

    def test_brew10(self):
        """Test edit distance between 'possible' and 'poss' where deletions are zero-weighted."""
        expected = (0, ['MATCH', 'MATCH', 'MATCH', 'MATCH', 'MATCH', 'MATCH', 'MATCH', 'MATCH'])
        self.assertTrue(brew.distance("possible", "poss", "both", (0, 1, 0, 1)) == expected)

    def test_brew11(self):
        """Test error handling of non-string input."""
        with self.assertRaises(BrewException):
            brew.distance(75, 67)

    # Note the following three tests trigger UnicodeEncodeError exceptions
    # with Python 2.6 and some 2.7 environments due to this bug:
    # https://bugs.python.org/issue10417. On MacOS X 10.11, its native
    # Python 2.6 triggers in an environment configured to support UTF-8,
    # while its Python 2.7 works fine. Under NetBSD 7.1, with the "C"
    # locale, Python 2.7 triggers as well. Python 2.7 has been left
    # enabled for now, as it passes in the Travis CI environment.
    if sys.hexversion >= 0x02070000:
        def test_brew12(self):
            """Test edit distance between 'cafe' and 'café'."""
            expected = (1, ['MATCH', 'MATCH', 'MATCH', 'SUBST'])
            self.assertTrue(brew.distance("cafe", "café", "both") == expected)

        def test_brew13(self):
            """Test edit distance between 'groß' and 'gross'."""
            expected = (2, ['MATCH', 'MATCH', 'MATCH', 'INS', 'SUBST'])
            self.assertTrue(brew.distance("groß", "gross", "both") == expected)

        def test_brew14(self):
            """Test edit distance between 'Σίβύλλα' and 'Sibylla'."""
            expected = (7, ['SUBST', 'SUBST', 'SUBST', 'SUBST', 'SUBST', 'SUBST', 'SUBST'])
            self.assertTrue(brew.distance("Σίβύλλα", "Sibylla", "both") == expected)

if __name__ == '__main__':
    unittest.main()
