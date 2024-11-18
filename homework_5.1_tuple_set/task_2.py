cinema_genres = ('Комедия', 'Экшн', 'Пеплум', 'Триллер')
print(cinema_genres)
print()

change_cinema_genres = tuple('Боевик' if v == 'Экшн' else v for v in cinema_genres)

# так как мы знаем индекс каждого элемента не стал усложнять циклом
updated_genre_tuple = change_cinema_genres[:2] + ('Фэнтези',) + change_cinema_genres[2:]
print(tuple(updated_genre_tuple))

change_cinema_genres_in_str = ', '.join(updated_genre_tuple)
print(f'Обновленные жанры кино: {change_cinema_genres_in_str}')
