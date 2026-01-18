import datetime


current_date_time = datetime.datetime.now()
print(current_date_time)

vuln_found_date_time = datetime.datetime.fromisoformat('2025-03-11T18:14:46.119Z')
print(vuln_found_date_time)
vuln_found_date_time = vuln_found_date_time.replace(tzinfo=None)
print(vuln_found_date_time)

if vuln_found_date_time < current_date_time - datetime.timedelta(days=15):
    print('This vulnerability is greater than 15 days old')
