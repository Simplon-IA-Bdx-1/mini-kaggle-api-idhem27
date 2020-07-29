import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv("train.csv")
print(train.head())
monthly_income_mean = train["MonthlyIncome"].mean()
train = train.fillna({"MonthlyIncome" : monthly_income_mean, "NumberOfDependents": 1})

y = train['SeriousDlqin2yrs']
print(y.head())
X = train.drop('SeriousDlqin2yrs', axis=1)
print(X.head())

model = LogisticRegression(max_iter=200).fit(X,y)

test2 = pd.read_csv("test2.csv")
monthly_income_mean_test = test2["MonthlyIncome"].mean()
test2 = test2.fillna({"MonthlyIncome" : monthly_income_mean_test, "NumberOfDependents": 1})

test2_y = test2['SeriousDlqin2yrs']
test2_X = test2.drop("SeriousDlqin2yrs", axis=1)

test2_predictions = model.predict(test2_X)
pd.DataFrame({"prediction":test2_predictions}).to_csv("test2-predictions.csv")
