import json
import numpy as np

def compare_outputs(file1, file2):
    with open(file1, 'r') as json_file:
        file1_json = json.load(json_file)
        
    with open(file2, 'r') as json_file:
        file2_json = json.load(json_file)
    
    for key in dict.keys(file1_json):
        compare_vals(key, file1_json[key], file2_json[key])

def compare_vals(key, a, b):
    for i in range(len(a)):
        _a = np.array(a[i])
        _b = np.array(b[i])
        print('{0}[{1}]: different values = {2}, average difference = {3}'.\
              format(key, i,
                     np.sum(_a != _b),
                     np.sum(np.abs(_a - _b)) / np.size(_a)
        ))

if __name__ == '__main__':
    print('*' * 10, 'tf.Keras Python vs tfjs Node', '*' * 10)
    compare_outputs('keras_model_python.json', 'keras_model_tfjs_node.json')
    
    print('')

    print('*' * 10, 'tf.Keras Python vs tfjs Browser', '*' * 10)
    compare_outputs('keras_model_python.json', 'keras_model_tfjs_browser.json')




