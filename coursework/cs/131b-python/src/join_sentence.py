'''
e2_join_sentence.py
jl-ccsf
06/12/2026
CS-131B, Prof. Ibrahim
Selects a word list by its index and joins them in a sentence.
'''

def main():

    # Defines word lists and sentence variables
    word_list = [["Today", "is", "a", "good", "day."], 
                 ["Apples", "are", "my", "favorite", "fruit."]]
    sentence_1 = join_sentence(word_list, 0)
    sentence_2 = join_sentence(word_list, 1)

    # Displays sentences
    print(sentence_1)
    print(sentence_2)

'''Selects list and joins items'''
def join_sentence(outer_list, x):
    sentence = " ".join(outer_list[x])
    return sentence

main()

'''
SAMPLE RUN

Today is a good day.
Apples are my favorite fruit.
'''
