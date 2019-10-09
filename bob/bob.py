"""
This module represents Bob following this logic:
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.
    Bob answers 'Sure.' if you ask him a question.
    He answers 'Whoa, chill out!' if you yell at him.
    He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
    He says 'Fine. Be that way!' if you address him without actually saying anything.
    He answers 'Whatever.' to anything else.

    extending
    He answers 'mmm... OK' if you use the word 'please'
    He answers "that's me" if you mention his name unless you're yelling at him

"""

from typing import Dict


class PhraseAnalysis:
    """
    this class performs a basic analysis of the input phrase and returns true / false for each method that
    is used
    """

    @staticmethod
    def is_question(phrase: str) -> str:
        return phrase[-1] == "?"

    @staticmethod
    def is_yell(phrase: str) -> str:
        return phrase.isupper()

    @staticmethod
    def is_yell_question(phrase: str) -> str:
        return phrase[-1] == "?" and phrase.isupper()

    @staticmethod
    def is_address(phrase: str) -> str:
        return phrase.strip() == ''


def bob_response() -> Dict:
    """
    this function returns the possible responses of Bob to different phrases
    :return: a dict of phrase type and the adequate response message
    """
    response = dict()
    response['question'] = "Sure."
    response['yell'] = "Whoa, chill out!"
    response['yell_question'] = "Calm down, I know what I'm doing!"
    response['address'] = "Fine. Be that way!"
    response['other'] = "Whatever."

    return response


def get_phrase_type(phrase: str) -> str:
    """
    this function gets the phrase and returns the type of the phrase
    :param phrase:
    :return: type of the phrase
    """
    if phrase == "":
        return "address"
    elif PhraseAnalysis.is_yell_question(phrase):
        return "yell_question"
    elif PhraseAnalysis.is_question(phrase):
        return "question"
    elif PhraseAnalysis.is_yell(phrase):
        return "yell"
    elif PhraseAnalysis.is_address(phrase):
        return "address"
    else:
        return "other"


def hey(phrase: str) -> str:
    """
    this function gets the phrase and returns Bob's response to the phrase
    the phrase that is passed to the analysis function is stripped from spaces and special
    characters as /n /t
    :param phrase:
    :return: Bob's response to the phrase
    """
    if not isinstance(phrase, str):
        raise Exception("Must use strings as an input")
    bobs_responses = bob_response()
    phrase_type = get_phrase_type(''.join(phrase.split()))

    return bobs_responses[phrase_type]


if __name__ == '__main__':
    PHRASE = "\n\r \t"
    print(hey(PHRASE))
