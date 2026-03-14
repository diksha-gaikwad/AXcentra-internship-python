text = input("Enter a sentence: ")
words = text.split()

word_count = {}

for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
