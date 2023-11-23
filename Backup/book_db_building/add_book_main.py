#!/usr/bin/python3
"""main file for book_db_building"""
add_book = __import__('add_book_pages').add_book_pages

if __name__ == "__main__":
    page = 1
    book_id = '73dc5c93-7837-4824-8901-5a02b89d05f0'
    statement_file_path = '/home/elmahdi/alx/MyLibrary/Backup/book_db_building/1984'

    for i in range (0, 376):
        add_book('/home/elmahdi/Téléchargements/orwell1984preywo/EPUB/page_{}.html'.format(i),
                 book_id, statement_file_path, page)
        page += 1
