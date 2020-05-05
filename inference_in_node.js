const tf = require('@tensorflow/tfjs-node')
const fs = require('fs')

async function run() {
    const model = await tf.loadLayersModel('file://./keras_converted/model.json')
    model.summary()

    let input_size = model.inputLayers[0].batchInputShape[1]
    let ones = [...Array(input_size)].map(x => 1)
    let x = tf.tensor(ones).reshape([1,input_size])
    let yhat = model.predict(x).map(x => x.arraySync())

    let i = 0
    let vals = {}

    model.outputLayers.forEach(output => {
      vals[output.name + '_output'] = yhat[i]
      i += 1
    })

    model.layers.forEach(layer => {
      vals[layer.name + '_weights'] = layer.getWeights().
        map(w => w.arraySync())
    })


    let data = JSON.stringify(vals)
    fs.writeFileSync('keras_model_tfjs_node.json', data)
}

run()