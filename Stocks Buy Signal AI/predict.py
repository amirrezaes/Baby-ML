from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics  
import pandas as pd


df = pd.read_csv("data.csv", header = 0)

original_headers = list(df.columns.values)
# remove Nan rows
df = df.dropna()
numpy_array = df.to_numpy()

y = df['Buy']
X = df[['Open','High','Low','Close','Adj Close','Volume', 'Topen']]

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3, shuffle=True)



#creating RandomForestClassifier constructor
clf = RandomForestClassifier(n_estimators = 300, n_jobs=-1)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print("ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred))

# Predicting the values for you

inp = input("Enter data: ")
inp = inp.split(',')
inp = [float(i) for i in inp]
inp = [inp]
y_pred = clf.predict(inp)
print(y_pred)