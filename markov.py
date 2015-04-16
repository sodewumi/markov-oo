import sys
from random import choice

class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        opn_file = open(filenames)
        opn_file = opn_file.read().split()

        return self.make_chains(opn_file, 2)



    def make_chains(self, corpus_path, num):
        """Takes input text as string; stores chains."""

        key = []
        n_grams = {}

        for i in range(len(corpus_path)-num):

            for t in range(num):
                key.append(corpus_path[i+t])

            key = tuple(key)

            nxt_word = corpus_path[i + num]

            n_grams.setdefault(key, []).append(nxt_word)

            key = []

        for i in range(5):
            print str(i +1)+": " + self.make_text(n_grams)
        

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""
        """Takes dictionary of markov chains; returns random text."""

        # choose a random bi-gram then find the value of said bi-gram. 
        # Afterward choose a random value from the generated list
        random_n_gram = choice(chains.keys())
        random_word = choice(chains[random_n_gram])
        generated_txt = random_word

        # the last word from the previous bi-gram key along with the randomly
        # choosen word is saved for the next iteration of the while loop
        next_tuple = random_n_gram[1:] + tuple([random_word])
        n_gram_value = chains.get(next_tuple)

        while n_gram_value:
            # the random word is put in the first element of the nxt word tuple,
            # and the second element is the newly choosen random word.
            new_random_word = choice(n_gram_value)
            generated_txt = generated_txt +" "+ new_random_word
            next_tuple = next_tuple[1:] + tuple([new_random_word])

            # if the bi-gram from the previous while loop has a value, return it
            # If there is not a value, return None and close the loop
            n_gram_value = chains.get(next_tuple)


        return generated_txt



if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    script, corpus = sys.argv
    smg = SimpleMarkovGenerator()
    smg.read_files(corpus)