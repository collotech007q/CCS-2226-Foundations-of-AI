#Name:   Collins Kipkirui
#Reg No: CIT-227-065/2024
#Unit:   Foundations of AI
#Course: Software Engineering

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# (a) Download and load the MNIST dataset
print("Downloading and loading MNIST dataset...")
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocess the data: Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# (b) Build a simple Neural Network to distinguish digits 0 - 9
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)), # Flatten 28x28 images to 1D vectors
    layers.Dense(128, activation='relu'),  # Hidden layer
    layers.Dropout(0.2),                   # Prevent overfitting
    layers.Dense(10, activation='softmax') # Output layer (10 classes for digits 0-9)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
print("\nTraining the model...")
model.fit(x_train, y_train, epochs=3)

# Evaluate the model
print("\nEvaluating on test data:")
test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)
print(f'\nTest Accuracy: {test_acc*100:.2f}%')

# Make a prediction on the first test image
prediction = model.predict(x_test[:1])
predicted_digit = np.argmax(prediction)

# Show the image and the result
plt.imshow(x_test[0], cmap='gray')
plt.title(f"Computer's Guess: {predicted_digit}")
plt.show()

print(f"The neural network identified this digit as: {predicted_digit}")
