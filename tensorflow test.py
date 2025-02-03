import tensorflow as tf

# Create some example tensors
tensor1 = tf.constant(42)
# tensor2 = tf.constant(3.14159)
tensor3 = tf.constant("TensorFlow")

# Format the tensors into a string
formatted_string = tf.strings.format("Integer: {}, String: {}", (tensor1, tensor3))

# Convert the formatted string tensor to a numpy array and print it
print(formatted_string.numpy().decode('utf-8'))
