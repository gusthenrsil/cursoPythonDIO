def initial_key(words):
    key_list = []
    for i in words:
        character = i[0]
        key_list.append(character)
    key = "".join(key_list)
    return key

def last_key(words):
    end_characters = []
    for i in words:
            position = len(i)-1
            end_characters.append(i[position])
    end_key = "".join(end_characters)
    first_key = initial_key(words)
    return first_key + end_key


string_user = input("Digite sua frase: ")
words = string_user.split()
if len(words) >= 8:
    key = initial_key(words)
else:
    key = last_key(words)
print(key)