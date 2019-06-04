import re
to_be_checked = input("enter your string ")
stripped_to_check = re.sub(r'[^A-Za-z]', '', to_be_checked)
lower_stripped = stripped_to_check.lower()

def palindrome_checker(i):
    if len(i) == 0 or len(i) == 1:
        print("is a palindrome")
        return None
    elif i[0] == i[-1]:
        i = i[1:-1]
        palindrome_checker(i)
    else:
        print("is not a palindrome")
        return None

palindrome_checker(lower_stripped)