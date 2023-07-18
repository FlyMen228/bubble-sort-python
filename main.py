from random import randint


def main():

    array = [randint(-500, 500) for _ in range(10000)]

    bubble_sort(array)

    print(*array)


def bubble_sort(array):

    for i in range(len(array) - 1):

        break_point = False

        for j in range(len(array) - i - 1):

            if array[j] > array[j+1]:

                array[j], array[j+1] = array[j+1], array[j]

                break_point = True

        if break_point == False:

            break

    return array


if __name__ == "__main__":

    main()