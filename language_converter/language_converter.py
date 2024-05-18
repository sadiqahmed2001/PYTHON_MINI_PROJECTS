from googletrans import Translator

def translate_text(user_input, dest_lang):
    translator = Translator()
    translation = translator.translate(user_input, dest=dest_lang)
    return translation.text

user_input = input("Enter the text you want to translate: ")
print("Original text:", user_input)

supported_languages = {
    "arabic": "ar", "german": "de", "french": "fr", "chinese": "zh-CN",
    "czech": "cs", "hindi": "hi", "japanese": "ja", "korean": "ko",
    "luxembourgish": "lb", "macedonian": "mk", "marathi": "mr", "telugu": "te",
    "kannada": "kn", "bengali": "bn", "bhojpuri": "bho", "russian": "ru",
    "tamil": "ta", "turkish": "tr", "urdu": "ur"
}

lang_convert = input("Enter the language to which you want to translate: ").lower()

if lang_convert in supported_languages:
    translation = translate_text(user_input, supported_languages[lang_convert])
    print(f"Translated text: {translation}")
else:
    print("Sorry, this language is not supported. Please choose from the following supported languages:")
    for lang in supported_languages:
        print(lang.capitalize())