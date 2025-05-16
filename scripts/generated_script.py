Certainly! Here's a Python script that generates a random password of a specified length using letters, numbers, and special characters:

```python
import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

password_length = 12
random_password = generate_password(password_length)
print(random_password)
```

This script defines a function `generate_password` that takes a parameter `length` specifying the length of the password to generate. The function creates a password by randomly selecting characters from letters (both uppercase and lowercase), digits, and punctuation. The generated password is then printed to the console.