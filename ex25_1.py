import ex25
sentence = "All good thins come to those who wait."
words = ex25.break_words(sentence)

sorted_words = ex25.sort_words(words)

ex25.print_first_word(words)
ex25.print_last_word(sorted_words)

sorted_words = ex25.sort_sentence(sentence)

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
