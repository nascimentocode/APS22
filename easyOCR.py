import easyocr

def recognizeImg(pathImg):
    reader = easyocr.Reader(['en'], gpu=False)
    textImg = reader.readtext(pathImg)

    if not textImg:
        return ''
    else:
        return textImg[0][1]