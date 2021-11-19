import os
import re
import string
import random

from graph import Graph, Vertex


# get words from text
# create a graph
# get next for x number of words
# print the output

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        text = ' '.join(text.split())  # turns all whitespaces to spaces
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))  # removes punctutation

    words = text.split()  # split on spaces
    return words


def make_graph(words):
    g = Graph()

    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    g.generate_probability_mapping()
    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():
    words = get_words_from_text('texts/TaylorLyrics.txt')

    g = make_graph(words)

    composition = compose(g, words, 100)
    print(' '.join(composition))


if __name__ == '__main__':
    main()