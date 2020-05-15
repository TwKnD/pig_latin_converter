# check  for special char at end of str after space.
def e1(string):
    l = []
    for w in string.split():
        print(w)
        if w.isalpha():
            l.append(w[1:] + w[0] + 'ay')
            print(l)
        else:
            l.append(w)
            print(l)

    return ' '.join(l)


def e1r(string):
    return ' '.join([w[1:]+w[0]+'ay' if w.isalpha() else w for w in string.split()])


# check for special char at end of word.
def w1(string):
    l = []
    for w in string.split():
        print(w)
        if w[-1].isalpha():
            l.append(w[1:] + w[0] + 'ay')
        else:
            l.append(w[1:-1] + w[0] + 'ay' + w[-1])

    return ' '.join(l)


# Combine both checks
def b1(string):
    l = []
    for w in string.split():
        if not w[-1].isalpha() and w[:-1].isalpha():
            l.append(w[1:-1] + w[0] + 'ay' + w[-1])
        elif not w.isalpha():
            l.append(w)
        else:
            l.append(w[1:] + w[0] + 'ay')

    return ' '.join(l)


print(b1('test test !'))
print(b1('test test!'))
print(b1('test test !!!'))
