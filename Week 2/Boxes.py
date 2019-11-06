a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
z = 0
# identity check
if a1 * b1 * c1 == a2 * b2 * c2:
    if a1 == a2 or a1 == b2 or a1 == c2:
        if b1 == a2 or b1 == b2 or b1 == c2:
            if c1 == a2 or c1 == b2 or c1 == c2:
                print('Boxes are equal')
if a1 * b1 * c1 < a2 * b2 * c2:
    if a1 <= a2 or a1 <= b2 or a1 <= c2:
        if b1 <= a2 or b1 <= b2 or b1 <= c2:
            if c1 <= a2 or c1 <= b2 or c1 <= c2:
                print('The first box is smaller than the second one')
if a1 * b1 * c1 > a2 * b2 * c2:
    if a1 >= a2 or a1 >= b2 or a1 >= c2:
        if b1 >= a2 or b1 >= b2 or b1 >= c2:
            if c1 >= a2 or c1 >= b2 or c1 >= c2:
                print('The first box is larger than the second one')
            else:
                print('Boxes are incomparable')
