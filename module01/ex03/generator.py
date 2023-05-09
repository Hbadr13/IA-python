import random


def ft_shuffle(lstt):
    new = []
    while len(lstt) > 0:
        index = random.choice(lstt)
        new.append(index)
        lstt.remove(index)
    return new


def ft_unique(lstt):
    new = []
    for word in lstt:
        new.append(word)
        for mot in lstt:
            if mot == word:
                lstt.remove(mot)
    return new


def ft_ordered(lstt):
    new = lstt
    i = 0
    while i < len(lstt) - 1:
        if lstt[i] > lstt[i + 1]:
            swap = lstt[i + 1]
            lstt[i + 1] = lstt[i]
            lstt[i] = swap
            i = -1
        if i == len(lstt) - 1:
            break
        i = i + 1
    return lstt


def generator(text, sep=" ", option=None):
    if not isinstance(text , str):
        print("ERROR")
        exit(1)
    t = text.split(sep)
    if option == "unique":
        lst = ft_unique(t)
    elif option == "shuffle":
        lst = ft_shuffle(t)
    elif option == "ordered":
        lst = ft_ordered(t)
    elif option == None:
        lst = t
    else:
        raise NotImplementedError("")
    for word in lst:
        yield word


# text = "Le Lorem Ipsum est simplement du faux texte."

# for word in generator(text, sep=" ", option="ordered"):
#     print(word)
