def count_words(text):
    text = text.lower()

    clean_text = ""
    for char in text:
        if char.isalpha():
            clean_text += char
        else:
            clean_text += ' '

    words = clean_text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
                     