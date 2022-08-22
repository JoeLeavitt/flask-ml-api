from flask import Flask, jsonify, request
import torch

import util
from util import NeuralNetwork

MODEL_PATH = "/app/model/mnist_model.pth"

app = Flask(__name__)

# load model
model = NeuralNetwork()
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()

@app.route("/classify", methods=["POST"])
def classify_digit():
    # read in the file downloaded via CURL
    img = request.files["file"]

    # prepare the image
    img = util.prepare_image(img)

    # use trained model to classify image
    res = model(img)
    res = torch.argmax(res)

    return jsonify({"digit": res.item()})
