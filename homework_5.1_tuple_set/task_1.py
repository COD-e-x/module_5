sinema_genres = ('Роман', 'Новелла', 'Фэнтези', 'Научная Фантастика.')
some_num = 3, 7, 9, 6, 8, 2, 5, 4

print()


def process_tuples(some_tuple):
    print(f'Кортеж: {some_tuple}')
    print(f'Длина: {len(some_tuple)}')
    print(f'Максимальный и минимальный элемент: "{max(some_tuple)}" - "{min(some_tuple)}"')
    if all(isinstance(item, int) for item in some_tuple):
        print(f'Сумма: {sum(some_tuple)}')
    else:
        print('Сумма: Суммировать str не получится!')
    print(tuple(sorted(some_tuple)))
    print(tuple(sorted(some_tuple, reverse=True)))


process_tuples(sinema_genres)
print()
process_tuples(some_num)
