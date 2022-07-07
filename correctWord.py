# from telegram import U
from uzwords import words
from difflib import get_close_matches

def checkWord(word, words=words):
    word = word.lower()
    match = set(get_close_matches(word, words))
    available = False 

    if word in match:
        available = True
        match = word
    elif 'х' in word:
        word = word.replace('х','ҳ')
        match.update(get_close_matches(word,words))
    elif 'ҳ' in word:
        word = word.replace('ҳ','х')
        match.update(get_close_matches(word,words))

    return {'available': available, 'matches': match}
if __name__ == '__main__':
    print(checkWord("ҳато"))
    print(checkWord("тариҳ"))
    print(checkWord("хато"))
    print(checkWord("олма"))
    print(checkWord("ҳат"))
    print(checkWord("ҳайт"))





# my_word = "эслатма"
# print(checkWords(my_word))