# Tuple Iteration Using While Loop
cves_impacting_chrome = ('CVE-2022-4440', 'CVE-2025-0438', 'CVE-2024-8636', 'CVE-2022-0801', 'CVE-2019-5814',
                         'CVE-2025-0436', 'CVE-2019-13736', 'CVE-2015-8664', 'CVE-2022-4181', 'CVE-2015-1290',
                         'CVE-2024-7981')

number_of_cves = len(cves_impacting_chrome)
print(number_of_cves)

count = 0

while count < number_of_cves:
    print(cves_impacting_chrome[count])
    count += 1


# While Loops and File Handling
with open('daily_cve_file.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
