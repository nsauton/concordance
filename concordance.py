import re
import argparse

# list of abbreviations, can be expanded if I come across more
ABBREVIATIONS = ["i.e.", "e.g.", "etc.", "vs.", 
                 "mr.", "mrs.", "ms.", "dr.", "sr.", "jr.", 
                 "a.m.", "p.m.", "no.", "st.", "ave.", "dept.", "co.", "inc." ]

def replace_abbreviations(text):
    """
    Replace periods in known abbreviations with a placeholder
    returns the updated text and the placeholder
    """
    placeholder = "<DOT>"
    for abbr in ABBREVIATIONS:
        fix = abbr.replace(".", placeholder)
        text = text.replace(abbr, fix)
    return text, placeholder

def restore_abbreviations(sentence, placeholder):
    """
    Restore abbreviation placeholders back to periods.
    """
    return sentence.replace(placeholder, ".")

def build_concordance(text):
    """
    Build a concordance from an English text.

    Each word maps to:
      - total occurrence count
      - a list of sentence numbers in which it appears

    Returns the constructed concordance dictionary.
    """

    concordance = {}

    # replace abbreviations so they dont get split into sentences
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

def parse_args(argv=None):
    """
    Parse the command line arguments
    """
    
    parser = argparse.ArgumentParser(
        description="Build a concordance from an English text file"
    )

    parser.add_argument(
        "input_file",
        help="Text file to build the concordance from"
    )

    parser.add_argument(
        "--print",
        dest="print_output",
        action="store_true",
        help="Print output to terminal instead of writing to file"
    )

    return parser.parse_args(argv)


def main():
    # parse command line arguments
    args = parse_args()

    # open the file
    with open(args.input_file, "r", encoding="utf-8") as fin:
        text = fin.read()

    # build the concordance
    concordance = build_concordance(text)

    # write the concordance to an output file or print to terminal
    if args.print_output:
        count = 1
        for word in sorted(concordance):
            occurrences = ','.join(map(str, concordance[word]["occurrences"]))
            print(f'{count}. {word} {{{concordance[word]["count"]}:{occurrences}}}')
            count += 1
    else:
        with open("concordance_output.txt", "w", encoding="utf-8") as fout:
            count = 1
            for word in sorted(concordance):
                occurrences = ','.join(map(str, concordance[word]["occurrences"]))
                fout.write(f'{count}. {word} {{{concordance[word]["count"]}:{occurrences}}}\n')
                count += 1

if __name__ == "__main__":
    main()