import re
import sys

ABBREVIATIONS = ["i.e."]

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

def build_concordance(text):
    concordance = {}

    # replacing the '.' abbreviations with <DOT> so that they dont get split into a sentences
    text = text.lower()
    text, placeholder  = replace_abbreviations(text)

    # split all sentences
    sentence_num = 1
    sentences = re.split(r'[.!?]+', text)
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        # restroing the abbreviations to their normal form
        sentence = restore_abbreviations(sentence, placeholder)

        # split each sentence into their words
        words = re.split(r'\s+', sentence)
        for word in words:
            word = word.strip(",!?;:\"()[]{}")
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
    if len(sys.argv) != 2:
        print("Usage: python3 concordance.py <input_file>")
        sys.exit(1)

    # open the file
    file = sys.argv[1]
    with open(file, "r", encoding="utf-8") as fin:
        text = fin.read()

    # build the concordance
    concordance = build_concordance(text)

    # write the concordance to an output file
    with open("concordance_output.txt", "w", encoding="utf-8") as fout:
        count = 1
        for word in sorted(concordance):
            occurrences = ','.join(map(str, concordance[word]["occurrences"]))
            fout.write(f'{count}. {word} {{{concordance[word]["count"]}:{occurrences}}}\n')
            count += 1

if __name__ == "__main__":
    main()