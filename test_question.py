import load_spacy as model
from question import is_direct_question

def main():
    # Load the SpaCy English model
    examples = [
        "Is this a question?",
        "What time is it?",
        "This is not a question.",
        "Can you help me?",
        "The sky is blue.",
        "To whom should I address this letter?",
        "Do you know the way to San Jose?",
        "Could I borrow your pen?",
        "You're coming to the party, aren't you?",
        "She likes ice cream, doesn't she?",
        "Why not try again?",
        "How about we go for a walk?",
        "Where did you put my keys?",
        "Have you ever been to Paris?",
        "Shall we dance?",
        "Would you mind passing the salt?",
        "Who wants ice cream?",
        "Which option do you prefer?",
        "When does the movie start?",

        "How come you didn't call?",
        "What if we tried a different approach?",
        "Could you tell me where the bathroom is?",
        "I wonder if you could help me.",
        "Do you know what time it is?",
        "Ready?",
        "Finished?",
        "Your name?",
    ]
    for input_text in examples:
        question_result = is_direct_question(input_text, model.nlp)

        print(f"Text: {input_text}")
        print(f"Question: {question_result}")
        print("\n")


if __name__ == '__main__':
    main()
