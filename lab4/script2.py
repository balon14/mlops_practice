import pandas as pd


df = pd.read_csv('datasets/data.csv')


mean_age = df['Age'].mean()


df['Age'].fillna(mean_age, inplace=True)


df.to_csv('datasets/data.csv', index=False)
