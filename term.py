"""
Terminal pig-latin converter
Author: TwKnD
"""
import os


class App:

    def __init__(self):
        self.run = True
        os.system('clear')
        # TODO: Add welcome message with description of pig latin.

    def to_pig_latin(self, string):
        l1 = []
        for w in string.split():
            if not w[-1].isalpha() and w[:-1].isalpha():
                l1.append(w[1:-1] + w[0] + 'ay' + w[-1])
            elif not w.isalpha():
                l1.append(w)
            else:
                l1.append(w[1:] + w[0] + 'ay')

        return ' '.join(l1).capitalize()

    def to_english(self, string):
        l1 = []
        print('start:', string)
        for w in string.split():
            print(w)
            if w.isalpha():
                l1.append(w[-3] + w[:-3])
            elif len(w) > 3:
                l1.append(w[-4] + w[:-4] + w[-1])
            else:
                l1.append(w)
        return ' '.join(l1).capitalize()

    def get_convertion(self):
        print("\n\n")
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
            # TODO: Add ask if convert again.

            if convert_to == 'q':
                self.exit_converter()
                break

            elif convert_to == 'p':
                og_string = self.get_string()
                string = self.to_pig_latin(og_string)
                os.system('clear')
                print("\n\nEnglish: \n" + og_string)
                print("\n\nPig Latin: \n" + string)

            elif convert_to == 'e':
                og_string = self.get_string()
                string = self.to_english(og_string)
                os.system('clear')
                print("\n\nPig Latin: \n" + og_string)
                print("\n\nEnglish: \n" + string)


the_app = App()
the_app.main()
