# tfjs-python-node-differences

An example to illustrate the differences between model output in tensorflow run in Python and Node versus tensorflow run in the browser.

This has been tested using tfjs 1.7.4, tensorflow 2.1.0 and Chrome 81.0.4044.129. 

## Setting up

### Python
Create a virtual environment, install the dependencies and activate.

```
virtualenv .
pip install -r requirements.txt
source bin/activate
```

### Node
Do this if you want to run the test in Node as well. Otherwise feel free to skip.

```
npm install
```

## Running the test

### Create and run the model in tf.Keras
Create the model using tf.Keras, run inference against a test vector of ones and save the output to JSON.
This will save the model output as ```keras_model_python.json``` and the tensorflowjs conversion in the ```keras_converted``` folder.

```
python create_keras_model.py
```

### Run the model in Node
Run the same model in Node. The output is saved as ```keras_model_tfjs_node.json```.

```
node inference_in_node.js
```

### Run the model in the browser
To run the model in a browser you'll need to start a http server.

```
python -m http.server
```

Next, navigate to http://0.0.0.0:8000/inference_in_browser.html. This will trigger a download of the model output as ```keras_model_tfjs_browser.json```. Make sure you move this to the current folder before runnning the next step.

### Compare the outputs
Run the Python script to compare the model outputs.

```python compare_outputs.py```

This should give you something like this:

```
********** tf.Keras Python vs tfjs Node **********
dense_0_weights[0]: different values = 0, average difference = 0.0
dense_0_weights[1]: different values = 0, average difference = 0.0
dense_0_output[0]: different values = 0, average difference = 0.0
dense_1_weights[0]: different values = 0, average difference = 0.0
dense_1_weights[1]: different values = 0, average difference = 0.0
dense_1_output[0]: different values = 0, average difference = 0.0
dense_2_weights[0]: different values = 0, average difference = 0.0
dense_2_weights[1]: different values = 0, average difference = 0.0
dense_2_output[0]: different values = 0, average difference = 0.0
dense_3_weights[0]: different values = 0, average difference = 0.0
dense_3_weights[1]: different values = 0, average difference = 0.0
dense_3_output[0]: different values = 0, average difference = 0.0
dense_4_weights[0]: different values = 0, average difference = 0.0
dense_4_weights[1]: different values = 0, average difference = 0.0
dense_4_output[0]: different values = 0, average difference = 0.0
dense_5_weights[0]: different values = 0, average difference = 0.0
dense_5_weights[1]: different values = 0, average difference = 0.0
dense_5_output[0]: different values = 0, average difference = 0.0
dense_6_weights[0]: different values = 0, average difference = 0.0
dense_6_weights[1]: different values = 0, average difference = 0.0
dense_6_output[0]: different values = 0, average difference = 0.0
dense_7_weights[0]: different values = 0, average difference = 0.0
dense_7_weights[1]: different values = 0, average difference = 0.0
dense_7_output[0]: different values = 0, average difference = 0.0
dense_8_weights[0]: different values = 0, average difference = 0.0
dense_8_weights[1]: different values = 0, average difference = 0.0
dense_8_output[0]: different values = 0, average difference = 0.0
dense_9_weights[0]: different values = 0, average difference = 0.0
dense_9_weights[1]: different values = 0, average difference = 0.0
dense_9_output[0]: different values = 0, average difference = 0.0

********** tf.Keras Python vs tfjs Browser **********
dense_0_weights[0]: different values = 0, average difference = 0.0
dense_0_weights[1]: different values = 0, average difference = 0.0
dense_0_output[0]: different values = 0, average difference = 0.0
dense_1_weights[0]: different values = 0, average difference = 0.0
dense_1_weights[1]: different values = 0, average difference = 0.0
dense_1_output[0]: different values = 40, average difference = 1.7833709716796876e-06
dense_2_weights[0]: different values = 0, average difference = 0.0
dense_2_weights[1]: different values = 0, average difference = 0.0
dense_2_output[0]: different values = 43, average difference = 1.2047290802001953e-05
dense_3_weights[0]: different values = 0, average difference = 0.0
dense_3_weights[1]: different values = 0, average difference = 0.0
dense_3_output[0]: different values = 38, average difference = 5.3539276123046876e-05
dense_4_weights[0]: different values = 0, average difference = 0.0
dense_4_weights[1]: different values = 0, average difference = 0.0
dense_4_output[0]: different values = 43, average difference = 0.00024005889892578125
dense_5_weights[0]: different values = 0, average difference = 0.0
dense_5_weights[1]: different values = 0, average difference = 0.0
dense_5_output[0]: different values = 45, average difference = 0.0010586166381835937
dense_6_weights[0]: different values = 0, average difference = 0.0
dense_6_weights[1]: different values = 0, average difference = 0.0
dense_6_output[0]: different values = 46, average difference = 0.00515625
dense_7_weights[0]: different values = 0, average difference = 0.0
dense_7_weights[1]: different values = 0, average difference = 0.0
dense_7_output[0]: different values = 47, average difference = 0.0254345703125
dense_8_weights[0]: different values = 0, average difference = 0.0
dense_8_weights[1]: different values = 0, average difference = 0.0
dense_8_output[0]: different values = 46, average difference = 0.11546875
dense_9_weights[0]: different values = 0, average difference = 0.0
dense_9_weights[1]: different values = 0, average difference = 0.0
dense_9_output[0]: different values = 44, average difference = 0.42203125
```

Running the model in Python and Node produces the same exact output. However, when run in the browser using tfjs, there are small differences the output of each layer, which end up diverging significantly by the end.