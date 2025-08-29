# import numpy as np
# import tensorflow as tf
# import os

# class PredictionPipeline:
#     def __init__(self, filename):
#         self.filename = filename

#     def predict(self):
        # Load model
        # model_path = os.path.join("model", "model.h5")
        # if not os.path.exists(model_path):
        #     raise FileNotFoundError(f"Model not found at {model_path}")
        # model = tf.keras.models.load_model(model_path)

        # # Load and preprocess image
        # img_path = self.filename
        # if not os.path.exists(img_path):
        #     raise FileNotFoundError(f"Image not found at {img_path}")
        
        # test_image = tf.keras.utils.load_img(img_path, target_size=(224, 224))
        # test_image = tf.keras.utils.img_to_array(test_image)
        # test_image = np.expand_dims(test_image, axis=0)
        # test_image = test_image / 255.0  # Normalize if your model was trained on normalized images

        # Make prediction
        # result = np.argmax(model.predict(test_image), axis=1)
        # print("Raw prediction output:", result)

        # if result[0] == 1:
        #     prediction = 'Normal'
        # else:
        #     prediction = 'Adenocarcinoma Cancer'

        # return [{"image": prediction}]




# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import os



# class PredictionPipeline:
#     def __init__(self,filename):
#         self.filename =filename


    
#     def predict(self):
#         ## load model
        
#         # model = load_model(os.path.join("artifacts","training", "model.h5"))
#         model = load_model(os.path.join("model", "model.h5"))

#         imagename = self.filename
#         test_image = image.load_img(imagename, target_size = (224,224))
#         test_image = image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis = 0)
#         result = np.argmax(model.predict(test_image), axis=1)
#         print(result)

#         if result[0] == 1:
#             prediction = 'Normal'
#             return [{ "image" : prediction}]
#         else:
#             prediction = 'Adenocarcinoma Cancer'
#             return [{ "image" : prediction}]



import numpy as np
import tensorflow as tf
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        ## load model
        model = tf.keras.models.load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = tf.keras.utils.load_img(imagename, target_size=(224,224))
        test_image = tf.keras.utils.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Normal'
            return [{"image": prediction}]
        else:
            prediction = 'Adenocarcinoma Cancer'
            return [{"image": prediction}]
