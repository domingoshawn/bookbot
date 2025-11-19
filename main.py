import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_char_count

if len(sys.argv) > 1:
    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents

    def main():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        get_num_words(get_book_text(sys.argv[1]))
        print("--------- Character Count -------")
        sort_char_count(get_num_char(get_book_text(sys.argv[1])))
        print("============= END ===============")

    main()
else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

