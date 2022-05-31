constituency = {"label": [[], ["S"], ["PP"], ["NP"], ["NP-SBJ"], ["VP"], ["ADJP"], ["SBAR"], ["NP-SBJ-1"], ["NP-SBJ-2"], ["S-1"], ["PRN"], ["SINV"], ["ADVP"], ["SBAR-NOM-SBJ"], ["FRAG", "NP"], ["QP"], ["S-SBJ"], ["NP-LGS"], ["UCP-PRD"], ["PP-PRD"], ["S-ADV"], ["PRT"], ["NP-PRD"], ["ADJP-PRD"], ["NP", "NP"], ["NP", "QP"], ["S-TPC-1"], ["FRAG", "ADJP"], ["NP-SBJ-3"], ["S", "NP-SBJ"], ["NP-ADV"], ["NP-SBJ", "NP"], ["S-NOM"], ["NP-1"], ["NP-TTL"], ["FRAG", "ADVP"], ["NP-2"], ["NP-3"], ["UCP"], ["NP=1", "QP"], ["NP=1"], ["S-NOM-SBJ"], ["S-PRD"], ["SBAR-2"], ["SBAR=2"], ["NP-SBJ-4"], ["S=1"], ["NP=2"], ["NP-PRD", "QP"], ["NP-SBJ=1"], ["NP=2", "QP"], ["FRAG", "NP", "QP"], ["CONJP"], ["SBAR-PRD"], ["S", "NP-SBJ-1"], ["SINV-TPC-1"], ["NP-TPC-2"], ["INTJ"], ["NAC-TMP"], ["NP-PRD", "NP"], ["FW"], ["SBARQ"], ["WHADVP"], ["SQ"], ["FRAG", "PP"], ["NP-1", "NP"],
                          ["SBAR-NOM"], ["SINV-1"], ["ADVP-PRD"], ["SINV", "VP"], ["PP-SBJ"], ["SINV", "S-TPC-1"], ["PP-2"], ["PP=2"], ["NP-2", "QP"], ["WHNP-1"], ["NP-SBJ-5"], ["UCP-1"], ["S-2"], ["NP-SBJ-2", "QP"], ["PP-3"], ["NP-SBJ=2", "QP"], ["PP=3"], ["S-TPC-2"], ["INTJ", "NP"], ["S-TTL"], ["NP-TMP"], ["SBAR-SBJ"], ["NP", "ADJP"], ["SQ-PRD"], ["NP-SBJ-1", "NP"], ["S", "PP"], ["NP-1", "QP"], ["NP-SBJ-2", "NP"], ["SBAR-TPC-1"], ["NP-TPC-1"], ["NP-TPC-4"], ["NP=3"], ["NP-SBJ", "QP"], ["NP-SBJ-6"], ["UU"], ["PERPRES"], ["PARPOL"], ["ADVP-3"], ["ADVP=3"], ["SBAR-NOM-SBJ-1"], ["NP-SBJ-3", "QP"], ["UCP-TPC-1"]], "tag": ["<START>", "<STOP>", "UNK", "IN", "PRP", ",", "NN", "DT", "MD", "VB", "JJ", "-NONE-", ".", "NNP", "CC", "RB", "CD", ":", "FW", "-LRB-", "-RRB-", "SYM", "PRP$", "RP", "WP", "``", "''", "VBZ", "WRB", "UH", "IIN", "VIN", "WEN", "THEYN", "TRIWULANN"]}

entities_ontonotes5 = {"tag2idx": {"PAD": 0, "X": 1, "OTHER": 2, "ADDRESS": 3, "PERSON": 4, "NORP": 5, "FAC": 6, "ORG": 7, "GPE": 8, "LOC": 9, "PRODUCT": 10, "EVENT": 11, "WORK_OF_ART": 12, "LAW": 13, "LANGUAGE": 14, "DATE": 15, "TIME": 16, "PERCENT": 17, "MONEY": 18, "QUANTITY": 19, "ORDINAL": 20, "CARDINAL": 21}, "idx2tag": {
    "0": "PAD", "1": "X", "2": "OTHER", "3": "ADDRESS", "4": "PERSON", "5": "NORP", "6": "FAC", "7": "ORG", "8": "GPE", "9": "LOC", "10": "PRODUCT", "11": "EVENT", "12": "WORK_OF_ART", "13": "LAW", "14": "LANGUAGE", "15": "DATE", "16": "TIME", "17": "PERCENT", "18": "MONEY", "19": "QUANTITY", "20": "ORDINAL", "21": "CARDINAL"}}

entities = {"idx2tag": {"0": "PAD", "1": "X", "2": "OTHER", "3": "organization",
                        "4": "person", "5": "time", "6": "location", "7": "quantity", "8": "law", "9": "event"}}

pos = {"idx2tag": {"0": "PAD", "1": "X", "2": "PROPN", "3": "AUX", "4": "DET", "5": "NOUN", "6": "PRON", "7": "VERB",
                   "8": "ADP", "9": "PUNCT", "10": "ADV", "11": "CCONJ", "12": "SCONJ", "13": "NUM", "14": "ADJ", "15": "PART", "16": "SYM"}}

phoneme_left = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    ' ': 4,
    "'": 5,
    '-': 6,
    '`': 7,
    'a': 8,
    'b': 9,
    'c': 10,
    'd': 11,
    'e': 12,
    'f': 13,
    'g': 14,
    'h': 15,
    'i': 16,
    'j': 17,
    'k': 18,
    'l': 19,
    'm': 20,
    'n': 21,
    'o': 22,
    'p': 23,
    'q': 24,
    'r': 25,
    's': 26,
    't': 27,
    'u': 28,
    'w': 29,
    'y': 30,
    'z': 31
}

phoneme_right = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    ' ': 4,
    ')': 5,
    ',': 6,
    '.': 7,
    '/': 8,
    ':': 9,
    'A': 10,
    'C': 11,
    'E': 12,
    'I': 13,
    'N': 14,
    'S': 15,
    'Z': 16,
    'a': 17,
    'b': 18,
    'd': 19,
    'e': 20,
    'f': 21,
    'g': 22,
    'h': 23,
    'i': 24,
    'j': 25,
    'k': 26,
    'l': 27,
    'm': 28,
    'n': 29,
    'o': 30,
    'p': 31,
    'r': 32,
    's': 33,
    't': 34,
    'u': 35,
    'w': 36,
    'z': 37,
    '\x8d': 38,
    '«': 39,
    '\xad': 40,
    'Ä': 41,
    'Ò': 42,
    'Ö': 43,
    'â': 44,
    'ø': 45,
    'ù': 46
}