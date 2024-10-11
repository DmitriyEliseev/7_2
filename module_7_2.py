def custom_write(file_name, strings):
    strings_positions = {}  # Словарь для хранения позиций строк

    with open(file_name, 'w', encoding='utf-8') as file:
        for idx, s in enumerate(strings):
            position = file.tell()  # Получаем позицию перед записью строки
            file.write(s + '\n')
            strings_positions[(idx + 1, position)] = s  # Добавляем позицию и строку в словарь

    return strings_positions

# Пример выполнения программы
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
