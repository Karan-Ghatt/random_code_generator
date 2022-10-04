import random
import string
import pandas as pd

lst = []

for i in range(100000):
    # get random string of length 8 without repeating letters
    source = string.ascii_uppercase + string.digits
    result_str = ''.join(random.sample(source, 8))
    if result_str not in lst:
        lst.append(result_str)
    else:
        pass


df = pd.DataFrame (lst, columns = ['value'])
df.to_csv('value_file.csv', index=False)