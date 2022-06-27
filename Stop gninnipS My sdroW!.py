def spin_words(sentence):
    sentence = sentence.split(' ')
    new=[]
    for i in sentence:
        if len(i)>=5 and '!' in i:
            i=i.replace('!', '')
            i = i[::-1]+'!'
            new.append(i)
            print(i)
        elif len(i)>=5:
            i = i[::-1]
            new.append(i)
        else:
            new.append(i)
    print(sentence)
    new = ' '.join(new)
    print(new)
    return new
