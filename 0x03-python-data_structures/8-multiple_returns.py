#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple containing the length of the sentence
    and its first character (or None if empty).
    """
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
