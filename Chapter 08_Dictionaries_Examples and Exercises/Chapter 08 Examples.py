# Limitations of Other Data Types
cve_company = 'Microsoft'
cve_identifier = 'CVE-2019-0708'
cve_description = 'Impact to Remote Desktop Protocol (RDP)'
cve_year_published = 2019
cve_severity_score = 9.8
cve_severity_rating = 'Critical'
cve_severity_sub_scores = [9.8, 5.9, 3.9]
cve_quantity = 1821

companies = ['Microsoft', 'IBM', 'Google']
cves = ['CVE-2019-0708', 'CVE-2024-47104', 'CVE-2015-1261']
cvss_scores = [9.8, 6.8, 5.0]


# Dictionary Characteristics - Example Dictionaries
{'Company': 'Microsoft', 'CVE': 'CVE-2019-0708', 'CVSS score': 9.8}
{'Company': 'IBM', 'CVE': 'CVE-2024-47104', 'CVSS score': 6.8}
{'Company': 'Google', 'CVE': 'CVE-2015-1261', 'CVSS score': 5.0}

{'Vector': 9.8, 'Complexity': 5.9, 'Privilege': 3.9}


# Dictionary with Duplicate Keys
{'Company': 'Microsoft', 'CVE': 'CVE-2019-0708', 'CVSS score': 9.8,
 'Company': 'IBM', 'CVE': 'CVE-2024-47104', 'CVSS score': 6.8,
 'Company': 'Google', 'CVE': 'CVE-2015-1261', 'CVSS score': 5.0}


# Dictionary Interaction
row1 = {'Company': 'Microsoft', 'CVE': 'CVE-2019-0708', 'CVSS score': 9.8}

print(row1.keys())

print(row1['CVE'])

row1['Severity'] = 'Critical'
print(row1)

row1.pop('Severity')
print(row1)

for key in row1:
    print(key)

for value in row1.values():
    print(value)
