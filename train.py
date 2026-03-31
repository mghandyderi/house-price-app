import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# تحميل البيانات
data = pd.read_csv("data/house_data.csv")

X = data[['Area', 'Rooms', 'Location']]
y = data['Price']

# تدريب الموديل
model = LinearRegression()
model.fit(X, y)

# حفظ الموديل
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")