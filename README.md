# CountryInfoFetcher

CountryInfoFetcher is a Python project designed to fetch and display information about countries using the [restcountries.com](https://restcountries.com) API. It provides details such as the country name, capital city, and a link to the flag image in PNG format, displayed in a tabular format in the console.

## Features

- Fetches country data from the restcountries.com API.
- Displays country information in a readable tabular format.
- Logs activities and errors for easy debugging and monitoring.

## Requirements

- Python 3.6+
- `requests` library
- `tabulate` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/igor20192/CountryInfoFetcher.git
    cd CountryInfoFetcher
    ```

2. Install the required libraries:
    ```bash
    pip install requests tabulate
    ```

## Usage

To fetch and display the country information, run the `main.py` script:

```bash
python country.py 
```

The script will fetch data from the API and display it in the console in a tabular format, including the country name, capital city, and flag URL.


## Project Structure

- country_info.py: Contains the CountryInfo class which handles fetching and displaying the data.
- README.md: Project documentation.

## Example Output

When you run the script, the output will be displayed in a table format like this:

+-----------------+----------------+-------------------------------------------------------------+
| Country Name    | Capital        | Flag URL                                                    |
+-----------------+----------------+-------------------------------------------------------------+
| Afghanistan     | Kabul          | https://flagcdn.com/w320/af.png                             |
| Albania         | Tirana         | https://flagcdn.com/w320/al.png                             |
| Algeria         | Algiers        | https://flagcdn.com/w320/dz.png                             |
| ...             | ...            | ...                                                         |
+-----------------+----------------+-------------------------------------------------------------+

## Logging

The application uses Python's logging module to log information and errors. The logs include details about fetching data, any HTTP errors, connection issues, and more.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me at [igor.udovenko2015@gmail.com].