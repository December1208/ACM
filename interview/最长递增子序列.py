

if __name__ == '__main__':
    n_m = input().split()
    n, m = int(n_m[0]), int(n_m[1])
    input_second = set()
    for i in range(n):
        x_y = input().split()
        x, y = int(x_y[0]), int(x_y[1])
        input_second.add(x+y)

    second = list(input_second)
    second.sort()
    second_length = len(second)
    dp = [1] * second_length
    for i in range(second_length):
        for j in range(i):
            if second[i] - second[j] >= m and dp[j]+1>dp[i]:
                dp[i] = dp[j]+1
            else:
                if dp[j] > dp[i]:
                    dp[i] = dp[j]

    print(dp[-1])





