# В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
# Одна строка файла содержит одно слово.

# Задание:
# Написать программу которая выводит список слов, 
# каждый элемент списка которого - это новое слово,
# которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
# Порядок вывода слов НЕ имеет значения

# Например, текстовый файл содержит слова:
# ласты
# стык
# стыковка
# баласт
# кабала
# карась

# Пользователь вводмт первое слово: ласты
# Программа выводит:
# ластык
# ластыковка

# Пользователь вводмт первое слово: кабала
# Программа выводит:
# кабаласты
# кабаласт

# Пользователь вводмт первое слово: стыковка
# Программа выводит:
# стыковкабала
# стыковкарась

def read_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

def find_concatenated_words(first_word, words):
    concatenated_words = []
    for word in words:
        if word != first_word:
            max_overlap = 0
            for i in range(1, min(len(first_word), len(word)) + 1):
                if first_word[-i:] == word[:i]:
                    max_overlap = i
            if max_overlap > 0:
                concatenated_words.append(first_word + word[max_overlap:])
    return concatenated_words

def main():
    file_path = 'words.txt'
    words = read_words(file_path)
    
    first_word = input("Введите первое слово: ").strip()
    
    if first_word in words:
        result = find_concatenated_words(first_word, words)
        for word in result:
            print(word)
    else:
        print("Слово не найдено в списке.")

if __name__ == '__main__':
  main()
