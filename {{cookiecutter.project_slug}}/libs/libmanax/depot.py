import string
import random

def newid(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


if __name__ == "__main__":
    print(newid(12))
