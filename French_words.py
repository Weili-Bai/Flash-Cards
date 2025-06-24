import pandas
import random

SUCCESS = {"French": "Vous avez résussi!", "English": "You succeeded!"}


def get_tuple():
    try:
        comb = random.choice(my_dict)
    except:
        comb = SUCCESS
    return comb


try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
my_dict = data.to_dict(orient="records")
if len(my_dict) == 0:
    data = pandas.read_csv("./data/french_words.csv")
    my_dict = data.to_dict(orient="records")
