import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\charan tej\Desktop\python project\air_quality (2).csv")

# Convert timestamp to datetime
df['last_update'] = pd.to_datetime(df['last_update'])

# Objective 1: Distribution of pollutants across states
pollutant_state_avg = df.groupby(['state', 'pollutant_id'])['pollutant_avg'].mean().reset_index()

# Plotting the boxplot for pollutant levels across different states
plt.figure(figsize=(12, 6))
sns.boxplot(x='state', y='pollutant_avg', data=df)  # Changed to 'state' on the x-axis
plt.title('Distribution of Pollutant Levels Across States')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 2: Top & bottom cities by average pollutant level
city_pollution_avg = df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False)

print("\nTop 5 Polluted Cities:")
print(city_pollution_avg.head().to_string())

print("\nLeast 5 Polluted Cities:")
print(city_pollution_avg.tail().to_string())

# Objective 3: Pollution trend over time (daily)
df_time = df.groupby(df['last_update'].dt.date)['pollutant_avg'].mean()

plt.figure(figsize=(12, 6))
df_time.plot(marker='o', linestyle='-')
plt.title("Daily Average Pollution Level Over Time")
plt.xlabel("Date")
plt.ylabel("Avg Pollution Level")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Objective 4: Geographical scatter plot
plt.figure(figsize=(10, 6))
sc = sns.scatterplot(
    x='longitude',
    y='latitude',
    hue='pollutant_avg',
    data=df,
    palette='coolwarm',
    size='pollutant_avg',
    legend=False
)
plt.colorbar(sc.collections[0], label='Pollutant Average')
plt.title("Geographical Distribution of Pollutant Averages")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()

# Additional Visualization 1: Heatmap of pollution by state & pollutant
heatmap_data = pollutant_state_avg.pivot(index="state", columns="pollutant_id", values="pollutant_avg")

plt.figure(figsize=(14, 10))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5)
plt.title("Heatmap of Average Pollution by State and Pollutant")
plt.xlabel("Pollutant")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# Additional Visualization 2: Monthly pollution trend
df['month'] = df['last_update'].dt.to_period('M')
monthly_avg = df.groupby('month')['pollutant_avg'].mean()

plt.figure(figsize=(12, 6))
monthly_avg.plot(marker='o', linestyle='-')
plt.title("Monthly Average Pollution Level")
plt.xlabel("Month")
plt.ylabel("Average Pollution")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Additional Visualization 3: Pollutant contribution pie chart
pollutant_total = df.groupby('pollutant_id')['pollutant_avg'].sum()

plt.figure(figsize=(8, 8))
pollutant_total.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
plt.title("Pollutant Contribution Share")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Additional Visualization 4: Top 10 polluted states
state_avg = df.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=state_avg.values, y=state_avg.index, hue=state_avg.index, palette='Reds_r', dodge=False)
plt.title("Top 10 Polluted States (Average Level)")
plt.xlabel("Average Pollution")
plt.ylabel("State")
plt.tight_layout()
plt.show()
