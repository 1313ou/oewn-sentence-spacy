import load_spacy as model
from case import is_punctuated


def main():
    examples = [
        "is anybody here",
        "The quick brown fox jumps over the lazy dog.",
        "a quick brown fox",
        "running fast",
        "She loves programming and solving complex problems.",
        "The cat sat on the mat.",
        "He was smoking.",
        "this is obvious",
        "obvious though this is ",
        "do you smoke",
    ]
    for input_text in examples:
        punctuation_result = is_punctuated(input_text, model.nlp)

        print(f"Text: {input_text}")
        print(f"Punctuation: {punctuation_result}")
        print("\n")


if __name__ == '__main__':
    main()
