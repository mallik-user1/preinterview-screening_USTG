import re

def check_password_validity(input_passwords):
    valid_passwords = []
    password_list = input_passwords

    for password in password_list:
        if (6 <= len(password) <= 12 and
                re.search("[a-z]", password) and
                re.search("[0-9]", password) and
                re.search("[A-Z]", password) and
                re.search("[$#@]", password)):
            valid_passwords.append(password)

    print(','.join(valid_passwords))

input_passwords = ["asqwr1234@1","aF145#","2w3E*","2We3345"]
check_password_validity(input_passwords)
