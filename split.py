import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('cs-training.csv', index_col = 0)

train, test2 = train_test_split(data, test_size=0.3)

test2.to_csv("test2.csv")
train.to_csv("train.csv")   