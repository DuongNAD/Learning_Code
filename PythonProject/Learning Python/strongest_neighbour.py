data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
k = 2

if __name__ == "__main__":

    result = []

    for i in range(len(data3) - k +1):
        current_window = data3[i:i+k]
        result.append(max(current_window))

print(result)