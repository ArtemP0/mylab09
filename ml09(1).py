import random as r

words = (input("Введіть слова : ")).split()
words_sorted = tuple(sorted(words))
words_shuffled = tuple(r.sample(words, len(words)))
print(f"1 кортеж : {words_sorted}\n2 кортеж : {words_shuffled}")
