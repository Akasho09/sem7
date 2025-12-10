import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model("best_model_2.h5")

print("✅ Model loaded successfully!")

# Example input (change based on your model)
sample_input = np.random.rand(1, 224, 224, 3)

prediction = model.predict(sample_input)
print("Prediction:", prediction)

