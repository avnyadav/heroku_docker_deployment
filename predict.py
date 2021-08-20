import numpy as np
from PIL import Image
import cv2
import tensorflow as tf

class LogoClassification:
    def __init__(self,filename):
        self.filename =filename


    def getPrediction(self):

        model_path = "models/fashion.h5"
        loaded_model = tf.keras.models.load_model(model_path)

        imagename = self.filename
        image = cv2.imread(imagename)

        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((224,224))
        expand_input = np.expand_dims(resize_image,axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255
        preds = loaded_model.predict(input_data)
        result = preds.argmax()
        if result == 0:
            prediction = 'Goggles'
            return [{"image": prediction}]
        elif result == 1:
            prediction = 'Hat'
            return [{"image": prediction}]
        elif result == 2:
            prediction = 'Jacket'
            return [{"image": prediction}]
        elif result == 3:
            prediction = 'Shirt'
            return [{"image": prediction}]
        elif result == 4:
            prediction = 'Shoes'
            return [{"image": prediction}]
        elif result == 5:
            prediction = 'Shorts'
            return [{"image": prediction}]
        elif result == 6:
            prediction = 'T-Shirt'
            return [{"image": prediction}]
        elif result == 7:
            prediction = 'Trouser'
            return [{"image": prediction}]
        elif result == 8:
            prediction = 'Wallet'
            return [{"image": prediction}]
        elif result == 9:
            prediction = 'Watch'
            return [{"image": prediction}]
        else:
            return [{"ERROR": "Please select another image. !!!"}]


        
