#!/usr/bin/python3
"""
import a book page from a book file into a mysql INSERT statement
"""
import os
import sys
import uuid


def add_book_pages(book_file_path, book_id, statement_file_path, page):
    """
    import a book page from a book file into a mysql INSERT statement
    """
    if not os.path.exists(book_file_path):
        print("book file path does not exist")
        sys.exit(1)
    if not os.path.exists(statement_file_path):
        print("statement file path does not exist")
        sys.exit(1)
    if not os.path.isfile(book_file_path):
        print("book file path is not a file")
        sys.exit(1)
    if not os.path.isfile(statement_file_path):
        print("statement file path is not a file")
        sys.exit(1)
    if not os.access(book_file_path, os.R_OK):
        print("book file path is not readable")
        sys.exit(1)
    if not os.access(statement_file_path, os.W_OK):
        print("statement file path is not writable")
        sys.exit(1)
    if type(book_id) is not str:
        print("book_id is not a string")
        sys.exit(1)
    if type(page) is not int:
        print("page is not an integer")
        sys.exit(1)

    with open(book_file_path) as infile, open(statement_file_path, 'a') as outfile:
        copy = False
        for line in infile:
            if "<p>" in line:
                copy = True

                line = line.lstrip().lstrip('<p>').rstrip().rstrip('</p>')
                line = line.replace("'", "''")
                outfile.write("INSERT INTO `book_pages` (`id`, `created_at`, `updated_at`, `book_id`, `page_no`, `content`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(str(uuid.uuid4()), '2023-11-21 15:00:00', '2023-11-21 15:00:00', book_id, page, line) + '\n')
            """elif "</p>" in line:
                copy = False
                print('test1')
            elif copy:
                print('test')
                print(line + '\n')
                outfile.write(line)
"""