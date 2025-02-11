def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = character_count(text)

    #display word count

    print(f"{num_words} words found in the document")

    #display sorted character counts
    sorted_counts = sorted(character_counts.items())
    print ("Character counts (sorted alphabetically):")
    for char, count in sorted_counts:
        print(f"'{char}': {count}")
    print()

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words (text):
    words = text.split()
    return len(words)

def character_count(text):
    count = {}
    low_words = text.lower()
    for char in low_words:
         if char.isalpha():
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    return count


main()


