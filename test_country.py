import unittest
from unittest.mock import patch
import requests
from country import CountryInfo


class TestCountryInfo(unittest.TestCase):
    @patch("country.requests.get")
    def test_get_country_data_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "name": {"common": "Testland"},
                "capital": ["Test City"],
                "flags": {"png": "https://flagcdn.com/w320/test.png"},
            }
        ]

        country_info = CountryInfo()
        result = country_info.get_country_data()

        self.assertEqual(
            result,
            [
                {
                    "name": {"common": "Testland"},
                    "capital": ["Test City"],
                    "flags": {"png": "https://flagcdn.com/w320/test.png"},
                }
            ],
        )

    @patch("country.requests.get")
    def test_get_country_data_http_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error")

        country_info = CountryInfo()
        result = country_info.get_country_data()

        self.assertEqual(result, [])

    @patch("country.requests.get")
    def test_get_country_data_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection Error")

        country_info = CountryInfo()
        result = country_info.get_country_data()

        self.assertEqual(result, [])

    @patch("country.CountryInfo.get_country_data")
    def test_display_countries_info(self, mock_get_country_data):
        mock_get_country_data.return_value = [
            {
                "name": {"common": "Testland"},
                "capital": ["Test City"],
                "flags": {"png": "https://flagcdn.com/w320/test.png"},
            }
        ]

        country_info = CountryInfo()

        with patch("builtins.print") as mock_print:
            country_info.display_countries_info()
            mock_print.assert_called_once()

    @patch("country.CountryInfo.get_country_data")
    def test_display_countries_info_no_data(self, mock_get_country_data):
        mock_get_country_data.return_value = []

        country_info = CountryInfo()

        with patch("builtins.print") as mock_print:
            country_info.display_countries_info()
            mock_print.assert_not_called()


if __name__ == "__main__":
    unittest.main()
