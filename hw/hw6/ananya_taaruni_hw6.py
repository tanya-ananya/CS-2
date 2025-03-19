import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('car_info.csv')
print(df.shape)

japanese_v6_cars = df[(df['origin'] == 'japan') & (df['cylinders'] == 6)]
print(japanese_v6_cars['name'])
missing_horsepower_cars = df[df['horsepower'].isna()]
print(missing_horsepower_cars['name'])
cars_with_high_mpg = df[df['mpg'] >= 20]
print(len(cars_with_high_mpg))
car_with_highest_mpg = df.loc[df['mpg'].idxmax()]
print(car_with_highest_mpg['name'])

max_weight = df['weight'].max()
min_weight = df['weight'].min()
avg_weight = round(df['weight'].mean(), 2)
print(f"Max weight: {max_weight}, Min weight: {min_weight}, Avg weight: {avg_weight}")

df_cleaned = df.dropna()
print(df_cleaned.shape)


country_counts = df['origin'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Cars Manufactured in Different Countries')
plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Scatter plot for MPG vs Weight
ax1.scatter(df['weight'], df['mpg'], color='blue', label='MPG vs Weight')
ax1.set_xlabel('Weight')
ax1.set_ylabel('MPG')
ax1.legend()
ax1.set_title('Scatter Plot of MPG vs Weight')

# Line plot for MPG vs Displacement
ax2.plot(df['displacement'], df['mpg'], color='green', label='MPG vs Displacement')
ax2.set_xlabel('Displacement')
ax2.set_ylabel('MPG')
ax2.legend()
ax2.set_title('Line Plot of MPG vs Displacement')

plt.tight_layout()
plt.show()