import math


if __name__ == '__main__':

    input_list = input().split(' ')
    x, y = int(input_list[0]), int(input_list[1])
    char_count = pow(26, y)
    int_count = math.ceil(x/char_count)
    result = math.ceil(math.log(int_count, 10))
    result = 1 if result == 0 else result
    print(result)


