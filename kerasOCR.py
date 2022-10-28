import keras_ocr

def recognizeImg(pathImg):
    pipeline = keras_ocr.pipeline.Pipeline()

    return pipeline.recognize([pathImg])