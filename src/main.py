from generator import Generator
import sys

def main():

    source = sys.argv[1]
    degree = int(sys.argv[2])
    words_to_generate = int(sys.argv[3])
    word_length = int(sys.argv[4])

    markov_generator = Generator(source,degree,word_length)

    markov_generator.train()

    generated_words = markov_generator.generate(words_to_generate)

    print(f"Generated {words_to_generate} words of length {word_length} with a {degree}-degree Markov Chain.")
    print(f"Words based on training data in {source}.")
    print()
    for word in generated_words:
        print(word," : ", len(word))
    
    print("Do you wish to save these words?")
    save = input("y/n?:")

    if save == "y":
        generated_words_as_string = "\n".join(generated_words)
        with open("generated_words.txt", "w") as file:
            file.write(generated_words_as_string)
        print("Words saved")
    
    elif save == "n":
        print("No words saved.")
    
    else:
        print("Invalid input, please repeat.")
        save = input("y/n?:")

    print("Thanks for using the generator.")


if __name__ == "__main__":
    main()