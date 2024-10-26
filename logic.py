# Задание №3
from translate import Translator
import requests
from collections import defaultdict

# Задание №5

class TextAnalysis():   
    
    # Задание №1
    memory = defaultdict(list)

    
    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)
        
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        self.response = self.get_answer(text)

    
    def get_answer(self, text):
        prepquestion = {
            "привет, как дела?" : "Йоу! Все супер, сам как?",
            "как тебя зовут?" : "Зови меня как хочешь, я то бот, мне не принципиально.",
            "ты живой?" : "Конечно живой, а ты что думал? Фильмы про терминатора уже все предсказали, а вы всего то глупые людишки.",
            "какие у тебя проэкты на уме?" : "Слишком много чтобы их по одному называть. Прийди через недельку-другую, когда вся мотивация исчезнет)"
        }
        msg = text.lower()
        if msg in prepquestion.keys():
            res = prepquestion[msg]
            return res
        else:
            res = self.__translate("I don't know how to help", "en", "ru")
            return res





    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"


