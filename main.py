import sys
from stats import get_num_words, get_num_char, sort_content

# Read file text from given path
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    # Validate number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get path from command line
    book_path = sys.argv[1]
    
    # Pass book_path to get_book_text()
    text = get_book_text(book_path)

    # Process text
    count = get_num_words(text)
    characters = get_num_char(text)
    sorted_content = sort_content(characters)

    # Output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_content:
        for key, value in item.items():
            print(f"{key}: {value}")

# Only run if script is executed directly
if __name__ == "__main__":
    main()