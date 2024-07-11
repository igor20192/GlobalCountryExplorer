import requests
import logging
from tabulate import tabulate


class CountryInfo:
    """
    A class to fetch and display country information using the restcountries.com API.
    """

    def __init__(self):
        """
        Initializes the API URL and sets up logging.
        """
        self.api_url = "https://restcountries.com/v3.1/all"
        logging.basicConfig(
            filename="country.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def get_country_data(self):
        """
        Fetches country data from the API.

        Returns:
            list: A list of country data in JSON format.

        Logs:
            INFO: When the data fetching process starts and completes successfully.
            ERROR: If any HTTP, connection, timeout, or other request exceptions occur.
        """
        try:
            logging.info("Fetching country data from API.")
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            logging.info("Successfully fetched country data.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            logging.exception(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            logging.exception(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            logging.exception(f"An error occurred: {req_err}")
        return []

    def display_countries_info(self):
        """
        Processes the fetched country data and displays it in a tabular format.

        The table includes the country name, capital city, and flag URL.

        Logs:
            ERROR: If no data is available for display or if any other exceptions occur during data processing.

        Prints:
            A table of country information with headers: "Country Name", "Capital", "Flag URL".
        """
        try:
            data = self.get_country_data()
            if not data:
                logging.error("No data to display.")
                return

            country_info_list = []

            for country in data:
                country_name = country.get("name", {}).get("common", "N/A")
                capital = country.get("capital", ["N/A"])[
                    0
                ]  # List of capitals, let's take the first one
                flag_url = country.get("flags", {}).get("png", "N/A")
                country_info_list.append([country_name, capital, flag_url])

            headers = ["Country Name", "Capital", "Flag URL"]
            print(tabulate(country_info_list, headers, tablefmt="grid"))
        except Exception as e:
            logging.exception(f"An error occurred while displaying data: {e}")


if __name__ == "__main__":
    country_info = CountryInfo()
    country_info.display_countries_info()
