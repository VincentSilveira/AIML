from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist


import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=128, validation_split=0.2)
model.evaluate(X_test, y_test)

pred = model.predict(X_test)
plt.imshow(X_test[100])
plt.title(f'Predicted { pred[100].argmax()}')
plt.show()