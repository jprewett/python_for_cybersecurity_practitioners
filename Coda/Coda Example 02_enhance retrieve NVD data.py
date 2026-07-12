# Retrieve NVD data

import requests


def retrieve_nvd_data():
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0/?"\
          "pubStartDate=2025-07-30T00:00:00.000&pubEndDate=2025-08-06T00:00:00.000"

    headers = {
        'apiKey': '<api_key_inserted_here_as_String_value>'
    }

    response = requests.request("GET", url, headers=headers)
    nvd_data = response.json()

    print(response)
    print(type(nvd_data))

    return nvd_data


def parse_nvd_data():
    pass


nvd_data_packet = retrieve_nvd_data()
