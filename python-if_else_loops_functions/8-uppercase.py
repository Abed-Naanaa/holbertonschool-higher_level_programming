#!/usr/bin/python3

def uppercase(str):
    result = "" #create a empty string ta red li byet7awalo 3a albo
    for c in str:
        if 'a' <= c <= 'z':  # Check if character is lowercase
            result += chr(ord(c) - 32)  # Convert to uppercase
        else:
            result += c  # Keep other characters the same
    print("{}".format(result))  # Print result as required
