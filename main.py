# Bibliotecas usadas
import time
import os

# Arquivos importados
from Test import test
import pytesseractOCR as pyt
import easyOCR as eas
import kerasOCR as ker

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
    print(f"True Positive: {tp} | False Positive: {fp}\nFalse Negative: {fn} | True Negative: {tn}\n")

    print("--------------Pontuation--------------")
    print(f"Acurácia: {round(accuracy*100, 2)}%\nPrecisão: {round(precision*100, 2)}%\nRevocação: {round(recall*100, 2)}%\nF1-Score: {round(f1Score*100, 2)}%")

def showDataBase(list):
    print("Pasta | Arquivo | Eh a letra I")
    for i in list:
        print(f"{i[0]}   | {i[1]}   | {i[2]}")

def allPaths():
    folder = r".\dataset"
    paths = []
    for directory, subfolders, files in os.walk(folder):
        for file in files:
            paths.append(os.path.join(directory, file))

    return paths

def recognizeAll():
    start = time.process_time()
    approved = ['i', 'í', 'I', 'Í']
    database = []
    count = 0
    for i in allPaths():
        letter = ker.recognizeImg(i)
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

if __name__ == '__main__':
    recognizeAll()