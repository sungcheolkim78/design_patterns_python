class EnglishLocalizer(object):
    def localize(self, msg):
        return msg


class KoreanLocalizer(object):
    def __init__(self):
        self.translations = {"car": "차", "bike": "자전거", "cycle": "싸이클"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer(object):
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


def Factory(language: str = "English"):
    localizers = {
        "Korean": KoreanLocalizer,
        "Spanish": SpanishLocalizer,
        "English": EnglishLocalizer,
    }

    return localizers[language]()


if __name__ == "__main__":
    k = Factory("Korean")
    s = Factory("Spanish")
    e = Factory("English")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(k.localize(msg))
        print(s.localize(msg))
        print(e.localize(msg))
