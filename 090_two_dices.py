#Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.
#
#For example, the square number 64 could be formed:
#
#In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.
#
#For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
#
#However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.
#
#In determining a distinct arrangement we are interested in the digits on each cube, not the order.
#
#{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
#
#But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
#
#How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
pairs = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]
def is_satisfyable(set1, set2):
    if 6 in set1 or 9 in set1:
        set1.update(set([6,9]))
    if 6 in set2 or 9 in set2:
        set2.update(set([6,9]))
    for pair in pairs:
        if not((pair[0] in set1 and pair[1] in set2) or
            (pair[0] in set2 and pair[1] in set1)):
            return False
    return True

count_sets = 0
for first in range(7):
    for second in range(first+1,8):
        for third in range(second+1,9):
            for forth in range(third+1,10):
                set1 = set([i for i in range(10)]) - set([first, second, third, forth])
                for fifth in range(7):
                    for sixth in range(fifth+1,8):
                        for seventh in range(sixth+1,9):
                            for eighth in range(seventh+1,10):
                                set2 = set([i for i in range(10)]) - set([fifth, sixth, seventh, eighth])
                                if is_satisfyable(set1, set2):
                                    count_sets += 1
print count_sets/2
#1217

