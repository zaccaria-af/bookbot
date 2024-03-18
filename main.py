def count_words(text: str) -> int:
    return len(text.split())

def get_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()
    
def count_letters(text: str) -> int:
    text = ''.join([i for i in text.lower() if i.isalpha()])
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    words = count_words(file_contents)
    letter_count = count_letters(file_contents)
    sorted_letter_count = dict(reversed(sorted(letter_count.items(), key=lambda item: item[1])))
    print(f"--- Begin report of {path} ---\n")
    print(f"{words} words found in the document \n\n")
    for letter in sorted_letter_count:
        print(f"The character {letter} was found {sorted_letter_count[letter]} times\n")
    print("--- End report ---")

main()
