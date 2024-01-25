def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document\n")
    tuple_list = []
    letters_dict = count_letters(text)
    for letter in letters_dict:
            tuple_list.append((letters_dict[letter], letter))
    tuple_list.sort(reverse=True)
    for tuple in tuple_list:
        print(f"The '{tuple[1]}' character was found {tuple[0]} times")
    print("--- End report ---")


def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    text_list = text.split()
    return len(text_list)

def count_letters(text):
    letters = {}
    for letter in text.lower():
        if letter.isalpha():
            if not letter in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    return letters

main()