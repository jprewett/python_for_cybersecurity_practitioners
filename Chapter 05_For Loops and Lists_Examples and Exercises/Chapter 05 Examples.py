# Loops and Variable Overwriting
total_vulnerability_count = 0

total_vulnerability_count = total_vulnerability_count + 1

total_vulnerability_count += 1


# Indexing and Debugging Review
cves_impacting_chrome = ['CVE-2022-4440', 'CVE-2025-0438', 'CVE-2024-8636', 'CVE-2022-0801',
                         'CVE-2019-5814', 'CVE-2025-0436', 'CVE-2019-13736', 'CVE-2015-8664',
                         'CVE-2022-4181', 'CVE-2015-1290', 'CVE-2024-7981']

print(cves_impacting_chrome[3])


# List Iteration Using For Loop
for item in cves_impacting_chrome:
    print(item)


# For Loop with Counter
cve_count = 0

for item in cves_impacting_chrome:
    cve_count += 1

print(cve_count)


# Nested Loop
cves_impacting_chrome = [['CVE-2022-4440', 'Network', 'Low', 'None'],
                         ['CVE-2025-0438', 'Network', 'Low', 'None'],
                         ['CVE-2024-8636', 'Network', 'Low', 'None'],
                         ['CVE-2022-0801', 'Network', 'Low', 'None'],
                         ['CVE-2019-5814', 'Network', 'Medium', 'None'],
                         ['CVE-2025-0436', 'Network', 'Low', 'None'],
                         ['CVE-2019-13736', 'Network', 'Medium', 'None'],
                         ['CVE-2015-8664', 'Network', 'Low', 'None'],
                         ['CVE-2022-4181', 'Network', 'Low', 'None'],
                         ['CVE-2015-1290', 'Network', 'Medium', 'None'],
                         ['CVE-2024-7981', 'Network', 'Low', 'None']]

for cve in cves_impacting_chrome:
    print(cve)
    for item in cve:
        print(item)


# Appending Items to Lists
print(cves_impacting_chrome)

new_cve_impacting_chrome = ['CVE-2017-5064', 'Network', 'Medium', 'None']
cves_impacting_chrome.append(new_cve_impacting_chrome)

print(cves_impacting_chrome)


# Removing Items from Lists
cves_impacting_chrome.remove(['CVE-2015-8664', 'Network', 'Low', 'None'])
print(cves_impacting_chrome)

cves_impacting_chrome.pop(3)
print(cves_impacting_chrome)
