import sys
from stats import word_count, char_count, sort_char_counts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path, "r", encoding="utf-8") as file:
        return file.read()

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    char_counts = char_count(book_text)
    sorted_char_counts = sort_char_counts(char_counts)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # Filter only alphabetic characters and sort alphabetically
    alpha_char_counts = [item for item in sorted_char_counts if item['char'].isalpha()]
    alpha_char_counts.sort(key=lambda x: x['char'])
    for item in alpha_char_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()