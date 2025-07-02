from stats import word_count


filepath = "books/"

def main():
    try:
        document = open_file(filepath + "frankenstein.txt")
        word_count(document)
    except Exception as error:
         print(error)

def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        return text

main()