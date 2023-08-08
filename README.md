# CRIS Data Retrieval Script

This script is designed to retrieve data from the CRIS (Current Research Information System) API using Python. It fetches information from various endpoints such as research outputs, persons, journals, publishers, organizations, and external organizations. The retrieved data is then processed and saved into Excel files for further analysis.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- The `requests` and `pandas` libraries. You can install them using the following commands:
  ```
  pip install requests pandas
  ```

## Setup

1. Clone or download this repository to your local machine.

2. Open the script file `cris_data_retrieval.py` in a text editor or an integrated development environment.

3. Obtain an API key from your CRIS administrator. Replace `'YOUR_API_KEY'` in the script with your actual API key.

## Usage

1. Run the script by executing the following command in your terminal or command prompt:

   ```
   cris_mining.py
   ```

2. The script will loop through the specified endpoints, retrieve data in chunks of 100 items, and save the data in Excel files.

3. Progress updates will be displayed as the script retrieves and processes the data. If an error occurs during the retrieval process, the status code will be printed.

## Output

The retrieved data will be saved as Excel files in the specified output directory. The files will be named based on the endpoint, such as `research-outputs_cris.xlsx`, `persons_cris.xlsx`, etc. You can find these files in the `raw_data` folder within your CRIS output directory.

## Note

- This script assumes that you have the necessary permissions for each endpoint granted by the CRIS administrator.
- You may need to adjust the file paths and API endpoint URLs based on your environment.

For any questions or issues, please feel free to reach out to gzeevi25@gmail.com.

---
