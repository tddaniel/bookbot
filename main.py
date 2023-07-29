
def letter_count(text):
    text = text.lower()
    out = {}
    for char in text:
        if char in out:
            out[char] += 1
        else:
            out[char] = 1
    out = {k:v for k,v in sorted(out.items(), key=lambda item: item[1],reverse=True)}
    return out
book = "frankenstein.txt"
with open(f"books/{book}") as f:
    file_contents = f.read()
    words = file_contents.split()

    char_count = letter_count(file_contents)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{len(words)} words were found in {book}.\n")

    for k,v in char_count.items():
        if k.isalpha():
            print(f"The {k} character was found {v} times")
