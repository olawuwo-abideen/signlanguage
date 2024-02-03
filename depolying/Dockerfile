FROM    public.ecr.aws/lambda/python:3.9.2022.09.27.12

RUN pip install keras-image-helper


RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl

COPY sign_language_model.tflite .

COPY lambda_function.py .

CMD ["lambda_function.lambda_handler"]


