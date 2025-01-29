import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt 
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = models.Sequential([
    layers.Flatten(input_shape = (28, 28)),
    layers.Dense(128, activation = "relu"),
    layers.Dense(10, activation = "soft_max")
])
model.compile(optimizer = "adam",
loss = "sparse_catagorical_crossentropy",
metrics = ["accuracy"])
model.fit(x_train, y_train, epochs = 5)
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"test accuracy:{test_acc}")
prediction = model.predict(x_test)
plt.imshow(x_test[0],cmap = plt.cm.binary)
plt.title(f"predicted: {prediction[0].argmax()}")
plt.show()