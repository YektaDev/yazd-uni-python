# Files

# File Modes:
# r -> Open a file for reading.
# w -> Write or create a file.
# x -> Only create if it does not exist.
# a -> Open for appending.
# t -> Open in text mode (default).
# b -> Open in binary mode.
# + -> Open for updating (read + write).

# Opening a file
f = open("test.txt", mode="w", encoding="utf-8")

# Closing a file
# Close with .close()
f = open("test.txt", mode="r", encoding="utf-8")
f.close()
# Close with `with`
with open("test.txt", mode="r", encoding="utf-8") as f:
    pass
# Close with `try` and `finally`
try:
    f = open("test.txt", mode="r", encoding="utf-8")
    # Perform file operations
finally:
    f.close()

# Writing to Files
# Writing a string or sequence of bytes (for binary files) to a file is done with the `write()` method.
with open("test.txt", mode="w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World.")

# Reading Files
# These are various methods available for this purpose.
# 1. read([size = len(file)])
with open("test.txt", mode="w", encoding="utf-8") as f:
    f.write('This is first line\n')
    f.write('Second line\n')
    f.write('Third line')
with open("test.txt", mode="r", encoding="utf-8") as f:
    print(f.read(4))
    print(f.tell())
    f.seek(0)
    print(f.read())

# 2. `for` loop
with open("test.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line, end='')

# 3. `readline()`
with open("test.txt", mode="r", encoding="utf-8") as f:
    print(f.readline(), end='')
    print(f.readline(), end='')
    print(f.readline())

# 4. `readlines()`
with open("test.txt", mode="r", encoding="utf-8") as f:
    print(f.readlines())
    f.seek(0)
    print(*f.readlines())

# File Methods
# 1. `flush()`
# Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects. This is called
# automatically when the file is closed. It may be useful to call this method before closing a file if the data in the
# buffer is meant to be immediately available to another file processing program.
with open("test.txt", mode="w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World.")
    f.flush()
# 2. readable()
# Return True if the file was opened in a read mode.

# 3. truncate([size])
# Truncate the file's size. If the optional size argument is present, the file is truncated to (at most) that size.

with open("test.txt", mode="w", encoding="utf-8") as f:
    f.write('This is first line\n')
    f.write('Second line\n')
    f.write('Third line')
    # print(f.read())
with open("test.txt", mode="r+", encoding="utf-8") as f:
    print(f.read())
with open("test.txt", mode="r+", encoding="utf-8") as f:
    f.truncate(13)
    f.seek(0)
    print(f.read())

# 4. writable()
# Return True if the file stream can be written to.

# 5. writelines(lines)
# Write a list of lines to the file. Note, the sequence can be any iterable object producing strings, typically a list
# of strings. This is equivalent to calling write() for each element.

# 6. seek(offset[, whence])
# The position is computed from adding offset to a reference pint; the reference point is selected by the whence
# argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses
# the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file
# as the reference point.
