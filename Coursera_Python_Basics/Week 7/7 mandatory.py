# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

x = open('input.txt')
a = x.read()

counter = {}
for word in a.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
