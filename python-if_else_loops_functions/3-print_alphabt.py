#!/usr/bin/python3

# Print all lowercase letters except 'q' and 'e'
print("".join([chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in ['q', 'e']]).format(), end='')
