import pandas as pd
import sklearn.model_selection as ms
import sklearn.linear_model as lm

genres = ['pop', 'r-n-b', 'k-pop', 'hip-hop', 'classical', 'indie', 'country']


def predict_genre(predict_matrix):
    # Training and Validating a Linear Regression Model
    df = pd.read_csv(r'data-set.csv', encoding="ISO-8859-1")

    # Split into training and validating data set
    x, y = df.iloc[:, :-1], df.iloc[:, -1]
    x_train, x_test, y_train, y_test = ms.train_test_split(x, y, test_size=0.25, random_state=42)

    # Linear regression to train model
    regression = lm.LinearRegression()
    regression.fit(x_train, y_train)
    regression.score(x_test, y_test)

    # Predict with new values
    predicted_genres = regression.predict(predict_matrix)

    return predicted_genres
