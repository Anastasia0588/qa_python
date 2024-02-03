import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    books_data = [{'Оно': 'Ужасы',
          'Макс Фрай': 'Фантастика',
          'Дракула': 'Ужасы',
          'Война и мир': 'Классика',
          'Морозко': 'Мультфильмы'
          }]

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создание экземпляра (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление двух книг
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверка, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_long_name_false(self):

        collector = BooksCollector()

        # добавление книги с названием более 40 символов
        collector.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')

        # проверка, что книга не добаваилась
        assert not collector.get_books_genre()

    def test_set_book_genre_existed_book_existed_genre_true(self):

        collector = BooksCollector()

        # добавление одной книги и жанра из списка жанров
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно','Ужасы')

        # проверка, что жанр книги "Оно"  - "Ужасы"
        assert collector.books_genre['Оно'] == 'Ужасы'

    def test_set_book_genre_existed_book_not_existed_genre_empty(self):

        collector = BooksCollector()

        # добавление одной книги и жанра к ней не из списка жанров
        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Сказки')

        # проверка, что жанр не добавился
        assert collector.books_genre['Золушка'] == ''

    @pytest.mark.parametrize('book,genre',
                             [
                                 ['Оно', 'Ужасы'],
                                 ['Макс Фрай', 'Фантастика'],
                                 ['Война и мир', 'Комедии']
                             ])
    def test_get_book_genre_books_with_genre_true(self, book, genre):

        collector = BooksCollector()

        # добавление книги и жанра из списка жанров
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        # проверка, что получаемый жанр по названию книги соответствет заданному жанру
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize('books_data', books_data)
    def test_get_books_with_specific_genre_two_books_with_same_genre_true(self, books_data):

        collector = BooksCollector()

        # создание словаря books_genre и добавление всех книг в список любимых книг
        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        # определение длины получившегося списка книг с одинаковым заданным жанром 'Ужасы'
        len_result_books_lst = len(collector.get_books_with_specific_genre('Ужасы'))

        # получаем список книг с одинаковым заданным жанром
        result_books_lst = collector.get_books_with_specific_genre('Ужасы')

        # проверка, что длина результирующего списка 2, и состава списка
        assert len_result_books_lst == 2 and result_books_lst == ['Оно', 'Дракула']

    @pytest.mark.parametrize('books_data', books_data)
    def test_get_books_for_children_two_books_without_age_rating_true(self, books_data):

        collector = BooksCollector()

        # создание словаря books_genre и добавление всех книг в список любимых книг
        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        # определение длины получившегося списка книг с без возрастного ограничения
        len_result_books_lst = len(collector.get_books_for_children())

        # получение списка книг без возрастного ограничения
        result_books_lst = collector.get_books_for_children()

        # проверка, что в результирующем списке 2 книги и состава списка
        assert len_result_books_lst == 2 and result_books_lst == ['Макс Фрай', 'Морозко']

    @pytest.mark.parametrize('books_data', books_data)
    def test_add_book_in_favorites_all_books_added_in_empty_list_true(self, books_data):

        collector = BooksCollector()

        # создание словаря books_genre и добавление всех книг в список любимых книг
        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        # получим список всех добавленных книг
        books_lst = list(collector.books_genre.keys())

        # проверка, что все книги добавлены в список любимых книг
        assert collector.favorites == books_lst

    @pytest.mark.parametrize('books_data', books_data)
    def test_delete_book_from_favorites_one_book_deleted_true(self, books_data):

        collector = BooksCollector()

        # создание словаря books_genre и добавление всех книг в список любимых книг
        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        # удаление книги из списка любимых книг и сохраннение результирующего списка любимых книг в переменную
        result_fav_books_lst = collector.delete_book_from_favorites('Макс Фрай')

        # отбор всех ключей-названий книг из словаря books_genre,
        # преобразование его в список, удаление книги из списка и сохранение в переменную для проверки
        ref_books_lst = list(collector.books_genre.keys()).remove('Макс Фрай')

        assert  result_fav_books_lst == ref_books_lst

    @pytest.mark.parametrize('books_data', books_data)
    def test_get_list_of_favorites_books_true(self, books_data):

        collector = BooksCollector()

        # создание словаря books_genre и добавление всех книг в список любимых книг
        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        # получение списка любимых книг и сохранение его в переменную
        result_fav_books_lst = collector.get_list_of_favorites_books()

        # отбор всех ключей-названий книг из словаря books_genre, преобразование его в список и сохранение в переменную
        ref_books_lst = list(collector.books_genre.keys())

        assert result_fav_books_lst == ref_books_lst
