#!/usr/bin/env python

with open('0000 - challenge3.txt', 'rb') as f:
    encrypted = f.read()

print(encrypted)

def distance_between(letter1, letter2):
    letter1_offset = encrypted.find(letter1)
    letter2_offset = encrypted.find(letter2)
    distance = letter2_offset - letter1_offset
    return distance if distance > 0 else len(encrypted) - letter1_offset + letter2_offset

print(f"Distance between F and L: {distance_between(b'F', b'L')}")
print(f"Distance between L and A: {distance_between(b'F', b'A')}")
print(f"Distance between f and G: {distance_between(b'F', b'G')}")
print(f"Distance between F and : {distance_between(b'Fz', b'{')}")
print(f"Length = {len(encrypted)}")