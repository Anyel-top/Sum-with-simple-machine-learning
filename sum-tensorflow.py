import tensorflow as tf
import numpy as np
# Generate data for training
# 10,000 examples of addition of two random numbers between 0 and 100 are generated
data = np.random.randint(0, 100, (10000, 2))
labels = np.sum(data, axis=1) # Make the sum

# Create and compile the model
model = tf.keras.Sequential([ #model sequential
    tf.keras.layers.Dense(32, input_shape=(2,), activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error') #function tensorflow

model.fit(data, labels, epochs=10, batch_size=32)

# save model
model.save("modelo_suma.h5")
print("Modelo de suma creado correctamente")
#test_data = np.array([[30, 70], [80, 20], [10, 90]])  # Example sum
#predictions = model.predict(test_data)
#for i in range(len(test_data)):
    #print(f"Predicción para {test_data[i]}: {predictions[i][0]}")
