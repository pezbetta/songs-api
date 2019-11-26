from django.test import TestCase
from .utils import _has_duplicates, _has_anagrams, _is_valid_passphrase, \
    check_list_passphrases


class UtilsTestCase(TestCase):

    def test__has_duplicates(self):
        """Animals that can speak are correctly identified"""
        self.assertFalse(_has_duplicates(['hola', 'mundo', 'elloh', 'world']))
        self.assertTrue(_has_duplicates(['hola', 'mundo', 'hello', 'mundo']))

    def test__has_anagrams(self):
        """Animals that can speak are correctly identified"""
        self.assertFalse(_has_anagrams(['hola', 'mundo', 'hello', 'world']))
        self.assertTrue(_has_anagrams(['hola', 'mundo', 'alho', 'world']))

    def test__is_valid_passphrase(self):
        """Animals that can speak are correctly identified"""
        self.assertTrue(_is_valid_passphrase('hola mundo hello world'))
        self.assertFalse(_is_valid_passphrase('hola mundo hola world'))

    def test__is_valid_passphrase_with_anagrams(self):
        """Animals that can speak are correctly identified"""
        self.assertTrue(_is_valid_passphrase(
            'hola mundo hello world', checks_anagrams=True
        ))
        self.assertFalse(_is_valid_passphrase(
            'hola mundo hola unmdo', checks_anagrams=True
        ))

    def test_check_list_passphrases(self):
        self.assertEqual(check_list_passphrases([
            'hola mundo hello world',
            'hola mundo hola unmdo',
            'song api song list',
            'song api songs list',
        ]), 2)

    def test_check_list_passphrases_with_anagrams(self):
        self.assertEqual(check_list_passphrases([
            'hola mundo hello world',
            'hola mundo hola unmdo',
            'song api song list',
            'song api gons list',
        ], checks_anagrams=True), 1)
