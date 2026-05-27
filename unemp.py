import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Display first rows
print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove spaces in column names
df.columns = df.columns.str.strip()

print(df.columns)

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# Statistical summary
print(df.describe())

# Histogram
plt.figure(figsize=(8,5))

sns.histplot(
df['Estimated Unemployment Rate (%)'],
bins=20
)

plt.title("Unemployment Distribution")

plt.show()
plt.figure(figsize=(12,6))

sns.barplot(
x='Region',
y='Estimated Unemployment Rate (%)',
data=df
)

plt.xticks(rotation=90)

plt.title("Region Wise Unemployment")

plt.show()
plt.figure(figsize=(7,5))

sns.boxplot(
x='Area',
y='Estimated Unemployment Rate (%)',
data=df
)

plt.title("Urban vs Rural")

plt.show()
covid = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(10,5))

sns.lineplot(
x='Date',
y='Estimated Unemployment Rate (%)',
data=covid
)

plt.xticks(rotation=45)

plt.title("Covid Impact")

plt.show()
df['Month'] = df['Date'].dt.month

monthly = df.groupby(
'Month'
)['Estimated Unemployment Rate (%)'].mean()

print(monthly)

monthly.plot(
kind='line',
marker='o'
)

plt.title("Monthly Trend")

plt.show()