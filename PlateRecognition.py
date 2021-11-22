import cv2 as cv
import pytesseract as tess
from lib.lib_tess import diminuir


iaPlaca = cv.CascadeClassifier(".cascades/Haarcascade_plate.xml") #IA DA PLACA
ipcam = "http://192.168.0.103:4747/mjpegfeed"
imagem = cv.imread("testeplaca.jpg")
#camera = cv.VideoCapture(ipcam)
camera = cv.VideoCapture("TesteCasa2.mp4")
listaPlacasAuth = ['IXM0E64', 'IUC0816'] #PLACAS AUTORIZADAS
config_tesseract = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNPQRSTUVXYZ0123456789  --psm 6 --tessdata-dir tessdata' #PARÂMETROS TESSERACT PSM6 MELHOR MÉTODO PARA RECONHECER OS CARACTERS


while True:
    _, frame = camera.read()
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    placa = iaPlaca.detectMultiScale(frame, 1.2, 5) #RECEBE AS COORDENADAS DE ONDE ESTÁ A PLACA
    
    for(x, y, w, h) in placa:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
#              ***PRE PROCESSAMENTO DA IMAGEM***        
        placa_rgb = frame[y+15:(y+h)-15, x+40:(x+w)-40]
        placaResize = cv.resize(placa_rgb, None, fx=4,fy=4, interpolation=cv.INTER_CUBIC)
        placaCinza = cv.cvtColor(placaResize,cv.COLOR_BGR2GRAY)
        _, placaBin = cv.threshold(placaCinza,130, 255, cv.THRESH_BINARY)
#               ***FIM DO PRE PROCESSAMENTO DA IMAGEM***
        texto = tess.image_to_string(placaBin, lang='eng', config=config_tesseract)#DESCOBRE OS CARACTERES
        textoProcess = diminuir(texto)
#               ***AUTENTICAÇÃO DA PLACA***
        if textoProcess in listaPlacasAuth:
            with open("log/log.log", "a") as arquivo: #REGISTRA NO ARQUIVO DE LOG
                arquivo.write(textoProcess+ " LIBERADA\n")
        

    cv.imshow("camera", frame)
    #cv.imshow("cameraR", placaResize)
    #cv.imshow("cameraB", placaBin)
    key = cv.waitKey(60)
    if key == 27:
        break
cv.destroyAllWindows()
camera.release()