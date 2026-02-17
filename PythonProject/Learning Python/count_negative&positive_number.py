data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

if __name__ == '__main__':
    negative_number = []
    positive_number = []

    for i in data1:
        if i >= 0:
            positive_number.append(i)
        else:
            negative_number.append(i)

print(f"Danh sách số âm: {negative_number} - {len(negative_number)}")
print(f"Danh sách số dương: {positive_number} - {len(positive_number)}")