# without zip, iterate through the index values
def give_feedback(guess, correct_word):
    # Give feedack about a guessed word for a Wordle-like game
    feedback = []
    for i in range(len(guess)):
        guessed_let = guess[i]
        correct_let = correct_word[i]
        if guessed_let == correct_let:
            feedback.append("Y")
        elif guessed_let in correct_word:
            feedback.append("y")
        else:
            feedback.append("-")
    return feedback

# using zip, it's a little easier to understand
def give_feedback(guess, correct_word):
    # Give feedack about a guessed word for a Wordle-like game
    feedback = []
    for guessed_let, correct_let in zip(guess, correct_word):
        if guessed_let == correct_let:
            feedback.append("Y")
        elif guessed_let in correct_word:
            feedback.append("y")
        else:
            feedback.append("-")
    return feedback


# with a list comprehension instead of manual accumulation

def one_letter_feedback(guessed_let, correct_let, correct_word):
    if guessed_let == correct_let:
        return "Y"
    elif guessed_let in correct_word:
        return "y"
    else:
        return "-"

def give_feedback(guess, correct_word):
    # Give feedack about a guessed word for a Wordle-like game
    return [one_letter_feedback(guessed_let, correct_let, correct_word) 
            for guessed_let, correct_let in zip(guess, correct_word)]

# tests for the above function 

assert list(give_feedback("guess", "guess")) == ['Y', 'Y', 'Y', 'Y', 'Y']
assert list(give_feedback("abcde", "fghij")) == ['-', '-', '-', '-', '-']
assert list(give_feedback("abcde", "edcba")) == ['y', 'y', 'Y', 'y', 'y']
assert list(give_feedback("hello", "hails")) == ['Y', '-', 'y', 'Y', '-']
assert list(give_feedback("tests", "testy")) == ['Y', 'Y', 'Y', 'Y', 'y']
assert list(give_feedback("testy", "tests")) == ['Y', 'Y', 'Y', 'Y', '-']



list1 = ["cat", "sun", "red"]
list2 = ["dog", "sky", "blue"]
list3 = ["cow", "sea", "green"]

zipped = zip(list1, list2, list3)
longest_words = [max(group, key=len) for group in zipped]
print(longest_words)