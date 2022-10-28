import cv2
import pytesseract

def recognizeImg(pathImg):
    # Lendo e exibindo a imagem
    img = cv2.imread(pathImg)
    # cv2.imshow("Imagem", img)
    # cv2.waitKey(1)

    # Caminho onde foi instalado o PYTESSERACT(sem isso seu código dará um erro)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\Tesseract.exe"

    # Reconhecendo a imagem e retornando em string o reconhecimento da imagem
    return pytesseract.image_to_string(img, lang="eng", config="--oem 0 --psm 10 -c tessedit_char_blacklist=0123456789").strip()