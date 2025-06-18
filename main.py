import sys
from stats import get_num_words
from stats import get_char_num
from stats import sort_char_counts
from stats import sort_num_order
#start here

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return (file_contents)

def main():
    if len(sys.argv) !=2:
          print("Usage: python3 main.py <path_to_book>")
          sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    char_num = get_char_num(book_text)
    sorted_char_strings = sort_char_counts(char_num)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words") 
    print("--------- Character Count -------")
    sorted_num_order = sort_num_order(char_num)
    for line1 in sorted_num_order:
        if line1["char"].isalpha():
            print(f"{line1['char']}: {line1['num']}")
        
    print("=== THE END ===")

main()

