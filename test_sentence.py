import load_spacy as model
from sentence import parse_sentence


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
        sentence_result, parsed = parse_sentence(input_text, model.nlp)

        print(f"Text: {input_text}")
        print(f"Deps: {parsed}")
        print(f"Sentence: {sentence_result}")
        print("\n")


if __name__ == '__main__':
    main()
