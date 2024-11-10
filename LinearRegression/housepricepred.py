#Import libraries:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler



# Load the dataset
df = pd.read_csv('housing.csv')


# Display the first few rows of the dataset
df.head()

# Check for missing values
print(df.isnull().sum())

# Visualize the distribution of house prices
plt.figure(figsize=(10,6))
sns.histplot(df['SalePrice'], kde=True)
plt.title('Distribution of Housing Prices')
plt.show()


# Drop columns with too many missing values
df = df.drop(columns=['Alley', 'PoolQC', 'Fence', 'MiscFeature'])

# Fill missing values for numerical columns with the median
df.fillna(df.median(), inplace=True)

# Encode categorical columns using one-hot encoding
df = pd.get_dummies(df)

# Split the data into features and target variable
X = df.drop(columns=['SalePrice'])
y = df['SalePrice']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Scaling the features: Standardize the features to improve model performance.


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Train a Linear Regression Model: Train the model using Linear Regression.



model = LinearRegression()
model.fit(X_train_scaled, y_train)

#Make Predictions: Use the trained model to predict housing prices.



y_pred = model.predict(X_test_scaled)

#Evaluate the Model: Evaluate the model’s performance using metrics like Mean Absolute Error (MAE) and Mean Squared Error (MSE).


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")

