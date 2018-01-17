fname = raw_input("(Entre com o nome do arquivo) Enter file name: ")

num_words = 0
num_char = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        num_char += sum(len(word) for word in words)
    median = float(num_char/float(num_words))
print("(Numero de palavras) Number of words:")
print(num_words)
print(" (Numero de letras) Number of letters")
print(num_char)
print("median")
print(median)