import re
import random


def encode(sentence, separator='\n---weird---\n'):
    original_words = list()
    sentence_letters = list(sentence)
    words = re.finditer(r'\w+', sentence)
    for word in words:
        if len(word.group(0)) > 3:
            original = sentence_letters[word.start() + 1:word.end() - 1]
            check = {letter for letter in original}
            if len(check) > 1:
                changed = original[:]
                while changed == original:
                    random.shuffle(changed)
                sentence_letters[word.start() + 1:word.end() - 1] = changed
                original_words.append(word.group(0))
    return separator + "".join(sentence_letters) + separator + " ".join(sorted(original_words, key=str.casefold))


def decode(sentence, separator='\n---weird---\n'):
    _, text, original_words = sentence.split(separator)
    text_letters = list(text)
    original_words = original_words.split(" ")
    original_words_as_letters = {i: sorted(list(word)) for i, word in enumerate(original_words)}
    words = re.finditer(r'\w+', text)
    for word in words:
        if len(word.group(0)) > 3:
            changed_word = sorted(list(word.group(0)))
            for i, original_word in original_words_as_letters.items():
                if changed_word == original_word:
                    text_letters[word.start():word.end()] = original_words[i]
                    del original_words_as_letters[i]
                    break
    return "".join(text_letters)
