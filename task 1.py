from random import random


def experiment(player_a, player_b, matrix, ml_a, ml_b):
    a_temp = player_a
    b_temp = player_b

    player_choice = []
    a_result = 0
    b_result = 0

    for i in range(100):
        boundary_value_a = a_temp[0] / (a_temp[0] + a_temp[1])
        boundary_value_b = b_temp[0] / (b_temp[0] + b_temp[1])

        if random() < boundary_value_a:
            choice_row = 0
        else:
            choice_row = 1

        if random() < boundary_value_b:
            choice_column = 0
        else:
            choice_column = 1

        player_choice.append([choice_row, choice_column])

        a_result += matrix[choice_row][choice_column]
        b_result -= matrix[choice_row][choice_column]

        if ml_a == 1:
            if matrix[choice_row][choice_column] > 0:
                a_temp[choice_row] += matrix[choice_row][choice_column]
        elif ml_a == 2:
            if matrix[choice_row][choice_column] < 0:
                a_temp[choice_row] += matrix[choice_row][choice_column]

        if ml_b == 1:
            if matrix[choice_row][choice_column] < 0:
                b_temp[choice_row] -= matrix[choice_row][choice_column]

    math_expectation = matrix[0][0] * boundary_value_a * boundary_value_b + matrix[0][1] * (
                1 - boundary_value_b) * boundary_value_a + matrix[1][0] * (1 - boundary_value_a) * boundary_value_b + \
                       matrix[1][1] * (1 - boundary_value_a) * (1 - boundary_value_b)

    dispersion = (matrix[0][0] ** 2) * boundary_value_a * boundary_value_b + (matrix[0][1] ** 2) * boundary_value_a * (
            1 - boundary_value_b) + (matrix[1][0] ** 2) * (1 - boundary_value_a) * boundary_value_b + (
                         matrix[1][1] ** 2) * (1 - boundary_value_a) * (1 - boundary_value_b) - math_expectation ** 2

    return a_result, b_result, math_expectation, dispersion, boundary_value_b, boundary_value_b


def calculation(pa1, pb1, matrix, ma, mb):
    player_a, player_b, exp, disp, value_a, value_b = experiment(pa1, pb1, matrix, ma, mb)
    sko = disp ** 0.5

    print("Выигрыши игроков: А = {0}, В = {1}:".format(player_a, player_b))
    print("Средние выигрыши: А = {0}, В = {1}".format(player_a / 100, player_b / 100))
    print("Мат. ожидание:{:.5f}".format(exp))
    print("Дисперсия: {:.5f}".format(disp))
    print("СКО: {:.5f}\n".format(sko))
    print("Конечная вероятность А: {:.5f}\n".format(value_a))
    print("Конечная вероятность B: {:.5f}\n".format(value_b))


matrix = [[2, -3], [-1, 2]]
trial1 = [1, 1]
trial2 = [1, 3]
trial3 = [10, 10]
trial4 = [100, 100]

print('Игроки выбирают строки и столбцы с равной вероятностью:\n')
calculation(trial1, trial1, matrix, 0, 0)
print('\nИгрок В в три раза чаще выбирает синий:\n')
calculation(trial1, trial2, matrix, 0, 0)
print('\nИгрок В в три раза чаще выбирает синий, игрок А обучается с поощрением:\n')
calculation(trial3, trial2, matrix, 1, 0)
print('\nИгрок В в три раза чаще выбирает синий, игрок А обучается с наказанием:\n')
calculation(trial4, trial2, matrix, 2, 0)
print('\nИгрок В в три раза чаще выбирает синий, оба игрока обучаются с поощрением:\n')
calculation(trial3, trial3, matrix, 1, 1)
