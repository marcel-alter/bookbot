def get_book_text(input):
    with open(input) as f:
        file_contents = f.read()
        return file_contents

def main(input_2):
    book = get_book_text(input_2)
    from stats import get_num_words
    num_words = get_num_words(book)
    
    from stats import get_num_characters
    num_characters = get_num_characters(book)

    from stats import sort_letter
    sorted_number = sort_letter(num_characters)

    print(f"Found {num_words} total words")
    for i in sorted_number:
        print(f"{i["char"]}: {i["num"]}")




main("books/frankenstein.txt")
