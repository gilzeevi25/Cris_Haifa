# Data Retrieval Scripts

This repository contains Python scripts designed to retrieve data from different sources using APIs. These scripts fetch and process data for further analysis and save it in various formats.

## Scopus Data Scraper

This Python script is designed to scrape publication data from Scopus using the pybliometrics library. It retrieves publication information for researchers and updates the dataset periodically. The retrieved data is saved into a CSV file for further analysis.

### Prerequisites

Make sure you have the necessary libraries installed in your Python environment:
- `numpy`
- `pandas`
- `pickle`
- `re`
- `datetime`
- `pybliometrics`
- `tqdm`

Install them using the following command:
```bash
pip install numpy pandas pybliometrics tqdm
```

### Usage

1. Clone or download this repository to your local machine.

2. Open the Jupyter notebook `Getting_haifa_publications.ipynb` in your preferred code IDE.

3. Update the notebook with your desired configurations and input parameters, if needed.

4. Run the notebook. The script will gather publication data from Scopus and store it in a CSV file named `publications_with_abstracts_and_names_classes_v{version_number}.csv`.

5. You can periodically run the script to update the dataset with new publications for specific researchers.

### Configuration

The script uses the `pybliometrics` library to interact with Scopus. Make sure you have a Scopus API key and configure it in the `pybliometrics` library. If you haven't configured it yet, you can uncomment the line `pybliometrics.scopus.utils.create_config()` in the script and follow the instructions.

### Important Notes

- The script scrapes publication data from Scopus for specific researchers and updates the dataset. Ensure that you have the necessary permissions to access the researchers' data.

- The script may need periodic updates based on changes to the Scopus API or your specific requirements.

- Make sure to comply with Scopus's terms of use and guidelines while using this script.

## CRIS Data Retrieval Script

This script is designed to retrieve data from the CRIS (Current Research Information System) API using Python. It fetches information from various endpoints such as research outputs, persons, journals, publishers, organizations, and external organizations. The retrieved data is then processed and saved into Excel files for further analysis.

### Prerequisites

Before running the script, make sure you have the following prerequisites:
- Python 3.x installed on your system.
- The `requests` and `pandas` libraries. You can install them using the following commands:
  ```
  pip install requests pandas
  ```

### Setup

1. Clone or download this repository to your local machine.

2. Open the script file `cris_mining.py` in a text editor or an integrated development environment.

3. Obtain an API key from your CRIS administrator. Replace `'YOUR_API_KEY'` in the script with your actual API key.

### Usage

1. Run the script by executing the following command in your terminal or command prompt:
   ```
   cris_mining.py
   ```

2. The script will loop through the specified endpoints, retrieve data in chunks of 100 items, and save the data in Excel files.

3. Progress updates will be displayed as the script retrieves and processes the data. If an error occurs during the retrieval process, the status code will be printed.

### Output

The retrieved data will be saved as Excel files in the specified output directory. The files will be named based on the endpoint, such as `research-outputs_cris.xlsx`, `persons_cris.xlsx`, etc. You can find these files in the `raw_data` folder within your CRIS output directory.

### Note

- This script assumes that you have the necessary permissions for each endpoint granted by the CRIS administrator.

For any questions or issues related to the Scopus Data Scraper notebook or CRIS Data Retrieval script, please feel free to reach out to [Gil Zeevi](gzeevi25@gmail.com).
