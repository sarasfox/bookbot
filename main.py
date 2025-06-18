from stats import get_num_words,count_letters
import sys

def get_book_text(book_name):
    with open(book_name) as f:
        return f.read()
    
def main():
    if len(sys.argv) > 1:
        book_name = sys.argv[1]
    else:   
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_name) 
    num_words = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at '{book_name}'...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in count_letters(book_text):
        print(f"{i[0]}: {i[1]}")
    print("============= END ===============")

main()