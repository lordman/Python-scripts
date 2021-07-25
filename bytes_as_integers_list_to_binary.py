#!/usr/bin/env python3

my_bytes_list = [116, 92, 82, 101, 108, 101, 97, 115, 101, 92, 97, 98, 46, 112, 100, 98, 0]

file = open("file.exe", "wb")    # Write as binary file
my_byte_array = bytearray(my_bytes_list)
file.write(my_byte_array)
file.close
