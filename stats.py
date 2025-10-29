def get_num_words(book):
    words = book.split()
    return len(words)

def get_num_characters(book):
    character_count = {}
    for character in book:
        char = character.lower()
        if char not in character_count:
            character_count[char] = 1
        else: character_count[char] += 1
    
    return character_count

def sort_on(items):
    return items["num"]

    
def sort_letter(input):
    dicto = []

    for ch, count in input.items():
        output = {}

        output["char"] = ch
        output["num"] = count
        if ch.isalpha() == True:
            dicto.append(output)

    dicto.sort(reverse=True, key=sort_on)
    return dicto
