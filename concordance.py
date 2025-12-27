import re
import sys

# list of abbreviations, can be expanded if I come across more
ABBREVIATIONS = ["i.e.", "e.g.", "etc.", "vs.", 
                 "mr.", "mrs.", "ms.", "dr.", "sr.", "jr.", 
                 "a.m.", "p.m.", "no.", "st.", "ave.", "dept.", "co.", "inc." ]

# the following 2 functions are to deal with the abbreviations in the text
def replace_abbreviations(text):
    # replace each . in the text that is apart of an abbreviation with the placeholder <DOT>
    placeholder = "<DOT>"
    for abbr in ABBREVIATIONS:
        fix = abbr.replace(".", placeholder)
        text = text.replace(abbr, fix)
    return text, placeholder

def restore_abbreviations(sentence, placeholder):
    # change the placeholder <DOT> back to .
    return sentence.replace(placeholder, ".")

# this function builds a concordance dictionary where each entry is a word 
# for each word the dict stores its count and a list of what sentences it appears in
def build_concordance(text):
    concordance = {}

    # replacing the '.' abbreviations with <DOT> so that they dont get split into a sentences
    text = text.lower()
    text, placeholder  = replace_abbreviations(text)

    # split all sentences
    sentence_num = 1
    sentences = re.split(r'[.!?]+', text)
    for sentence in sentences:
        sentence = sentence.strip(".!?")
        if not sentence:
            continue

        # restroing the abbreviations to their normal form
        sentence = restore_abbreviations(sentence, placeholder)

        # split each sentence into their words
        words = re.split(r'\s+', sentence)
        for word in words:
            word = word.strip(",;:\"()[]{}")
            if not word:
                continue

            # add each word to the concordance
            if word not in concordance:
                concordance[word] = {
                    "count": 1, 
                    "occurrences": [sentence_num]
                }
            else:
                concordance[word]["count"] += 1
                concordance[word]["occurrences"].append(sentence_num)

        sentence_num += 1

    return concordance


def main():
    # check for correct usage
    if len(sys.argv) != 3:
        print("Usage: python3 concordance.py <input_file> [1|2]")
        print("incorrect number of arguments")
        sys.exit(1)

    # check if number in usage is correct
    output = int(sys.argv[2])
    if not (output == 1 or output == 2):
        print("Usage: python3 concordance.py <input_file> [1|2]")
        print("only allowed numbers are 1 and 2")
        sys.exit(1)

    # open the file
    file = sys.argv[1]
    with open(file, "r", encoding="utf-8") as fin:
        text = fin.read()

    # build the concordance
    concordance = build_concordance(text)

    # write the concordance to an output file or print to terminal
    if output == 1:
        with open("concordance_output.txt", "w", encoding="utf-8") as fout:
            count = 1
            for word in sorted(concordance):
                occurrences = ','.join(map(str, concordance[word]["occurrences"]))
                fout.write(f'{count}. {word} {{{concordance[word]["count"]}:{occurrences}}}\n')
                count += 1
    elif output == 2:
        count = 1
        for word in sorted(concordance):
            occurrences = ','.join(map(str, concordance[word]["occurrences"]))
            print(f'{count}. {word} {{{concordance[word]["count"]}:{occurrences}}}')
            count += 1

if __name__ == "__main__":
    main()