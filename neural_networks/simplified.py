import numpy as np

weights_input_to_hidden_1 = [0.25, 0.25, 0]
weights_input_to_hidden_2 = [0.5, -0.4, 0.9]
weights_hidden_to_output = np.array([-1, 1])

def activation_function(x):
    if x >= 0.5:
        return 1
    else:
        return 0


def predict(inputs):
    weights_input_to_hidden = np.array([weights_input_to_hidden_1, weights_input_to_hidden_2])

    hidden_input = np.dot(weights_input_to_hidden, inputs)
    print("Hidden input: " + str(hidden_input))

    hidden_output = np.array([activation_function(x) for x in hidden_input])
    print("Hidden output: " + str(hidden_output))

    output = np.dot(weights_hidden_to_output, hidden_output)
    print("Output: " + str(output))

    return activation_function(output) == 1


result = predict(np.array([0, 1, 0]))
print("Result: " + str(result))
