# Pig Latin Translator

##### What is Pig Latin?

Pig Latin is a twist on English.  
Simply take any word, move the first letter to the end and add 'ay'.  
Example: **word** *becomes* **ordway**  

##### Inspiration?

The inspiration for this project was a python course that showed a short function to convert a *single* word from English to Pig Latin

##### Why?

Seems like a good chance to build an APP and learn classes.


## Goal.

To create a simple app that does 2 things.  

   1 - take in an English return Pig Latin.  
   2 - take in Pig Latin and return English.

First build will be a terminal APP, Second will add a GUI.

##### Terminal:

2 optional args. { Direction [String] }  
If no args are given then it will ask for user input.  
First the conversion, Second the string.

After taking Input make the conversion and return the result.  
Then ask if they would like to run again. 
 
   yes ->  ask for conversion again, then string.  
   no  ->  close APP.

##### GUI:

Buttons:  
   1 - Convert.  
   2 - Change conversion.

Fields:  
   1 - User input for string to convert.  
   2 - Output of conversion.

Users must be able to copy the converted result.


### NOTES
How to handle the GUI & Term modes / apps.
 - seperate files?
 - same file with check for launch mode?
 - same file with check for flag:
    ```py
    if __name__ == "__main__":
        # if launched with flag --term
        the_app = app(term)
        # else: app()
        # default = GUI
    ```

How to package with dependancies for all OS.
