import math
import pprint

# --- EXTENDED DATASET (60 SAMPLES) ---
# Mỗi lớp có 20 bông hoa để phục vụ bài toán thống kê Top 50 và KNN
dataset = [
    # --- CLASS 1: IRIS SETOSA (Đặc điểm: Ngắn và Bè) ---
    [5.1, 3.5, "Iris-setosa"], [4.9, 3.0, "Iris-setosa"], [4.7, 3.2, "Iris-setosa"],
    [4.6, 3.1, "Iris-setosa"], [5.0, 3.6, "Iris-setosa"], [5.4, 3.9, "Iris-setosa"],
    [4.6, 3.4, "Iris-setosa"], [5.0, 3.4, "Iris-setosa"], [4.4, 2.9, "Iris-setosa"],
    [4.9, 3.1, "Iris-setosa"], [5.4, 3.7, "Iris-setosa"], [4.8, 3.4, "Iris-setosa"],
    [4.8, 3.0, "Iris-setosa"], [4.3, 3.0, "Iris-setosa"], [5.8, 4.0, "Iris-setosa"],
    [5.7, 4.4, "Iris-setosa"], [5.4, 3.9, "Iris-setosa"], [5.1, 3.5, "Iris-setosa"],
    [5.7, 3.8, "Iris-setosa"], [5.1, 3.8, "Iris-setosa"],

    # --- CLASS 2: IRIS VERSICOLOR (Đặc điểm: Trung bình) ---
    [7.0, 3.2, "Iris-versicolor"], [6.4, 3.2, "Iris-versicolor"], [6.9, 3.1, "Iris-versicolor"],
    [5.5, 2.3, "Iris-versicolor"], [6.5, 2.8, "Iris-versicolor"], [5.7, 2.8, "Iris-versicolor"],
    [6.3, 3.3, "Iris-versicolor"], [4.9, 2.4, "Iris-versicolor"], [6.6, 2.9, "Iris-versicolor"],
    [5.2, 2.7, "Iris-versicolor"], [5.0, 2.0, "Iris-versicolor"], [5.9, 3.0, "Iris-versicolor"],
    [6.0, 2.2, "Iris-versicolor"], [6.1, 2.9, "Iris-versicolor"], [5.6, 2.9, "Iris-versicolor"],
    [6.7, 3.1, "Iris-versicolor"], [5.6, 3.0, "Iris-versicolor"], [5.8, 2.7, "Iris-versicolor"],
    [6.2, 2.2, "Iris-versicolor"], [5.6, 2.5, "Iris-versicolor"],

    # --- CLASS 3: IRIS VIRGINICA (Đặc điểm: Dài và Hẹp hơn Setosa) ---
    [6.3, 3.3, "Iris-virginica"], [5.8, 2.7, "Iris-virginica"], [7.1, 3.0, "Iris-virginica"],
    [6.3, 2.9, "Iris-virginica"], [6.5, 3.0, "Iris-virginica"], [7.6, 3.0, "Iris-virginica"],
    [4.9, 2.5, "Iris-virginica"], [7.3, 2.9, "Iris-virginica"], [6.7, 2.5, "Iris-virginica"],
    [7.2, 3.6, "Iris-virginica"], [6.5, 3.2, "Iris-virginica"], [6.4, 2.7, "Iris-virginica"],
    [6.8, 3.0, "Iris-virginica"], [5.7, 2.5, "Iris-virginica"], [5.8, 2.8, "Iris-virginica"],
    [6.4, 3.2, "Iris-virginica"], [6.5, 3.0, "Iris-virginica"], [7.7, 3.8, "Iris-virginica"],
    [7.7, 2.6, "Iris-virginica"], [6.0, 2.2, "Iris-virginica"]
]

def calculate_mean_per_class(dataset):
    """
    Tính trung bình cộng chiều dài và chiều rộng của từng dataset
    """

    grouped_data = {}

    for flower in dataset:
        length = flower[0]
        width = flower[1]
        class_name = flower[2]

        if class_name not in grouped_data:
            grouped_data[class_name] = []

        grouped_data[class_name].append([length, width])

    """
    Tính trung bình cộng đài hoa từng loại hoa 
    """
    average_data = {}

    for class_name in grouped_data:
        total_length = 0
        total_width = 0
        count = len(grouped_data[class_name])
        for flower in grouped_data[class_name]:
            total_length += flower[0]
            total_width += flower[1]

        average_length = total_length / count
        average_width = total_width / count

        average_length = round(average_length, 2)
        average_width = round(average_width, 2)

        average_data[class_name] = [average_length, average_width]

    return average_data

def find_max(dataset):
    """
    Tìm khoảng cách input(length, width) đầu vào tới class trung bình loài hoa ngắn nhất
    """
    grouped_data = {}
    for flower in dataset:
        length = flower[0]
        width = flower[1]
        class_name = flower[2]
        if class_name not in grouped_data:
            grouped_data[class_name] = []

        grouped_data[class_name].append([length, width])

    max_data = {}
    for class_name in grouped_data:
        flowers_list = grouped_data[class_name]

        max_length = max([flower[0] for flower in flowers_list])
        max_width = max([flower[1] for flower in flowers_list])

        max_data[class_name] = [max_length, max_width]
    return max_data

def find_class_flower(dataset, flower_input):
    all_distances = []
    for flower in dataset:
        d= math.sqrt((flower_input[0] - flower[0]) ** 2 + (flower_input[1] - flower[1]) ** 2)
        all_distances.append([flower[2], d])

    all_distances.sort(key=lambda x: x[1])

    while len(all_distances) > 0:
        min_distance = all_distances[0][1]
        candidates = []
        for f in all_distances:
            if f[1] == min_distance:
                candidates.append(f)

        candidate_class = set([f[0] for f in candidates])

        if len(candidate_class) == 1:
            class_name = list(candidate_class)[0]
            return [class_name, min_distance]
        else:
            remaining_flowers = []
            for f in all_distances:
                if f[1] > min_distance:
                    remaining_flowers.append(f)

            all_distances = remaining_flowers

    return 1


def find_top10_length_class_flower(data):
    grouped_data = {}
    for flower in data:
        length = flower[0]
        width = flower[1]
        class_name = flower[2]
        if class_name not in grouped_data:
            grouped_data[class_name] = []

        grouped_data[class_name].append([length, width])

    top10_class_flower ={}
    for class_name,flower_list in grouped_data.items():
        sorted_flower = sorted(flower_list, key=lambda x: x[0], reverse = True)
        top10 = sorted_flower[:10]

        top10_class_flower[class_name] = top10

    return top10_class_flower

def top50_max_distances_count_class_flower(data):
    grouped_data = []
    for flower in data:
        distance = flower[0] + flower[1]
        class_name = flower[2]

        grouped_data.append([class_name, distance])
    sorted_flower = sorted(grouped_data, key=lambda x: x[1], reverse=True)
    top50_max_distances = sorted_flower[:50]

    print(top50_max_distances)
    count_result = {
        "Iris-setosa": 0,
        "Iris-versicolor": 0,
        "Iris-virginica": 0
    }

    for flower in top50_max_distances:
        class_name = flower[0]

        if class_name in count_result:
            count_result[class_name] += 1

    for name, quantity in count_result.items():
        print(name, quantity)

def find_class_knn(dataset, flower_input):
    grouped_data = []
    for flower in dataset:
        distance = math.sqrt((flower_input[0] - flower[0]) ** 2 + (flower_input[1] - flower[1]) ** 2)
        class_name = flower[2]
        grouped_data.append([class_name, distance])

    grouped_data.sort(key=lambda x: x[1])
    i =7
    while i <= len(grouped_data):
        distance_flower = grouped_data[:i]

        class_flower = {}
        for flower in distance_flower:
            class_name = flower[0]
            if class_name in class_flower:
                class_flower[class_name] += 1
            else:
                class_flower[class_name] = 1

        max_class_flower = max(class_flower.values())

        class_flower_true = []
        for name,count in class_flower.items():
            if count == max_class_flower:
                class_flower_true.append(name)

        if (len(class_flower_true) == 1):
            return class_flower_true[0]
        else:
            i +=1

    return 2


if __name__ == "__main__":

    fake_dataset = [
        [0.5, 0.5, "Phe Đỏ"],

        [1.1, 0.0, "Phe Xanh"],
        [0.0, 1.1, "Phe Xanh"],

        [-2.0, -2.0, "Phe Vàng"],
        [-2.0, 2.0, "Phe Vàng"],
        [2.0, -2.0, "Phe Vàng"],
        [2.0, 2.0, "Phe Vàng"],
        [0.0, -3.0, "Phe Vàng"]
    ]
    data = dataset
    mean_result = calculate_mean_per_class(data)
    pprint.pprint(mean_result)
    print("\n")
    pprint.pprint(find_max(data))
    print("\n")


    pprint.pprint(find_top10_length_class_flower(data))
    print("\n")
    top50_max_distances_count_class_flower(data)
    print("\n")
    top50_max_distances_count_class_flower(data)
    print("\n")
    flower_input = [ 0, 0]
    if(find_class_flower(fake_dataset, flower_input) == 1):
        print(find_class_knn(fake_dataset, flower_input))
    else:
        print(find_class_flower(fake_dataset, flower_input))




