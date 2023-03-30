import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv('data.csv')
# print(data)

X = data.iloc[:, :-1]  # Select all columns except the last one
y = data.iloc[:, -1]  # Select only the last column


encoder = LabelEncoder()
y = encoder.fit_transform(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)
# joblib.dump(clf, 'TA_score_classifier.joblib')



# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print('Accuracy:', accuracy)


# new_TA_features = [[3, 3, 2, 2, 2]]  # Example feature values for a new TA
# predicted_score = clf.predict(new_TA_features)
# print('Predicted score:', encoder.inverse_transform(predicted_score))


clf = joblib.load('TA_score_classifier.joblib') 

new_TA_features = [2,23,3,2,38]  # Example feature values for a new TA
new_TA_features = [new_TA_features]  # Reshape into a 2D array
predicted_score = clf.predict(new_TA_features)
predicted_label = encoder.inverse_transform(predicted_score)
print('Predicted score:', predicted_label)
