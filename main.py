book = "books/frankenstein.txt"

def main():
    with open(book) as f:
        file_contents = f.read()

    print(file_contents)

def wordcount():
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
    
    print(f'{len(words)} words found in the document')

def charcount():
    with open(book) as f:
        file_contents = f.read()

    counter = {}

    for character in file_contents:
        char = character.lower()
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

def bookreport():
    unsorted = charcount()
    char_list = []
    for char in unsorted:
        if char.isalpha():
            letter_dict = {"char": char, "num": unsorted[char]} 
            char_list.append(letter_dict)

    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    print(f'--- Begin report of {book} ---')
    wordcount()
    print()

    for char in char_list:
        print(f"The \'{char['char']}\' character was found {char['num']} times")

    print()
    print('--- End report ---')
    
bookreport()