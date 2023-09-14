# only real gamers get this (idk why I made a repo for this)
import sys
import random

def main():
    if len(sys.argv) != 4:
        print("usage: markovtext.py <corpuslocation> <seedlength> <textlength>")
        return 1

    # generate a dictionary corpus of the format "seed" : "[next chars]"
    k = int(sys.argv[2])
    end_length = int(sys.argv[3])
    corpus = {}

    with open(sys.argv[1]) as f:
        seed = ""
        for line in f:
            current_line = line
            
            for c in current_line:
                #add character to existing markov chain
                if len(seed) == k:
                    if seed in corpus:
                        corpus[seed].append(c)
                    else:
                        corpus[seed] = [c]

                #update the seed
                seed += c
                if len(seed) > k:
                    seed = seed[len(seed)-k:]

    # choose a random seed to start with and generate text until we hit the length
    generated_text = random.choice(list(corpus.keys()))
    while len(generated_text) < end_length:
        key = generated_text[-k:]
        if not key in corpus:
            break
        generated_text += random.choice(corpus[key])

    print(generated_text)
    return 0

if __name__ == "__main__":
    sys.exit(main())