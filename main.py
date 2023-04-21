from pysentimiento import create_analyzer

# pip install https://github.com/pysentimiento/pysentimiento.git
# pip install pysentimiento

emotion_analyzer = create_analyzer(task="emotion", lang="es")

while True:
    s = input('>>> ')
    print(emotion_analyzer.predict(s).probas)