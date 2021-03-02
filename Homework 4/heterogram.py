def heterogram(text):
    text = list(text)
    print(text)

    if len(text) == len(set(text)):
        print('Yes')
    else:
        print('No')


text = input('Write the sentance ')
heterogram(text)
