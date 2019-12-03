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


class ViewTestCase(TestCase):

    def test_basic_passphrase_with_one_line(self):
        response = self.client.post(
            '/passphrase/basic',
            data='aa bb cc dd ee',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 1)

    def test_basic_passphrase_with_several_lines(self):
        response = self.client.post(
            '/passphrase/basic',
            data='aa bb cc dd ee\n aa bb cc dd aa \naa bb cc dd bab',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 2)

    def test_basic_passphrase_with_spaces(self):
        response = self.client.post(
            '/passphrase/basic',
            data='aa bb cc dd ee\n aa bb    cc dd   ',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 2)

    def test_basic_passphrase_with_emphty_passphrases(self):
        response = self.client.post(
            '/passphrase/advance',
            data='aa bb cc dd ee\n aa bb  \n \n   \n  cc dd',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 3)

    def test_advance_passphrase_with_one_line(self):
        response = self.client.post(
            '/passphrase/advance',
            data='aa bb cc dd ee',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 1)

    def test_advance_passphrase_with_several_lines(self):
        response = self.client.post(
            '/passphrase/advance',
            data='aa bb cc dd ee\n aa dda cc dad \naa bb cc dd bab',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 2)

    def test_advance_passphrase_with_spaces(self):
        response = self.client.post(
            '/passphrase/advance',
            data='aa bb cc dd ee\n aa bb    cc dd   ',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 2)

    def test_advance_passphrase_with_emphty_passphrases(self):
        response = self.client.post(
            '/passphrase/advance',
            data='aa bb ec dd ce\n aa bb  \n \n   \n  cd dc',
            content_type="text/plain"
        )
        self.assertEqual(response.json().get('valid_passphrase'), 1)
