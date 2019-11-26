from collections import Counter


def check_list_passphrases(passphrase_list, checks_anagrams=False):
    """
    Return the number of valid passphrases recive. They will be checked and declare
    invalid if they contains duplicate words.
    :param passphrase_list: List of passphrases to be verify.
    :type: List(str)
    :param checks_anagrams: When True passphrases will not be vlaid of they contains anagrams.
    :type: bool
    :return: Number of valid passphrases
    """
    valid_passphrase_list = [
        passphrase for passphrase in passphrase_list
        if _is_valid_passphrase(passphrase, checks_anagrams)
    ]
    return len(valid_passphrase_list)


def _is_valid_passphrase(passphrase, checks_anagrams=False):
    """
    Checks if passphrase is valid
    :param passphrase: String with words separated by space.
    :type: str
    :param checks_anagrams: When True passphrase should be checked for anagrams.
    :type: bool
    :return: True is String does no contains duplicates or anagrams if required.
    """
    words = passphrase.lower().split()
    if checks_anagrams and _has_anagrams(words):
        return False
    if _has_duplicates(words):
        return False
    return True


def _has_duplicates(words):
    """
    Returns True if list of words contains duplicates.
    """
    most_common = Counter(words).most_common(1)[0]
    if most_common[1] > 1:
        return True
    return False


def _has_anagrams(words):
    """
    Returns True if list of words contains anagrams.
    """
    return _has_duplicates([''.join(sorted(word)) for word in words])
