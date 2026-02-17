import math

dataset = [
    # Iris Setosa (Nhóm 1)
    [5.1, 3.5, "Iris-setosa"],
    [4.9, 3.0, "Iris-setosa"],
    [4.7, 3.2, "Iris-setosa"],
    [4.6, 3.1, "Iris-setosa"],
    [5.0, 3.6, "Iris-setosa"],

    # Iris Versicolor (Nhóm 2)
    [7.0, 3.2, "Iris-versicolor"],
    [6.4, 3.2, "Iris-versicolor"],
    [6.9, 3.1, "Iris-versicolor"],
    [5.5, 2.3, "Iris-versicolor"],
    [6.5, 2.8, "Iris-versicolor"],

    # Iris Virginica (Nhóm 3)
    [6.3, 3.3, "Iris-virginica"],
    [5.8, 2.7, "Iris-virginica"],
    [7.1, 3.0, "Iris-virginica"],
    [6.3, 2.9, "Iris-virginica"],
    [6.5, 3.0, "Iris-virginica"]
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

length = 5
width = 6

flower_input = [length, width]
flowers_class = calculate_mean_per_class(dataset)
distances = {}

for class_name, flowers in flowers_class.items():
    d = math.sqrt((flower_input[0] - flowers[0]) ** 2 + (flower_input[1] - flowers[1]) ** 2)
    distance_flower = round(d, 2)
    distances[class_name] = distance_flower

print(distances)
