# Concordance

This program builds a concordance given an arbitrary text document written in English. A concordance is an alphabetical list of all word occurrences in the text document. The concordance provides the overall count for a word, followed by a colon, and then the sentence numbers in which each occurrence appeared.  

## concordance.py  

Build a concordance from an English text file  
usage:  
python3 concordance.py [-h] [--print] input_file  
positional arguments:  
  input_file  Text file to build the concordance from  
options:  
  -h, --help  show this help message and exit  
  --print     Print output to terminal instead of writing to file  

text files used for the input_file are found in the files/ folder
By default, output is written to a file named <input_file>_concordance.txt in the same directory as the input file.  
If the --print flag is provided, the concordance is printed to the terminal instead of being written to a file.  

## files folder  

text files used by the concordance program  

## tests folder  

contains the unit testing for both the build_concordance function and the parse_args function, which take care of the concordance building logic and command line arguments parsing respectively.  
In root folder, run tests with:  
python3 -m unittest discover tests  