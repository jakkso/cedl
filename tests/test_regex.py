"""Test regex."""
import unittest as ut

from downloader.downloader import extract_extension_id


class TestRegex(ut.TestCase):
    """Test Regex matching."""

    def test_regex_matches(self):
        """Test `extract_regex_matches`."""
        url_1, url_2, url_3 = 'https://chrome.google.com/webstore/detail/amazon-assistant-for-chro' \
                              '/pbjikboenpfhbbejgkoklgkhjpfogcam?hl=en', \
                              'https://chrome.google.com/webstore/detail/amazon-assistant-for-chro' \
                              '/pbjikboenpfhbbejgkoklgkhjpfogcam', \
                              'https://chrome.google.com/webstore/detail/amazon-assistant-for-chro '
        res_1, res_2 = extract_extension_id(url_1), extract_extension_id(url_2)
        self.assertEqual(res_1, res_2)
        with self.assertRaises(RuntimeError):
            extract_extension_id(url_3)


