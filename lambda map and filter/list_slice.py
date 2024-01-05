word = "abcdefghijklmno"
print(word[::-1]) #reverse string

words = ["Python","Java", "Javascript", "C++"]

reverse_words = list(map(lambda word:word[::-1], words))
print(reverse_words)