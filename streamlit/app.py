import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from PIL import Image
 
def main():
    st.title('Image Classifier')
    st.write('Upload any image that you think fits into one of the classes end see if the prediction is correct')

    file = st.file_uploader('Please upload an image', type=['jpg', 'png'])
    if file:
        image = Image.open(file)
        st.image(image, use_column_width=True)

        resized_image = image.resize((224, 224))
        img_array = np.array(resized_image) / 255
        img_array = img_array.reshape(1, 224, 224, 3)

        model = tf.keras.models.load_model('full-image-classification.h5')

        predictions = model.predict(img_array)
        image_classes = ['attire', 'food','misc','decoration']

        fig, ax = plt.subplots()
        y_pos = np.arange(len(image_classes))
        ax.barh(y_pos, predictions[0], align='centre')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(image_classes)
        ax.invert_yaxis()
        ax.set_xlabel('Probability')
        ax.set_title('Image Predicitons')

        st.pyplot(fig)

    else:
        st.text('You have not uploaded an image yet.')




if __name__ == '__main__':
    main()