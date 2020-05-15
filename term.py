"""
Terminal pig-latin converter
Author: TwKnD
"""
# TODO: Check for punctuation at end of string.
# ' '.join([w[1:]+w[0]+'ay' if w isalpha() else w for w in text.split()])
# TODO: Check for punctuation at end of words.
# TODO: Reference wikipedia for real pig latin. mum & gma??
# TODO: Implement 'would you like to convert another
#       yes = get_conversion(), no = exit_converter()

import os


class App:

    def __init__(self):
        self.run = True

    def to_pig_latin(self, string):
        return ' '.join([(w[1:] + w[0] + 'ay') for w in string.split()])

    def to_english(self, string):
        return ' '.join([(w[-3:-2] + w[0]) for w in string.split()])

    def get_convertion(self):
        print("\n\n\n")
        print("to Pig Latin: Pig")
        print("to English: English")
        print("Q to quit")

        while True:
            convertion = input("Enter convertion: ")[0].lower()
            if convertion in ('p', 'e', 'q'):
                return convertion

    def get_string(self):
        text_to_convert = input("Enter text to convert: ").lower()
        return text_to_convert

    def exit_converter(self):
        print("Thanks for using this tool!")
        self.run = False

    def main(self):

        while self.run:
            convert_to = self.get_convertion()

            if convert_to == 'q':
                self.exit_converter()
                break

            elif convert_to == 'p':
                og_string = self.get_string()
                string = self.to_pig_latin(og_string)
                os.system('clear')
                print("English: \n" + og_string)
                print("Pig Latin: \n" + string)

            elif convert_to == 'e':
                og_string = self.get_string()
                string = self.to_english(og_string)
                os.system('clear')
                print("Pig Latin: \n" + og_string)
                print("English: \n" + string)


the_app = App()
the_app.main()
