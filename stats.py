def letters_sort(letters):
    return sorted(letters, key=lambda x: x[1], reverse=True)
    
    
def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    letters = {}
    for l in book_text:
        if l.isalpha():
            lo = l.lower()
            if lo in letters:
                letters[lo] += 1
            else:
                letters[lo] = 1
    return letters_sort(list(letters.items()))