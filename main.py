from stats import get_num_words, get_char_count, get_sorted_list
import sys

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()    
    return file_contents

def main():
    
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {filepath}")
    print("----------- Word Count ----------")
    num_words = get_num_words(contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_list = get_sorted_list(get_char_count(contents))
    for row in char_list:
        print(f"{row["name"]}: {row["num"]}")
    print("============= END ===============")
    
main()