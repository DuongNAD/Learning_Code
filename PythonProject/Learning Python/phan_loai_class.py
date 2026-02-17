import math

def calculate_euclidean_distance(point, points):
    distances = {}
    for i in points:
        d = math.sqrt((point[0] - i[0])**2 + (point[1] - i[1])**2)

        distances[tuple(i)] = d

    return min(distances.items(),key=lambda item: item[1])


if __name__ == "__main__":
    p1 = [1,2]
    p2 = [3,1]
    p3 = [2,3]

    p4 = [5,7]
    p5 = [8,5]
    p6 = [7,6]

    points = [p1,p2,p3,p4,p5,p6]
    class_point1 = [p1,p2,p3]
    class_point2 = [p4,p5,p6]

    h = input("Enter H point (x y): ")
    h_point = list(map(int, h.split()))

    result = calculate_euclidean_distance(h_point,points)
    result_point = list(map(float,result[0]))


    if(result_point in class_point1):
        print("Class 1")
    else:
        print("Class 2")
