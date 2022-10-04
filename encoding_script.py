import hashlib
import pandas as pd

dataset = pd.read_csv('value_file.csv')
values = dataset['value']
lst = []

for value in values:
    hash_object = hashlib.sha256(value.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    lst.append(hex_dig)

fin_dataframe = dataset.assign(encoded = lst)
fin_dataframe.to_csv('encoded_file.csv', index=False)