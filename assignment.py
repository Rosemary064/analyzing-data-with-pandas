import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset (replace 'your_dataset.csv' with the actual dataset file path)
    df = pd.read_csv('your_dataset.csv')
    print("Dataset loaded successfully!")
    
    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    print(df.head())
    
    # Check for missing values
    print("Missing values in each column:")
    print(df.isnull().sum())
    
    # Check the data types of the columns
    print("Data types of columns:")
    print(df.dtypes)
    
    # Clean the dataset by filling missing values (or drop if preferred)
    df.fillna(df.mean(), inplace=True)
    print("Missing values filled with mean.")
    
except FileNotFoundError:
    print("Error: Dataset file not found.")
except pd.errors.EmptyDataError:
    print("Error: The dataset file is empty.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
# Compute basic statistics of numerical columns
print("Basic statistics of numerical columns:")
print(df.describe())

# Group by a categorical column ('species' as an example) and compute the mean of a numerical column ('sepal_length' as an example)
print("Mean sepal length for each species:")
print(df.groupby('species')['sepal_length'].mean())

# Task 3: Data Visualization
# Line chart showing trends over time (example: sales data)
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['sales'])
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Bar chart showing the comparison of a numerical value across categories (example: average petal length per species)
plt.figure(figsize=(10, 6))
df.groupby('species')['petal_length'].mean().plot(kind='bar')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.xticks(rotation=0)
plt.show()

# Histogram of a numerical column (example: sepal length distribution)
plt.figure(figsize=(10, 6))
df['sepal_length'].hist(bins=20)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to visualize the relationship between two numerical columns (example: sepal length vs petal length)
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal_length'], df['petal_length'])
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()
