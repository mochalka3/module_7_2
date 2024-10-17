def custom_write(file_name, strings):
    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}
        current_line_num = 1
        byte_offset = 0
        for string in strings:
            # Записываем строку и получаем позицию начала строки
            f.write(string + "\n")
            f.tell()  # Обновляем текущую позицию файла
            position = (current_line_num, byte_offset)

            # Добавляем строку в словарь
            strings_positions[position] = string

            # Увеличиваем номер строки и смещение
            current_line_num += 1
            byte_offset = f.tell()

    return strings_positions


# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
