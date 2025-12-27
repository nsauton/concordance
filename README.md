# Concordance

This progam builds a concordance given an arbitrary text document written in English. A concordance is an alphabetical list of all word occurrences in the text document. The concordance provides the overall count for a word, followed by a colon, and then the sentence numbers in which each occurrence appeared.  

## concordance.py  
Usage: "python3 concordance.py <input_file> [1|2]"  
concordance.py is the program that builds the concordance  
<input_file> text file that the concordacne is built from (files used are found in the files/ folder)  
[1|2] 1 to write to an output file concordance_output.txt, 2 to print to the terminal  

## files folder
test files I used for manual testing purposes

## tests folder
unit testing here, run it with "python3 -m unittest discover tests" in root folder