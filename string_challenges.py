# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а")) #если регистр иммет значения то делаем count от просто word


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = "аеиоэюя"
count_vowels = 0
for vowel in vowels:
    count_vowels += word.lower().count(vowel)
print(count_vowels)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(" ")+1)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(" ")
for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = len(sentence.split(" "))
print(words)
