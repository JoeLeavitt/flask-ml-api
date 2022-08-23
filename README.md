# flask-ml-api

## Introduction
This project deploys a pre-trained MNIST classifier model to a Flask API endpoint
using Docker. It's meant to emulate a client that sends an image to an endpoint
and a server that returns the prediction for the image. Docker and `curl` should
be installed on your system.

## Setup
You should build the Flask API server so that you can send images to an endpoint later.
```sh
docker build -t mnist_model .
```

After that, run the server locally on port 5000 by running the following command:
```sh
docker run -p 5000:5000 mnist_model
```

## Usage
Finally, you can request predictions from the model by opening another terminal,
navigating to the root of this repository, and running the following `curl` command:
```sh
curl -F 'file=@test_images/0.jpg' localhost:5000/classify
```

You should receive a response that looks like the following example:
```
{"digit": 0}
```

In the `test_images` folder, there are a number of example images that you can use to
test the model. You can also add your own images as test examples; to do so, you modify the file flag to match the desired image:
```sh
curl -F 'file=@test_images/[YOUR_FILENAME]' localhost:5000/classify
```
