data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

if __name__ == '__main__':
    unique_data = set(data2)
    array_greater_than_k =[]

    for i in unique_data:
        if data2.count(i) > k:
            array_greater_than_k.append(i)

    print(array_greater_than_k)
