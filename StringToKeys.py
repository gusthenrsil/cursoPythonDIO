string_user = input("Digite sua frase: ")
words = string_user.split()
numbers_words = len(words)
key_list = []
for i in words:
    character = i[0]
    key_list.append(character)
key = "".join(key_list)
print(key)