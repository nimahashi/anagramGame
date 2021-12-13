import urllib.request

def AnagramGame(letterset: str, URL_wordlist: str) -> list:
    '''
    Construct an instance of the game.

    letterset: str The set of letters the player can use to construct words
    param URL_wordlist: wordlist URL for the word list to check against
    return:
    '''

    top_ten_words = []
    top_ten_scores = []
    username = input("Hello! What is your name? ")
    while True:
        found = False
        file = urllib.request.urlopen(URL_wordlist)
        answer = input(
            username + ", create the longest possible word out of the word '" + letterset + "': ")

        if valid(letterset, answer):
            for word in file:
                possible_word = word.decode("utf-8").strip()
                if possible_word == answer:
                    found = True
                    if possible_word in top_ten_words:
                        print("You already used this word.")
                        break
                    if len(top_ten_scores) < 10:
                        top_ten_scores.append(len(possible_word))
                        top_ten_words.append(possible_word)
                    elif len(possible_word) > min(top_ten_scores):
                        delete = index_finder(top_ten_scores,
                                              min(top_ten_scores))
                        top_ten_scores.pop(delete)
                        top_ten_words.pop(delete)
                        top_ten_scores.append(len(possible_word))
                        top_ten_words.append(possible_word)
                    break

            if not found:
                print("This word is not in the text file.")
        else:
            print("This word is not valid, try again.")

        playAgain = input("Would you like to play again? [y/n]")
        if playAgain == 'n':
            break
    print(showhighscorelist(top_ten_scores, top_ten_words))


def valid(word1: str, word2: str) -> bool: # submitWord function but implemented with 2 param.
    """

    word1: The word the player uses to assemble a new word
    word2: The word the player suggested
    return: True if word2 can be assembled using only letters in word1 with no repeats else return False.
    """

    for letter in word2:
        if word2.count(letter) > word1.count(letter):
            return False
    return True


def index_finder(scores: list, lowest_score: int) -> int:
    """
    scores: List of the top 10 highest score
    lowest_score: lowest score of scores
    return: index of last occurrence with the value <lowest_score>
    """
    delete = -1
    for score in range(len(scores)):
        if scores[score] == lowest_score:
            delete = score
    return delete


def showhighscorelist(top_ten_scores: list, top_ten_words: list) -> list:
    """
    top_ten_scores: list of top ten highest scores
    top_ten_words: list of top ten words
    return: a list of the top 10 highest scores along with the word
    """
    final_score = []
    for i in range(len(top_ten_scores)):
        final_score.append([top_ten_words[i], top_ten_scores[i]])
    return final_score

#AnagramGame("areallylongword",
            #"http://www.math.sjsu.edu/~foster/dictionary.txt")
# I had to use the text above because the one provided does'nt work.
