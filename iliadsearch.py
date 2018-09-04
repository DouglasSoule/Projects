#!usr/bin/env python 3

with open('iliad.txt') as iliad:
    term_count = 0
    mult_term_line = 0
    search_term= 'achilles'
    for line in iliad:
        line = line.lower()
        if search_term in line:
            term_count += line.count(search_term)
            if line.count(search_term) > 1:
                print(line)
                mult_term_line += 1

    print(term_count)
    print(mult_term_line)
