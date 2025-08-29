
# from flask import Flask, request, jsonify, render_template
# from cnnClassifier.pipeline.prediction import PredictionPipeline  # your PredictionPipeline class
# import os

# app = Flask(__name__)

# Serve home page
# @app.route("/")
# def home():
#     return render_template("index.html")

# Predict endpoint
# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     if "image" not in data:
#         return jsonify({"error": "No image provided"}), 400

#     import base64
#     from io import BytesIO
#     from PIL import Image
#     import uuid

    # Convert base64 string to image
    # try:
    #     img_data = base64.b64decode(data["image"])
    #     img = Image.open(BytesIO(img_data)).convert("RGB")
    #     img_name = f"temp_{uuid.uuid4().hex}.jpg"
    #     img_path = os.path.join("uploads", img_name)
    #     os.makedirs("uploads", exist_ok=True)
    #     img.save(img_path)

        # Predict
        # pipeline = PredictionPipeline(img_path)
        # result = pipeline.predict()

        # Remove temp file
#         os.remove(img_path)
#         return jsonify(result)

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)





@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')



@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"




@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #for AWS