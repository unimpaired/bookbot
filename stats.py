def word_count(document):
    words = document.split()
    count = 0

    for word in words:
        count += 1
    
    print(f'{count} words found in the document')
