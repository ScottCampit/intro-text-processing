"""
main.py

"""

import contractions

from datasets import load_dataset
import spacy 

def fix_contractions(text:str):
    """Fix contractions in string of text"""
    all_words = list()
    for word in text.split():
        all_words.append(contractions.fix(word))

    return ' '.join(all_words)

def normalize_case(text:str):
    """Lowercase all text"""
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return ' '.join([token.text.lower() for token in doc])

if __name__ == "__main__":
    
    # 1. Load Blog Authorship Corpus dataset
    dataset = load_dataset("blog_authorship_corpus", split="train")
    text = dataset['text'][0]
    expanded_text = fix_contractions(text)
    all_lower_case = normalize_case(expanded_text)
    print(all_lower_case)