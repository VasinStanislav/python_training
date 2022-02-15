# Разделите введенное с клавиатуры предложение на слова (слова разделяются пробелом)

sentence = input("Вставить текст\n")
sentence += " "

another_word = ""
for s in sentence:
    if s != " ":
        another_word += s
    else:
        print(another_word)
        another_word = ""
