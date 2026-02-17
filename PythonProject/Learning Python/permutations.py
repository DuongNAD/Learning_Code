data4 = [1, 2, 3]

if __name__ == '__main__':
    result = []
    for i in data4:
        for j in data4:
            for k in data4:
                if i != j and i != k and j != k:
                    result.append(i*100 + j*10 + k)

    print(result)