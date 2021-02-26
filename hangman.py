# The goal of this project is to replicate hangman using python
# A sample file is provided that should help with printing the hangman in the terminal

def terminal(misses):
    initial = ["   ____________", "   | /         ", "   |/          ", "   |           ", "   |           ", "   |           ", "   |           ", "   |           ", "   |           ", "   |           ", "   |           ", "___|__________"]
    final = ["   ____________", "   | /        |", "   |/         |", "   |         ( )", "   |         _|_", "   |        |   |", "   |     <--|   |-->", "   |        |___|","   |         / \ ","   |        /   \\","   |      o|     |o", "___|__________"]
    for val in range(len(initial)):
        if misses > val:
            print(final[val])
        else:
            print(initial[val])


if __name__ == "__main__":
    for val in range(12):
        terminal(val)