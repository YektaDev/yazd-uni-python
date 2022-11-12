import re


def is_password_strong(pw):
    """
    Checks if a password is strong.
    :param pw:
    :return: True if a password is strong, False otherwise.
    """
    # All conditions by which the password is considered strong
    one_letter_minimum = re.search('[a-zA-Z]', pw)
    one_num_minimum = re.search('[1-9]', pw)
    one_special_minimum = re.search('[^a-zA-Z0-9]', pw)
    enough_length = len(pw) >= 6
    not_all_upper = not pw.isupper()
    not_all_lower = not pw.islower()
    not_all_digit = not pw.isdigit()
    not_repeated_much = not repeated(pw, len(pw) / 3)
    return one_letter_minimum and one_num_minimum and one_special_minimum and enough_length and not_all_upper \
        and not_all_lower and not_all_digit and not_repeated_much


def repeated(string, amount):
    """
    Checks if a string is repeated more than a certain amount.
    :param string: The string to check.
    :param amount: The amount of times the string can be repeated.
    :return: True if the string is repeated more than the amount, False otherwise.
    """
    current = None
    count = 0
    for letter in string:
        if letter == current:
            count += 1
            if count == amount:
                return True
            continue
        count = 1
        current = letter
    return False


print("»»————- Pᥲssᥕord Wᥱᥲkᥒᥱss Chᥱᥴkᥱr ————-««")
password = input("Please enter a password: ")
if is_password_strong(password):
    print("The given password is strong.")
else:
    print("The given password is weak; please consider choosing a stronger one.")
