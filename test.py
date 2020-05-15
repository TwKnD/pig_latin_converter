# initial versions
def to_pig(string):
    # english to pig  latin
    return ' '.join([(w[1:] + w[0] + 'ay') for w in string.split()])


def to_en(string):
    # pig latin to english
    return ' '.join([(w[-3:-2] + w[0]) for w in string.split()])


# check  for special char at end of str after space.
def e1(string):
    l1 = []
    for w in string.split():
        print(w)
        if w.isalpha():
            l1.append(w[1:] + w[0] + 'ay')
            print(l1)
        else:
            l1.append(w)
            print(l1)

    return ' '.join(l1)


def e1r(string):
    return ' '.join([w[1:]+w[0]+'ay' if w.isalpha()
                    else w for w in string.split()])


# check for special char at end of word.
def w1(string):
    l1 = []
    for w in string.split():
        print(w)
        if w[-1].isalpha():
            l1.append(w[1:] + w[0] + 'ay')
        else:
            l1.append(w[1:-1] + w[0] + 'ay' + w[-1])

    return ' '.join(l1)


# Combine both checks
def b1(string):
    # english to Pig Latin
    l1 = []
    for w in string.split():
        if not w[-1].isalpha() and w[:-1].isalpha():
            l1.append(w[1:-1] + w[0] + 'ay' + w[-1])
        elif not w.isalpha():
            l1.append(w)
        else:
            l1.append(w[1:] + w[0] + 'ay')

    return ' '.join(l1).capitalize()


def b2(string):
    # Pig Latin to english
    # ' '.join([(w[-3:-2] + w[0]) for w in string.split()])
    pass
#    l1 = []
#    for w in string.split():
#        if not w[-1].issalpha() and w[:-1].isalpha():
#            l1.append(w[-3]


# Tests ENG to PIG
print(b1('test test !'))
print(b1('test test!'))
print(b1('test test !!!'))
print(b1('This line, Is a test line.'))

# Tests PIG to  ENG
print(to_en('Esttay esstay !'))
print(to_en('Esttay esttay!'))
print(to_en('Esttay esttay !!!'))
print(to_en('Histay inelay, siay aay esttay inelay'))
