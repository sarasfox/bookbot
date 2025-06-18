def get_book_text(book_name):
    with open(book_name) as f:
        return f.read()
    
def main():
    book_name = "frankenstein"
    book_text = get_book_text(f"books/{book_name}.txt")
    print(book_text)    

main()