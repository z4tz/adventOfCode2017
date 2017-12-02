from InputReader import read


def solveCaptcha(captcha):
    numberList = captcha + captcha[0]
    captchaSum = 0
    for i in xrange(0,len(numberList)-1):
        if numberList[i] == numberList[i+1]:
            captchaSum += int(numberList[i])
    return captchaSum


def solveCaptchaB(captcha):
    captchaSum = 0
    for A, B in zip(captcha[:len(captcha)/2-1], captcha[len(captcha)/2:]):
        if A == B:
           captchaSum += int(A)
    return captchaSum*2


def run(data):
    print solveCaptcha(data[0])
    print solveCaptchaB(data[0])


if __name__ == "__main__":
    run(read('inputs/day1.txt'))
