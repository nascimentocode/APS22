import time
import cv2
import pytesseract
import os
from sklearn.neighbors import KNeighborsClassifier

def confusionMatrix(database):
    tp = 0
    fn = 0
    fp = 0
    tn = 0

    for i in database:
        if i[0] == 'i_l' or i[0] == 'I_u':
            if i[2] == 0:
                tp+=1
            else:
                fn+=1
        else:
            if i[2] == 0:
                tn+=1
            else:
                fp+=1

    accuracy = (tp+tn)/(tp+tn+fp+fn)
    precision = (tp)/(tp+fp)
    recall = (tp)/(tp+fn)
    f1Score = (2*precision*recall)/(precision+recall)

    print("----------Matrix de confusão----------")
    print(f"True Positive: {tp} | False Positive: {fp}\nFalse Negative: {fn} | True Negative: {tn}")

    print("--------------Pontuation--------------")
    print(f"Acurácia: {int(accuracy)}%\nPrecisão: {int(precision)}%\nRevocação: {int(recall)}%\nF1-Score: {int(f1Score)}%")

def showDataBase(database):
    print("Pasta | Arquivo | Eh a letra I")
    for i in database:
        print(f"{i[0]}   | {i[1]}   | {i[2]}")

def recognizeAll():
    start = time.process_time()
    approved = ['i', 'í', 'I', 'Í']
    database = []
    count = 0
    for i in allPaths():
        letter = recognizeImg(i)
        if letter in approved:
            print(f"{i} → {letter} → Eh um I")
            database.append([i.split('\\')[2], i.split('\\')[4].split('_')[2].replace('.png', ''), 0])
            count += 1
        else:
            print(f"{i} → {letter} → Não é um I")
            database.append([i.split('\\')[2], i.split('\\')[4].split('_')[2].replace('.png', ''), 1])

    print(f"Reconheci a letra i {count} vezes \n")

    showDataBase(database)
    end = time.process_time()
    print(f"\nTempo de execução: {end - start}\n")

    confusionMatrix(database)

def allPaths():
    folder = r".\testDataset"
    paths = []
    for directory, subfolders, files in os.walk(folder):
        for file in files:
            paths.append(os.path.join(directory, file))

    return paths

def recognizeImg(pathImg):
    # Lendo e exibindo a imagem
    img = cv2.imread(pathImg)
    # cv2.imshow("Imagem", img)
    # cv2.waitKey(1)

    # Caminho onde foi instalado o PYTESSERACT(sem isso seu código dará um erro)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\Tesseract.exe"

    # Reconhecendo a imagem e retornando em string o reconhecimento da imagem
    return pytesseract.image_to_string(img, lang="eng", config="--oem 0 --psm 10 -c tessedit_char_blacklist=0123456789").strip()

def main():
    recognizeAll()