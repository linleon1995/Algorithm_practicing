# AICS


def matrix_reshape(a, row, col):
    size = len(a) * len(a[0])
    assert size%(row*col)==0
    # b = row*[col*[0]]
    b = [list(range(row)) for _ in range(col)]
    x = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            x.append(a[i][j])
    
    c = 0
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j] = x[c]
            c += 1
    return b

if __name__ == "__main__":
    a = [[1,2],[3,4]]
    a2 = [[1,2,3],[4,5,6]]
    print(a2)
    b = matrix_reshape(a2, row=2, col=3)
    print(b)