# Модуль 10_1 "Введение в потоки".
# ===============================================
'''Задача: Потоковая запись в файлы.'''

# Импорты необходимых модулей
from time import sleep
from datetime import datetime
from threading import Thread

# Объявление функции write_words
def write_words(word_count, file_name): # где word_count - количество записываемых слов,
    # file_name - название файла, куда будут записываться слова.
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write( f'Какое-то слово №  {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
time_start = datetime.now()

# Запуск функций с аргументами из задачи
# После создания файла вызовите 4 раза функцию wite_words
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_stop = datetime.now()
time_result = time_stop - time_start

# Вывод разницы начала и конца работы функций
print(f'Время работы функций {time_result}')

# После вызовов функций создайте 4 потока для вызова этой функции

# Взятие текущего времени
time2_start = datetime.now()

# Создание и запуск потоков с аргументами из задачи
thread_first = Thread(target=write_words, args= (10, 'example5.txt'))
thread_second = Thread(target=write_words, args= (30, 'example6.txt'))
thread_third = Thread(target=write_words, args= (200, 'example7.txt'))
thread_fourth = Thread(target=write_words, args= (100, 'example8.txt'))

thread_first.start()
thread_second.start()
thread_third.start()
thread_fourth.start()

# Остановка основного потока.
thread_first.join()
thread_second.join()
thread_third.join()
thread_fourth.join()

# Взятие текущего времени

time2_stop = datetime.now()
time2_result = time2_stop - time2_start
print(f'Время работы потоков {time2_result}')

# Вывод разницы времени работы потоков
print(f'Использование Потоков быстрее функций на {time_result-time2_result} секунд')
