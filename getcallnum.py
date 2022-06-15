# -*- coding: utf-8 -*-
from collections import Counter

global callnum_queue
callnum_queue = []

def get_callnum(text):
    count = 0
    text = text.replace(" ", "")
    for idx, val in enumerate(text): # 리스트 요소 하나씩 접근
        if (ord(val) >= 48 and ord(val) <= 57):
            count += 1
        else:
            count = 0
        if count == 3:
            callnum_single = text[idx-2:idx+1]
            callnum_queue.append(callnum_single)
            getcallnum = True
            if len(callnum_queue) == 10:
                callnum_queue.pop(0)
            callnum_counter = Counter(callnum_queue)
            if int(callnum_counter.most_common(1)[0][1]) >= 3:
                callnum = callnum_counter.most_common(1)[0][0]
                return callnum[0]
            break
