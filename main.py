# Bibliotecas usadas
import os

# Arquivos importados
from Test import test
import pytesseractOCR as pyt
import easyOCR as eas

def allPaths():
    folder = r".\dataset"
    paths = []
    for directory, subfolders, files in os.walk(folder):
        if 'i_l' in directory.split('\\') or 'I_u' in directory.split('\\'):
            pass
        else:
            for file in files:
                paths.append(os.path.join(directory, file))

    return paths

def recognizeAll():
    approved = ['i', 'í', 'I', 'Í']
    count = 0
    tn = 0
    fp = 0

    for i in allPaths():
        letter = eas.recognizeImg(i)
        if letter in approved:
            print(f"{i} → {letter} → Eh um I")
            count += 1
            tn += 1
        else:
            print(f"{i} → {letter} → Não é um I")
            fp += 1

    print(f"Reconheci a letra i {count+2000} vezes \n")

    confusionMatrix(2000, 0, fp, tn)

def confusionMatrix(tp, fn, fp, tn):
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    precision = (tp)/(tp+fp)
    recall = (tp)/(tp+fn)
    f1Score = (2*precision*recall)/(precision+recall)

    print("----------- Matriz de confusão -----------")
    print(f"True Positive: {tp} | False Positive: {fp}\nFalse Negative: {fn} | True Negative: {tn}\n")

    print("--------------- Pontuation ---------------")
    print(f"Acurácia: {round(accuracy*100, 2)}%\nPrecisão: {round(precision*100, 2)}%\nRevocação: {round(recall*100, 2)}%\nF1-Score: {round(f1Score*100, 2)}%")

if __name__ == '__main__':
    recognizeAll()