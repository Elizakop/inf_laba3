# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delimiter= ','): # функция находит общих участников в двух группах
    first_list = first_group.split(delimiter)
    second_list = second_group.split(delimiter) # разбиваем вторую группу на список участников
    common = set(first_list) & set(second_list) # возвращаем множество содержащее элементы которые есть в обоих множествах
    return sorted(common) # возвращаем отсортированный список всех участников

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants("Иванов|Петров|Сидоров", "Петров|Сидоров|Смирнов", ";")
print(result)