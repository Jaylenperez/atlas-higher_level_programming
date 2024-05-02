#!/usr/bin/python3

# Print all lowercase letters except 'q' and 'e'
print("".join("{}" for _ in range(ord('a'), ord('z')+1) if chr(_) not in ['q', 'e']).format(*[chr(_) for _ in range(ord('a'), ord('z')+1) if chr(_) not in ['q', 'e']]))
