from generator import Generator
import sys

def main():

    source = sys.argv[1]
    print("Please select generation specifics.")
    degree = int(input("What degree chain do you wish to use?: "))
    words_to_generate = int(input("How many words to generate?: "))
    word_length = int(input("How long should the words be?: "))

    markov_generator = Generator(source,degree,word_length)

    markov_generator.train()

    generated_words = markov_generator.generate(words_to_generate)

    print(f"Generated {words_to_generate} words of length {word_length} with a {degree}-degree Markov Chain.")
    print(f"Words based on training data in {source}.")
    print()
    for word in generated_words:
        print(word," : ", len(word))
    
    print("Do you wish to save these words?")
    

    save = input("y/n?: ")
    
    if save not in "yn":
        while True:
            print("Invalid input, please reply y or n.")
            save = input("y/n?: ")
            if save == "y" or save =="n":
                break
    
    if save == "y":
        generated_words_as_string = "\n".join(generated_words)
        with open("generated_words.txt", "w") as file:
            file.write(generated_words_as_string)
        print("Words saved")
    
    elif save == "n":
        print("No words saved.")
    
    print("Thanks for using the generator.")


if __name__ == "__main__":
    main()