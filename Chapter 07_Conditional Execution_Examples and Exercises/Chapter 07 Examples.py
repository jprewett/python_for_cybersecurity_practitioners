# Boolean Values
critical_vulnerability = True
print(type(critical_vulnerability))


# Conditional Execution - String Comparison
first_cvss_score = '5.3'
second_cvss_score = '5.3'
if first_cvss_score == second_cvss_score:
    print('These CVEs have the same CVSS score.')


# Conditional Execution - String Membership Check
current_year = '2025'
cve = 'CVE - 2019 - 0708'
if current_year not in cve:
    print('This CVE published prior to the current year.')


# Alternative Execution - String Comparison
first_cvss_score = '5.3'
second_cvss_score = '5.3'
if first_cvss_score == second_cvss_score:
    print('These CVEs have the same CVSS score.')
else:
    print('These CVEs have different CVSS scores.')


# Alternative Execution - String Membership Check
current_year = '2025'
cve = 'CVE-2019-0708'
if current_year not in cve:
    print('This CVE published prior to the current year.')
else:
    print('This CVE published in the current year.')


# Chained Conditionals
vulnerability_cvss_score = 9.8
if 9.0 <= vulnerability_cvss_score <= 10:
    print('This is a Critical severity vulnerability.')
elif 7.0 <= vulnerability_cvss_score <= 8.9:
    print('This is a High severity vulnerability.')
elif 4.0 <= vulnerability_cvss_score <= 6.9:
    print('This is a Medium severity vulnerability.')
elif 0.1 <= vulnerability_cvss_score <= 3.9:
    print('This is a Low severity vulnerability.')
else:
    print('This vulnerability has no severity.')


# Nested Conditionals
current_year = '2025'
vulnerability_id = 'CVE-2019-0708'
vulnerability_cvss_score = 5.5

if 9.0 <= vulnerability_cvss_score <= 10:
    print('This is a Critical severity vulnerability.')
    if current_year not in vulnerability_id:
        print('This is an old vulnerability of Critical severity.')
elif 7.0 <= vulnerability_cvss_score <= 8.9:
    print('This is a High severity vulnerability.')
    if current_year not in vulnerability_id:
        print('This is an old vulnerability of High severity.')
elif 4.0 <= vulnerability_cvss_score <= 6.9:
    print('This is a Medium severity vulnerability.')
    if current_year not in vulnerability_id:
        print('This is an old vulnerability of Medium severity.')
elif 0.1 <= vulnerability_cvss_score <= 3.9:
    print('This is a Low severity vulnerability.')
    if current_year not in vulnerability_id:
        print('This is an old vulnerability of Low severity.')
else:
    print('This vulnerability has no severity.')
    if current_year not in vulnerability_id:
        print('This is an old vulnerability with no severity.')


# Error Messages - Indentation Error
first_cvss_score = '5.3'
second_cvss_score = '5.3'
if first_cvss_score == second_cvss_score:
print('These CVEs have the same CVSS score.')


# Error Messages - Missing Colon
first_cvss_score = '5.3'
second_cvss_score = '5.3'
if first_cvss_score == second_cvss_score
    print('These CVEs have the same severity score.')