words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {0: "Нулевой", 1: "Так себе", 2: "Можно лучше", 3: "Норм", 4: "Хорошо", 5: "Отлично"}


def get_difficulty_level():
    words = {}
    print('Готовы проверить ваше знание английского языка!')
    user_choice = input('Выберите уровень сложности (легкий, средний, сложный): ').lower().strip()
    if user_choice == 'средний':
        words.update(words_medium)
    elif user_choice == 'сложный':
        words.update(words_hard)
    else:
        words.update(words_easy)
    return words


def game(words):
    answers = {}
    for k, v in words.items():
        print(f'\n{k}, {len(v)}, начинается на {v[0]}...')
        user_choice = input('Предложите вариант перевода: ').lower().strip()
        if user_choice == v:
            answers[k] = True
            print('Верно')
        else:
            answers[k] = False
            print('Неверно')
    return answers


def show_the_result(words):
    correct_answers = [k for k, v in words.items() if v]
    incorrect_answers = [k for k, v in words.items() if v == False]
    if correct_answers:
        print(f'\nПравильно отвеченные слова:\n{'\n'.join(correct_answers)}')
    if incorrect_answers:
        print(f'\nНеправильно отвеченные слова:\n{'\n'.join(incorrect_answers)}')

    print(f'\nВаш ранг:\n{levels[len(correct_answers)]}')


def main():
    words = get_difficulty_level()
    answer = game(words)
    show = show_the_result(answer)
    return show


main()
