# plate-recognition-with-tesseract-OCR
Para o desenvolvimento do código utilizamos como referência um problema já existente, a autenticação de placas de carros em condomínios residenciais.

Utilizamos uma IA treinada que reconhece o formato das placas na imagem.
A IA se encontra em (iaPlaca = cv.CascadeClassifier("_cascades/Haarcascade_plate.xml")

O Tesseract faz o reconhecimento dos caracteres na placa e procura a mesma
combinação na lista de placas autorizadas, se a placa estiver
entre as autorizadas o carro recebe a autorização para entrar.

O Tesseract possui 13 parâmetros para o reconhecimento dos
caracteres, após vários testes o parâmetro 6 foi o que apresentou
melhor resultado e utilizamos no código.

Necessário para rodar o algoritmo:
- Python 3.6 ou superior
- OpenCV
- Baixar e instalar o Programa do Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Instalar a Lib PyTesseract através do comando pip install pytesseract
