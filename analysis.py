import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv("student_data.csv")

# Display data
print(data)

# Basic analysis
print("Average Marks:", data["Marks"].mean())
print("Average Study Hours:", data["Study_Hours"].mean())

# Bar Chart
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

# Scatter Plot
plt.scatter(data["Study_Hours"], data["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# Heatmap
correlation = data[["Age", "Study_Hours", "Attendance", "Marks"]].corr()

sns.heatmap(correlation, annot=True)
plt.title("Student Data Heatmap")
plt.show()
