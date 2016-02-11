from random import shuffle, randint


def quicksort(lst):  # n log n best/average, n2 worst, log n memory
    if len(lst) < 2:
        return lst

    # 1. get pivot (random element)
    pivot = lst[randint(0, len(lst) - 1)]

    # 2. put all smaller to left, into a group
    left = [e for e in lst if e is not pivot and e <= pivot]

    # 3. put all greater to right, into a group
    right = [e for e in lst if e is not pivot and e > pivot]

    # repeat for those 2 new groups
    return quicksort(left) + [pivot] + quicksort(right)


def mergesort(lst):  # n log n best/average/worst, n memory
    if len(lst) < 2:
        return lst

    # split in half
    left = lst[0:len(lst) // 2]
    right = lst[len(lst) // 2:]

    # sort halves
    left = mergesort(left)
    right = mergesort(right)

    # merge them together into sorted final
    sorted = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    if i < len(left):
        sorted.extend(left[i:])
    else:
        sorted.extend(right[j:])

    return sorted


def heapsort(lst):  # n log n best/average/worst, 1 memory
    if len(lst) < 2:
        return lst

    tree = lst.copy()

    def swap(i1, i2):
        temp = tree[i1]
        tree[i1] = tree[i2]
        tree[i2] = temp

    # make parent nodes smaller than children
    def heapify():
        reheap = False
        for parenti in range(len(tree)):
            lefti = parenti * 2 + 1
            righti = lefti + 1
            if lefti < len(tree) and tree[lefti] < tree[parenti]:
                swap(lefti, parenti)
                reheap = True
            elif righti < len(tree) and tree[righti] < tree[parenti]:
                swap(righti, parenti)
                reheap = True

        if reheap:
            heapify()

    heapify()

    sorted = []

    def sift_down():
        if len(tree) is 0:
            return

        # move root to sorted, put last in its place
        sorted.append(tree[0])
        tree[0] = tree[len(tree) - 1]
        del tree[len(tree) - 1]

        # sift that one down (let smallest child go up)
        currenti = 0
        lefti = currenti * 2 + 1
        righti = lefti + 1
        while lefti < len(tree):  # has a child
            if righti >= len(tree):  # no right child
                if tree[lefti] < tree[currenti]:
                    swap(lefti, currenti)
                    currenti = lefti
                else:
                    break
            else:  # two children
                if tree[lefti] < tree[currenti] and tree[lefti] < tree[righti]:
                    swap(lefti, currenti)
                    currenti = lefti
                elif tree[righti] < tree[currenti] and tree[lefti] > tree[righti]:
                    swap(righti, currenti)
                    currenti = righti
                else:
                    break
            lefti = currenti * 2 + 1
            righti = lefti + 1
        sift_down()

    sift_down()

    return sorted


def bubblesort(lst):  # n best, n2 average/worst, 1 memory
    newlist = lst.copy()

    # for every 2 elements, shuft the smaller one up
    issorted = True
    for i in range(len(newlist)):
        nexti = i + 1
        if nexti < len(lst):
            if newlist[nexti] < newlist[i]:
                temp = newlist[i]
                newlist[i] = newlist[nexti]
                newlist[nexti] = temp
                issorted = False

    if not issorted:
        newlist = bubblesort(newlist)

    return newlist


def treesort(lst): #n log n best/average, n2 worst
    newlist = lst.copy()

    # put all in a binary tree where left child is less than parent and right child is greater
    tree = [None for count in range(2 ** (len(newlist) + 1))]
    randomidx = randint(0, len(newlist) - 1)
    tree[0] = newlist[randomidx]  # root = random element
    del newlist[randomidx]
    for e in newlist:
        parenti = 0
        while tree[parenti] is not None:
            lefti = parenti * 2 + 1
            righti = lefti + 1
            if e < tree[parenti]:
                if tree[lefti] is None:
                    tree[lefti] = e
                    break
                else:
                    parenti = lefti
                    continue
            else:
                if tree[righti] is None:
                    tree[righti] = e
                    break
                else:
                    parenti = righti
                    continue
    sorted = []

    # traverse fully left then fully right
    def traverse(parenti):
        lefti = parenti * 2 + 1
        righti = lefti + 1
        if tree[lefti] is not None:
            traverse(lefti)
        sorted.append(tree[parenti])
        if tree[righti] is not None:
            traverse(righti)

    traverse(0)
    return sorted


def radixsort(lst): #nk best/average/worst, n+k memory
    def digitat(idx, num):
        return num % 10 ** (idx + 1) // 10 ** idx

    # make buckets with indices
    buckets = [[] for count in range(10)]

    # for every last digit of number to first put that number in bucket index of that digit and reorder the numbers according to indices
    mostdigits = 1
    for e in lst:
        digits = len(str(e))
        if digits > mostdigits:
            mostdigits = digits

    newlist = lst.copy()
    for i in range(mostdigits):
        templist = newlist.copy()
        newlist.clear()
        for e in templist:
            buckets[digitat(i, e)].append(e)
        for bucket in buckets:
            newlist.extend(bucket)
        for bucket in buckets:
            bucket.clear()

    return newlist


def insertionsort(lst): #n best, n2 average/worst, 1 memory
    if len(lst) < 2:
        return lst

    newlist = lst.copy()

    def swap(i1, i2):
        temp = newlist[i1]
        newlist[i1] = newlist[i2]
        newlist[i2] = temp

    #for every element, insert it into the correct position of everything previous by "bubbling" it down
    for elemidx in range(1, len(newlist)):
        for i in range(elemidx):
            if newlist[elemidx] < newlist[i]:
                swap(elemidx, i)

    return newlist


def selectionsort(lst): #n2 best/average/worst, 1 memory
    newlist = lst.copy()
    sorted = []

    #get smallest, repeat and repeat and repeat.
    while len(newlist):
        smallest = newlist[0]
        for e in newlist:
            if e < smallest:
                smallest = e

        sorted.append(smallest)
        newlist.remove(smallest)

    return sorted


l = [152, 122, 321, 222, 521]

shuffle(l)
print('quicksort', l, quicksort(l))

shuffle(l)
print('mergesort', l, mergesort(l))

shuffle(l)
print('heapsort', l, heapsort(l))

shuffle(l)
print('bubblesort', l, bubblesort(l))

shuffle(l)
print('treesort', l, treesort(l))

shuffle(l)
print('radixsort', l, radixsort(l))

shuffle(l)
print('insertionsort', l, insertionsort(l))

shuffle(l)
print('selectionsort', l, selectionsort(l))