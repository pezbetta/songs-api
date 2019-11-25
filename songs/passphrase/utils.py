from collections import Counter


def check_list_passphrases(passphrase_list, checks_anagrams=False):
    valid_passphrase_list = [
        passphrase for passphrase in passphrase_list
        if check_if_valid_passphrase(passphrase, checks_anagrams)
    ]
    return len(valid_passphrase_list)


def check_if_valid_passphrase(passphrase, checks_anagrams=False):
    words = passphrase.lower().split()
    if check_if_invalid_on_repetitions(words):
        return False
    if checks_anagrams:
        if check_if_invalid_on_anagrams(words):
            return False
    return True


def check_if_invalid_on_repetitions(words):
    most_common = Counter(words).most_common(1)[0]
    if most_common[1] > 1:
        return True
    return False


def check_if_invalid_on_anagrams(words):
    most_common = Counter([
        ''.join(sorted(word)) for word in words
    ]).most_common(1)[0]
    if most_common[1] > 1:
        return True
    return False
