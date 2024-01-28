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
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_long_name_false(self):

        collector = BooksCollector()

        # добавляем книгу с названием более 40 символов
        collector.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')

        #Проверим, что книга не добаваилась
        assert not collector.get_books_genre()

    def test_set_book_genre_existed_book_existed_genre_true(self):

        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно','Ужасы')

        #проверим, что жанры книги "Оно"  - "Ужасы"
        assert collector.books_genre['Оно'] == 'Ужасы'

    def test_set_book_genre_existed_book_not_existed_genre_empty(self):

        collector = BooksCollector()

        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Сказки')

        assert collector.books_genre['Золушка'] == ''

    @pytest.mark.parametrize('book,genre',
                             [
                                 ['Оно', 'Ужасы'],
                                 ['Макс Фрай', 'Фантастика'],
                                 ['Война и мир', 'Комедии']
                             ])
    def test_get_book_genre_books_with_genre_true(self, book, genre):

        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize('books_data', books_data)
    def test_get_books_with_specific_genre_two_books_with_same_genre_true(self, books_data):

        collector = BooksCollector()

        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert (len(collector.get_books_with_specific_genre('Ужасы')) == 2
                and collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Дракула'])

    @pytest.mark.parametrize('books_data', books_data)
    def test_get_books_for_children_two_books_without_age_rating_true(self, books_data):

        collector = BooksCollector()

        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert (len(collector.get_books_for_children()) == 2
                and collector.get_books_for_children() == ['Макс Фрай', 'Морозко'])

    @pytest.mark.parametrize('books_data', books_data)
    def test_add_book_in_favorites_all_books_added_in_empty_list_true(self, books_data):

        collector = BooksCollector()

        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        assert collector.favorites == list(collector.books_genre.keys())

    @pytest.mark.parametrize('books_data', books_data)
    def test_delete_book_from_favorites_one_book_deleted_true(self, books_data):

        collector = BooksCollector()

        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        assert collector.delete_book_from_favorites('Макс Фрай') == list(collector.books_genre.keys()).remove('Макс Фрай')

    @pytest.mark.parametrize('books_data', books_data)
    def test_get_list_of_favorites_books_true(self, books_data):

        collector = BooksCollector()

        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == list(collector.books_genre.keys())
