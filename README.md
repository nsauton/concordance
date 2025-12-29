# Concordance

This program builds a concordance given an arbitrary text document written in English. A concordance is an alphabetical list of all word occurrences in the text document. The concordance provides the overall count for a word, followed by a colon, and then the sentence numbers in which each occurrence appeared.  

## concordance.py  

usage:  
python3 concordance.py [-h] [--print] input_file  
Build a concordance from an English text file  
positional arguments:  
  input_file  Text file to build the concordance from  
options:  
  -h, --help  show this help message and exit  
  --print     Print output to terminal instead of writing to file  

input files used are found in the files/ folder
By default, output is written to a file called 'concordance_output.txt' unless the --print flag is attached which forces output to be printed to the terminal.  

## files folder  

text files used by the concordance program  

## tests folder  

contains the unit testing for both the build_concordance function and the parse_args function, which take care of the concordance building logic and command line argument parsing respectively.  
In root folder, run tests with:  
python3 -m unittest discover tests  