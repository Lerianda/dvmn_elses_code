# Файл search.py

Файл загадывает несколько целых чисел от 0 до 100 и предлагает вам угадать одно из чисел. Если введенное число есть в списке загаданных, то файл выводит в консоль позицию отгаданного числа в отсортированном списке загаданных. Поддерживает только целые числа. 

## get_num_0_100

Не принимает аргументов. В бесконечном цикле просит пользователя ввести число от 0 до 100, потом возвращает это число. Если ввели не число -- просит снова. Если ввели не от 0 до 100 -- просит снова. 

## s

Принимает на вход список и число, возвращает позицию числа в списке, если оно есть, или -1, если числа нет в списке
