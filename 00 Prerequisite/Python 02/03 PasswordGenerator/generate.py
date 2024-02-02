import random
import string

t = string.ascii_letters + string.digits
password = ''.join(random.sample(t+t+t, 24))
print(password)