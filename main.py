"""
main.py

"""

from datasets import load_dataset
import spacy 

if __name__ == "__main__":
    
    # 1. Load Blog Authorship Corpus dataset
    dataset = load_dataset("blog_authorship_corpus", split="train")
    print(dataset['text'][0])