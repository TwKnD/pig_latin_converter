# check  for special char at end of str after space.
def c1(string):
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


def c1r(string):
    return ' '.join([w[1:]+w[0]+'ay' if w.isalpha() else w for w in string.split()])


# check for special char at end of word.



print(c1r('test test !'))
print(c1r('test test!'))
print(c1r('test test !!!'))
