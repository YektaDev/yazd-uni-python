txt = "TEMPORARY TEXT"

txt.strip()  # trim
txt.lstrip()  # trim left
txt.rstrip()  # trim right
txt.strip('X')  # trim X

txt.replace('X', 'Y')  # replace X with Y
txt.replace('X', 'Y', 1)  # replace X with Y, only once

txt.split('X')  # split by X
txt.split('X', 1)  # split by X, only once

txt.partition('X')  # split by X, return tuple (left, X, right)

txt.join(',')  # join each character of txt by ,

txt.format('price: {:,}'.format(1234567890))  # format string
"""
Format options:
  {:,} - comma separated
  {:>10} - right aligned, 10 characters
  {:<10} - left aligned, 10 characters
  {:^10} - center aligned, 10 characters
  {:b} - binary
  {:o} - octal
  {:x} - hexadecimal
  {:X} - hexadecimal, uppercase
  {:e} - scientific notation
  {:E} - scientific notation, uppercase
  {:f} - fixed point
  {:F} - fixed point, uppercase
  {:g} - general format
  {:G} - general format, uppercase
"""

txt.isalpha()  # check if all characters are alphabetic
