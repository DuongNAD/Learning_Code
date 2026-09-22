import numpy as np



def homework(a):
    result_list = []
    for i in a:
        if i % 5 == 0 and i % 2 == 1:
            result_list.append(i)

    result = np.array(result_list, dtype=a.dtype)
    return result

if __name__ == '__main__':
    a = np.array([1,5,10,3,4])
    print(homework(a))


