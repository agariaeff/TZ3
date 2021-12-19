import custom_funcs as cf


def main(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(' ')))
        print(f'Вход: {data}\n')
        print(f'Сумма:\t\t\t{cf.custom_sum(data)}')
        print(f'Произведение:\t{cf.custom_mul(data)}')
        print(f'Максимум:\t\t{cf.custom_max(data)}')
        print(f'Минимум:\t\t{cf.custom_min(data)}')


main('input.txt')
