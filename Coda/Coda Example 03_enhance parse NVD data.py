# Parse NVD data

import requests


def retrieve_nvd_data():
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0/?"\
          "pubStartDate=2025-07-30T00:00:00.000&pubEndDate=2025-08-06T00:00:00.000"

    headers = {
        'apiKey': '<api_key_inserted_here_as_Sring_value>'
    }

    response = requests.request("GET", url, headers=headers)
    nvd_data = response.json()

    print(response)
    print(type(nvd_data))

    return nvd_data


def parse_nvd_data(nvd_data_to_parse):

    count_of_all_critical_vulns = 0
    count_of_all_high_vulns = 0
    count_of_all_medium_vulns = 0
    count_of_all_low_vulns = 0
    count_of_all_vulns_with_pending_severity = 0

    for vulns in nvd_data_to_parse['vulnerabilities']:
        cve_metrics = vulns['cve']['metrics']
        if not cve_metrics:
            count_of_all_vulns_with_pending_severity += 1
        else:
            metrics_key = next(iter(cve_metrics))
            for details in vulns['cve']['metrics'][metrics_key]:
                if details['cvssData']['baseSeverity'] == 'CRITICAL':
                    count_of_all_critical_vulns += 1
                elif details['cvssData']['baseSeverity'] == 'HIGH':
                    count_of_all_high_vulns += 1
                elif details['cvssData']['baseSeverity'] == 'MEDIUM':
                    count_of_all_medium_vulns += 1
                elif details['cvssData']['baseSeverity'] == 'LOW':
                    count_of_all_low_vulns += 1

    print('\nCritical Vulnerability Summary of the Week:')
    print('The number of Critical vulns this week: ', count_of_all_critical_vulns)
    print('The number of High vulns this week: ', count_of_all_high_vulns)
    print('The number of Medium vulns this week: ', count_of_all_medium_vulns)
    print('The number of Low vulns this week: ', count_of_all_low_vulns)
    print('The number of vulns with a pending severity: ', count_of_all_vulns_with_pending_severity)


nvd_data_packet = retrieve_nvd_data()
parse_nvd_data(nvd_data_packet)
