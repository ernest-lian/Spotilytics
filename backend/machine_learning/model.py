# Imports
import pandas as pd
import sklearn.model_selection as ms
import sklearn.linear_model as lm

# genres = ['acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass', 'blues',
#           'bossanova', 'brazil', 'breakbeat', 'british', 'cantopop', 'chicago-house', 'children', 'chill', 'classical',
#           'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco',
#           'disney', 'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french',
#           'funk', 'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove', 'grunge', 'guitar', 'happy', 'hard-rock',
#           'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'honky-tonk', 'house', 'idm', 'indian',
#           'indie', 'indie-pop', 'industrial', 'iranian', 'j-dance', 'j-idol', 'j-pop', 'j-rock', 'jazz', 'k-pop',
#           'kids', 'latin', 'latino', 'malay', 'mandopop', 'metal', 'metal-misc', 'metalcore', 'minimal-techno',
#           'movies', 'mpb', 'new-age', 'new-release', 'opera', 'pagode', 'party', 'philippines-opm', 'piano', 'pop',
#           'pop-film', 'post-dubstep', 'power-pop', 'progressive-house', 'psych-rock', 'punk', 'punk-rock', 'r-n-b',
#           'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'rockabilly', 'romance', 'sad',
#           'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul',
#           'soundtracks', 'spanish', 'study', 'summer', 'swedish', 'synth-pop', 'tango', 'techno', 'trance', 'trip-hop',
#           'turkish', 'work-out', 'world-music']

genres = ['pop', 'r-n-b', 'k-pop', 'hip-hop', 'classical', 'indie', 'country']


def predict_genre(predict_matrix):
    # Training and Validating a Linear Regression Model
    df = pd.read_csv(r'testing.csv', encoding="ISO-8859-1")

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