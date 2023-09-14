# MarkovTextGenerator
A silly text generator using a markov chain on an existing corpus to make something new.
This works by taking the previous <seedlength> characters and checking all possible next letters, then choosing one.

usage: markovtext.py <corpuslocation> <seedlength> <textlength>