
filepath = "books/"

def main():
    try:
            return open_file(filepath + "frankenstein.txt")
    except Exception as error:
         print(error)

def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        print(text)



main()
