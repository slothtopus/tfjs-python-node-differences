import json
import numpy as np

from tensorflow.keras.models import Model, save_model
from tensorflow.keras import layers as L
from tensorflow.keras import backend as K
from tensorflow.keras import initializers as I
import tensorflowjs as tfjs

def build_model(depth, size):
    x = L.Input((size), name = 'input')
    inputs = [x]
    outputs = []
    
    uniform_init = I.RandomUniform(minval=-1, maxval=1, seed=123)
    
    for i in range(depth):
        x = L.Dense(size,
                    dtype = 'float32',
                    kernel_initializer = uniform_init,
                    bias_initializer = uniform_init,
                    name = 'dense_' + str(i))(x)
        
        outputs += [x]
    
    model = Model(inputs=inputs, outputs=outputs)
    return (model, inputs, outputs)

def output_to_json(model, yhat):
    keras_vals = dict()
    
    for i, layer in enumerate(model.layers[1:]):
        keras_vals[layer.name + '_weights'] = [w.tolist() for w in layer.get_weights()]
        keras_vals[layer.name + '_output'] = yhat[i].tolist()

    with open('keras_model_python.json', 'w') as f:
        json.dump(keras_vals, f)


if __name__ == "__main__":
    K.clear_session()

    model, inputs, outputs = build_model(10, 50)
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.summary()

    tfjs.converters.save_keras_model(model, './keras_converted')

    # run the model on a single vector of ones
    yhat = model.predict(np.ones((1,inputs[0].shape[1])))

    output_to_json(model, yhat)
