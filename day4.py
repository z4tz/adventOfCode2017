from InputReader import read


def validPasswords(passwords):
    return sum([validatePassword(password) for password in passwords])


def validatePassword(password):
    words = password.split()
    c = set(words)
    if len(c) == len(words):
        return True
    return False


def validPasswordsB(passwords):
    return sum([validatePasswordB(password) for password in passwords])


def validatePasswordB(password):
    words = [''.join(sorted(word)) for word in password.split()]
    c = set(words)
    if len(c) == len(words):
        return True
    return False


def run(data):
    print validPasswords(data)
    print validPasswordsB(data)

if __name__ == "__main__":
    run(read('inputs/day4.txt'))
