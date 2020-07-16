from flask import request
import random

def riddle():

    if request.form(difficulty) == "Easy":
        return "randint.choice(easylist)"
    elif request.form(difficulty) == "Medium":
        return "randint.choice(mediumlist)"
    elif request.form(difficulty) == "Hard":
        return "randint.choice(hardlist)"
    else:
        return "ERROR"
