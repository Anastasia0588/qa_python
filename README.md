# qa_python

## Домашние задания по курсу "Автоматизатор тестирования на Python"
В данном репозитории будут выкладываться домашниие задния по курсу "Автоматизатор тестирования на Python" от Яндекс.Практикум

## Sprint4 
Юнит-тестирование

## Финальный проект
Задание: покрыть тестами приложение BooksCollector

### Тесты:

- test_add_new_book_add_two_books — *пример из задания*

- test_add_new_book_add_long_name_false — *книга с названием длиннее 40 символов не добавляется в списокс книг*
- test_set_book_genre_existed_book_existed_genre_true — *добавленной книге устанавливается жанр из списка жанров*
- test_set_book_genre_existed_book_not_existed_genre_empty — *добавленной книге устанавливается пустой жанр, если добавляли жанр не из списка*
- test_get_book_genre_books_with_genre_true — *по имен книги выводится ее жанр*
- test_get_books_with_specific_genre_two_books_with_same_genre_true — *список из двух книг с одинаковыми жанрами*
- test_get_books_for_children_two_books_without_age_rating_true — *список из двух книг вне возрастного ограничения*
- test_add_book_in_favorites_all_books_added_in_empty_list_true — *добавление всех книг в пустой список любимых книг*
- test_delete_book_from_favorites_one_book_deleted_true — *удаление заданной книги из списка любимых книг*
- test_get_list_of_favorites_books_true — *получение списка любимых книг*

### Запустить все тесты
```bash
pytest -v tests.py
```
