import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
# from __future__ import absolute_import, division, print_function
# TensorFlow and tf.keras

# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation, Conv1D, GlobalMaxPooling1D

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'



combined = pd.read_csv('Combined_News_DJIA.csv')
"""
Date, Label, top1-25 head lines
"""
djia = pd.read_csv('DJIA_table.csv')
"""
DateIn: YYYY-MM-DD format
Open: Opening weighted average stock value in USD
High: All day high in USD
Low: All day low in USD
Close: Closing weighted average stock value in USD
Volume: Number of trades
Adj Close: Adjusted closing prices - adjusted for both dividends and splits - in USD
"""
news = pd.read_csv('RedditNews.csv')
"""
Date, New
"""

train = combined[combined['Date'] <= '2015-01-01']
train_y = train['Label']
train_x = []
for row in range(0,len(train.index)):
    train_x.append(' '.join(str(x) for x in train.iloc[row,2:27]))
test = combined[combined['Date'] >= '2014-12-31']
test_y = test['Label']
test_x = []
for row in range(0,len(test.index)):
    test_x.append(' '.join(str(x) for x in test.iloc[row,2:27]))


advancedvectorizer = TfidfVectorizer(min_df=0.03, max_df=0.97, max_features = 200000, ngram_range = (2, 2))
advancedtrain = advancedvectorizer.fit_transform(train_x)
advancedtest = advancedvectorizer.transform(test_x)

print(advancedtest.shape)
print(advancedtrain.shape)

vectorizer = CountVectorizer()
train_X = vectorizer.fit_transform(train_x)
test_X = vectorizer.transform(test_x)

model = Sequential()
model.add(Dense(64,input_shape=(test_X.shape[1],)))
model.add(Dropout(0.2))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Dropout(0.2))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['acc'])

model.fit(train_X,train_y,batch_size=32,epochs=10,verbose=1,validation_split=0.2)

test_loss, test_acc = model.evaluate(test_X, test_y)

print('Test accuracy with countvectorizer:', test_acc)

predictions = model.predict(test_X)


"""

d = np.arange(10,60,10)
l = list()
for i in d:
    model2 = Sequential()
    model2.add(Dense(i,input_shape=(advancedtrain.shape[1],)))
    model2.add(Dropout(0.2))
    model2.add(Activation('relu'))
    model2.add(Dense(i))
    model2.add(Dropout(0.2))
    model2.add(Activation('relu'))
    model2.add(Dense(1))
    model2.add(Activation('sigmoid'))
    model2.summary()
    model2.compile(loss='binary_crossentropy',
                optimizer='adam',
                metrics=['acc'])
    model2.fit(advancedtrain,train_y,batch_size=32,epochs=3,verbose=1,validation_split=0.2)
    test_loss2, test_acc2 = model2.evaluate(advancedtest, test_y)
    l.append(test_acc2)
    # print('Test accuracy with tfidf:', test_acc2)

print(l)


from sklearn.neural_network import MLPClassifier


learning_rates = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3]
sizes = [(10,), (10,10,), (10,20,), (10, 20, 30,)]
for learning_rate in learning_rates:
    for size in sizes:
      print(f'Learning Rate {learning_rate}, Size {size}')
      mlp = MLPClassifier(hidden_layer_sizes=size, max_iter=10,
                          random_state=1, learning_rate_init=learning_rate)
      mlp.fit(advancedtrain, train_y)
      print("    Training set score: %f" % mlp.score(advancedtrain, train_y))
      print("    Test set score: %f" % mlp.score(advancedtest, test_y))

# Learning Rate 0.01, Size (10, 10)
# Training set score: 0.803849
# Test set score: 0.609499
"""