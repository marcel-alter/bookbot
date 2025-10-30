import sys
import os
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
if not os.path.isfile(book_path):
    print(f"Error: file not found: {book_path}")
    sys.exit(2)

def get_book_text(input):
    with open(input) as f:
        file_contents = f.read()
        return file_contents

def main(path):
    book = get_book_text(path)
    from stats import get_num_words
    num_words = get_num_words(book)
    
    from stats import get_num_characters
    num_characters = get_num_characters(book)

    from stats import sort_letter
    sorted_number = sort_letter(num_characters)

    print(f"Found {num_words} total words")
    for i in sorted_number:
        print(f"{i["char"]}: {i["num"]}")

print(sys.argv)
main(sys.argv[1])
