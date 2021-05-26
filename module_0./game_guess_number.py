import numpy as np

"""Загадано число от 1 до 100, необходимо отгадать его за меньшее количество попыток"""

number = np.random.randint(1, 101)                          # загаданное число
print("Загадано число от 1 до 100")


def guess_num(number):                                      # функция , которая угадывает число
    count = 0                                               # счетчик попыток
    low_predict = 1                                         # нижняя граница числа
    high_predict = 100                                      # верхняя граница числа
    
    while low_predict <= high_predict:
        middle_predict = (low_predict + high_predict) // 2  # средняя граница числа
        count += 1
        if number == middle_predict:
            return middle_predict                           # выход из цикла, если угадали
        elif number > middle_predict:
            high_predict = middle_predict - 1
        elif number < middle_predict:
            low_predict = middle_predict + 1
    return count                                            # выход из цикла, если угадали


def score_game(game):                                # функция для расчета среднего количества попыток
    """Запустите игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)                                # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:                      # запуск game для каждого сгенерированного числа
        count_ls.append(game(number))
        score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return score 


score_game(guess_num)                                # запускаем результат

