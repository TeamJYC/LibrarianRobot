# -*- coding: utf-8 -*-
from collections import Counter

global isnbn_queue
isbn_queue = []

def get_isbn(text):
    count = 0
    text = text.replace(" ", "")
    for idx, val in enumerate(text):
        if (ord(val) >= 48 and ord(val) <= 57):
            count += 1
        else:
            count = 0
        if count == 13:
            isbn_single = text[idx-12:idx+1]
            isbn_queue.append(isbn_single)
            if len(isbn_queue) == 10:
                isbn_queue.pop(0)
            isbn_counter = Counter(isbn_queue)
            if int(isbn_counter.most_common(1)[0][1]) >= 2:
                isbn = isbn_counter.most_common(1)[0][0]
                return isbn
            break
