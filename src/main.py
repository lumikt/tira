from generator import Generator


def run(degree):

    markov_generator = Generator("kuono_fi_nimilista.txt",degree)

    markov_generator.train()

    generated_words = markov_generator.generate(15)

    return generated_words



if __name__ == "__main__":
    #print(run(3))
    for word in run(4):
        print(word)
