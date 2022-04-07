#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Built-in
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--top', type=int, required=True, help="Number of top high frequency words")
args = parser.parse_args()
top =  args.top
assert top > 0, "number of top words must larger than 0"

words = {}

wordfile = "count_1w.txt"  # Get from https://norvig.com/ngrams/count_1w.txt
with open(wordfile) as f:
    for line in f.readlines():
        word, freq = line.strip().split()
        assert freq.isdigit()
        words[word] = int(freq)

sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)


if top < 1000:
    fname = f"{top}.txt"
else:
    quotient = top // 1000
    remainder = top % 1000
    if remainder == 0:
        fname = f"{quotient}k.txt"
    else:
        fname = f"{quotient}k_{remainder}.txt"

with open(fname, "w") as f:
    for idx, (word, freq) in enumerate(sorted_words[:top]):
        if idx == top-1:  # do not add new line on the end
            f.write(word)
        else:
            f.write(word+"\n")
