# Sum Model with TensorFlow

This is a simple script that creates a model using TensorFlow to perform addition of two numbers. Here's a brief explanation of the code:

## Explanation

1. **Data Generation**: The script first generates 10,000 examples of addition of two random numbers between 0 and 100.

2. **Model Creation**: A Sequential model is created using TensorFlow's Keras API. The model has two layers - a Dense layer with 32 neurons and ReLU activation function, and another Dense layer with a single neuron.

3. **Model Compilation**: The model is compiled with the Adam optimizer and Mean Squared Error as the loss function.

4. **Model Training**: The model is trained on the generated data for 10 epochs with a batch size of 32.

5. **Model Saving**: The trained model is saved to a file named "modelo_suma.h5".

6. **Model Testing**: The model can be tested by uncommenting the last few lines of the script. This will generate predictions for the sum of the numbers in the test_data array.

Please note that this is a simple model and might not give accurate results for all inputs. It's always recommended to use a larger dataset and fine-tune the model for better performance.
