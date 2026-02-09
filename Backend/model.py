import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\placement.csv")

plt.scatter(df['cgpa'],df['package'])
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')

X = df.iloc[:,0:1]
y = df.iloc[:,-1]

y

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)


from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X_train,y_train)

print(lr.predict([[8.5]]))

df.head()


import joblib

# Save model in api folder
joblib.dump(lr, r"C:\Users\hp\OneDrive\Desktop\end to End project\api\package_model.pkl")
print("Model saved in api folder")
