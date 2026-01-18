# input()
users_cvss_score = input('Please enter a CVSS score between 0.0 and 10.0: ')


# Escape Characters
print('NVD defines this vulnerability with a 'Critical' severity rating.')

print('NVD defines this vulnerability with a \'Critical\' severity rating.')


# User Input - Example 1
cvss_score = input('Please enter a CVSS score between 0.0 and 10.0: ')
print('The CVSS score entered is: ', cvss_score)
print(type(cvss_score))


# User Input - Example 2
cvss_score = input('Please enter a CVSS score between 0.0 and 10.0: ')
print('The CVSS score entered is: ', cvss_score)
print(type(cvss_score))
try:
    cvss_score = float(cvss_score)
    print('The CVSS score entered is: ', cvss_score)
    print(type(cvss_score))
except ValueError:
    print('Whoops!  You failed to enter a number.')


# User Input - Example 3
cvss_score = input('Please enter a CVSS score between 0.0 and 10.0: ')
print('The CVSS score entered is: ', cvss_score)
print(type(cvss_score))
try:
    cvss_score = float(cvss_score)
    print('The CVSS score entered is: ', cvss_score)
    print(type(cvss_score))
    if 0.0 <= cvss_score <= 10.0:
        print('\n')
        print('Woo-hoo! This is a valid CVSS score!')
    else:
        print('\n')
        print('Nope!  The score provided does not conform to the CVSS scoring system.')
except ValueError:
    print('\n')
    print('Whoops!  You failed to enter a numeric value of any kind.')
