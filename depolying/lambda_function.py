import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('xception', target_size=(299, 299))



interpreter = tflite.Interpreter(model_path='sign_language_model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']




labels = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9
}


 #url = {'url' : 'https://raw.githubusercontent.com/Olawuwo2000/sign-language/main/img_3455.jpg'}'

def predict(url):
    x = preprocessor.from_url(url)


    interpreter.set_tensor(input_index, x)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)



    return dict(zip(labels, preds[0]))
    
    
    
def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result 
 



