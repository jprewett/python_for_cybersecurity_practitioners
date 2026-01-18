# Function Composition
def calculate_cvss_severity_level(cvss_score):


# Example 1: Function Creation with Scope Demonstration
def report_cvss_score(cvss_score):
    print(cvss_score)

def calculate_severity_level(cvss_score):
    critical = 'This CVSS has a Critical severity rating'
    high = 'This CVSS has a High severity rating'
    medium = 'This CVSS has a Medium severity rating'
    low = 'This CVSS has a Low severity rating'
    information = 'This CVSS has no severity rating'

cvss_score = input('Please enter a CVSS score between 0.0 and 10.0: ')
report_cvss_score()
print(critical)


# Example 2: Void Function
def report_cvss_score(score):
    print(score)

def calculate_severity_level(score):
    if 9.0 <= score <= 10:
        print('This is a Critical severity vulnerability.')
    elif 7.0 <= score <= 8.9:
        print('This is a High severity vulnerability.')
    elif 4.0 <= score <= 6.9:
        print('This is a Medium severity vulnerability.')
    elif 0.1 <= score <= 3.9:
        print('This is a Low severity vulnerability.')
    else:
        print('This vulnerability has no severity.')

cvss_score = input('Please enter a CVSS score between 0.0 and 10.0: ')
# cvss_score = float(cvss_score)
report_cvss_score(cvss_score)
calculate_severity_level(cvss_score)


# Example 3: Fruitful Function
def convert_to_float(score):
    score = float(score)
    return score

def report_cvss_score(score):
    print(score)

def calculate_severity_level(score):
    if 9.0 <= score <= 10:
        print('This is a Critical severity vulnerability.')
    elif 7.0 <= score <= 8.9:
        print('This is a High severity vulnerability.')
    elif 4.0 <= score <= 6.9:
        print('This is a Medium severity vulnerability.')
    elif 0.1 <= score <= 3.9:
        print('This is a Low severity vulnerability.')
    else:
        print('This vulnerability has no severity.')

cvss_score = input('Please enter a CVSS score between 0.0 and 10.0: ')
cvss_score = convert_to_float(cvss_score)
report_cvss_score(cvss_score)
calculate_severity_level(cvss_score)