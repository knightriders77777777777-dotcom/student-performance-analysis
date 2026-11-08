import pandas as pd
import matplotlib.pyplot as plt

# Student marks data
data = {
    "Student": ["Arun", "Bala", "Kumar", "Ravi", "Siva"],
    "Marks": [85, 65, 92, 45, 75]
}

df = pd.DataFrame(data)

# Display student marks
print("STUDENT PERFORMANCE ANALYSIS")
print(df)

# Calculate average
average = df["Marks"].mean()
print("\nAverage Marks:", average)

# Find highest marks
highest = df["Marks"].max()
print("Highest Marks:", highest)

# Pass or fail
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 50 else "Fail"
)

print("\nStudent Results:")
print(df)

# Create graph
plt.bar(df["Student"], df["Marks"])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()