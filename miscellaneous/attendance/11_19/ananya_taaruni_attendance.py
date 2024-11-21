import pandas as pd
import numpy as np

# Exercise One
data = {
    'age': np.random.randint(0, 100, size=10),
    'score': np.random.randint(0, 25, size=10)
}
df = pd.DataFrame(data)
tail_value = df.tail()
description = df.describe()
sorted_df = df.sort_values(by='score')

print("Tail value of the dataframe:")
print(tail_value)
print("\nDescription of the dataframe:")
print(description)
print("\nDataframe sorted by score:")
print(sorted_df)

# Exercise Two
df.to_csv('/Users/taaruniananya/Downloads/pd_exer.csv', index=False)
df_from_csv = pd.read_csv('/Users/taaruniananya/Downloads/pd_exer.csv')

print("\nDataframe read from pd_exer.csv:")
print(df_from_csv)

# Exercise Three
new_row = {'age': np.random.randint(0, 100), 'score': np.random.randint(0, 25)}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

companies = ['Google', 'Apple', 'Microsoft']
df.insert(0, 'company', np.random.choice(companies, size=len(df)))

print("\nDataframe after adding a new row and inserting 'company' column:")
print(df)

# Exercise Four
high_score_df = df[df['score'] > 50]
print("\nRows with score greater than 50:")
print(high_score_df)

age_and_score_df = df[(df['age'] > 20) & (df['score'] > 50)]
print("\nRows with age greater than 20 and score greater than 50:")
print(age_and_score_df)

# Exercise Five
grouped_df = df.groupby('company').agg({'age': 'median', 'score': 'mean'})
print("\nGrouped dataframe with median age and mean score:")
print(grouped_df)

# Exercise Six
mean_values = df[['age', 'score']].apply(np.mean)
print("\nMean values for age and score:")
print(mean_values)
