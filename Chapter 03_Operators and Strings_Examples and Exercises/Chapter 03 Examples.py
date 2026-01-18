# Indexing
cve_identifier = 'CVE-2019-0708'
print(cve_identifier[4])


# Slicing
cve_identifier = 'CVE-2019-0708'
print(cve_identifier[4:8])

cve_identifier = 'CVE-2019-0708'
print(cve_identifier[:8])

cve_identifier = 'CVE-2019-0708'
print(cve_identifier[9:])


# Concatenation
prefix = 'CVE'
year = '2025'
identifier = '0282'
delimiter = '-'
cve_identifier = prefix + delimiter + year + delimiter + identifier
print(cve_identifier)


# Conversion
year = 2025
year = str(year)
print(year)
print(type(year))


# Comparison
first_cvss_score = '5.3'
second_cvss_score = '5.3'
if first_cvss_score == second_cvss_score:
    print('These CVEs have the same CVSS score.')


# Membership Check
current_year = '2025'
cve = 'CVE-2019-0708'
if current_year not in cve:
    print('This CVE published prior to the current year.')


# Flaws
prefix = 'CVE'
year = '2025'
identifier = '0282'
delimiter = '-'
cve_identifier = prefix + delimiter + identifier + delimiter + year
print(cve_identifier)


# Bugs
# Original example. This is a coding bug
average_cvss_score = (6.2 * 9.8 * 1.3) / 3

# Bug-free example. This is the correct mathematical way to calculate CVE average
average_cvss_score = (6.2 + 9.8 + 1.3) / 3


# print()
cybersecurity_holy_trinity = ['Confidentiality', 'Integrity', 'Availability']
cybersecurity_holy_trinity = ['Availability', 'Confidentiality', 'Integrity']
cybersecurity_holy_trinity = ['Integrity', 'Availability', 'Confidentiality']


cybersecurity_holy_trinity = ['Confidentiality', 'Integrity', 'Availability']
cybersecurity_holy_trinity = ['Availability', 'Confidentiality', 'Integrity']
cybersecurity_holy_trinity = ['Integrity', 'Availability', 'Confidentiality']
print(cybersecurity_holy_trinity)


cybersecurity_holy_trinity = ['Confidentiality', 'Integrity', 'Availability']
cybersecurity_holy_trinity = ['Availability', 'Confidentiality', 'Integrity']
cybersecurity_holy_trinity = ['Integrity', 'Availability', 'Confidentiality']
print(cybersecurity_holy_trinity)
print(type(cybersecurity_holy_trinity))
