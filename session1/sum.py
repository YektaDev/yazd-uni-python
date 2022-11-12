def sum_digits(num):
    sum_of_digits = 0
    while num:
        sum_of_digits += num % 10
        num //= 10
    return sum_of_digits


number = int(input())
while number > 9:
    number = sum_digits(number)
print(number)
