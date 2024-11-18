cinema_genres = ['комедия', 'экшн', 'пеплум', 'триллер', 'комедия', 'пеплум']
cinema_genres_set = set(cinema_genres)

cinema_genres_set.update({'фэнтези', 'боевик'})

cinema_genres_set.discard('экшн')

some_item_with_cinema_genres_set = cinema_genres_set.pop()

set_to_list = list(cinema_genres_set)

print(set_to_list)
