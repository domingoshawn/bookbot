def get_num_words(book):
    num_words = len(book.split())
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_num_char(book):
    counted_chars = {}
    words = list(book.lower())
    for each in words:
        if each in counted_chars:
            counted_chars[each] += 1
        else:
            counted_chars[each] =1
    return counted_chars

def sort_char_helper(book):
    return book["num"]

def sort_char_count(counted_char):
    grouped_char_count = []
    for char in counted_char:
        char_count = counted_char[char]
        per_char = {"char": char, "num": char_count}
        grouped_char_count.append(per_char)
        grouped_char_count.sort(reverse=True, key=sort_char_helper)
    for each in grouped_char_count:
        print(f"{each["char"]}: {each["num"]}")
