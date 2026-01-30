import hashlib
import random
import string
import sys

def random_string(length=16):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

found = False

for i in range(1000):
    data = random_string()
    hash_value = hashlib.md5(data.encode()).hexdigest()  

    print(f"Attempt {i + 1}: {hash_value}")

    if hash_value.startswith("00"):
        print("\nSuccess! Hash found:", hash_value)
        found = True
        break

if not found:
    print("\nNo hash starting with '00' found after 1000 attempts")
    sys.exit(1)  

sys.exit(0)  
