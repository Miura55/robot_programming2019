# coding: utf-8

def knapsack(W,weight,value):
    N = len(weight)
    inf=float("inf")
    dp=[[-inf for i in range(W+1)] for j in range(N+1)]
    for i in range(W+1):
        dp[0][i]=0

    #動的解析法
    for i in range(N):
        for w in range(W+1):
            if weight[i]<=w:
                dp[i+1][w]=max(dp[i][w-weight[i]]+value[i], dp[i][w])
            else:
                dp[i+1][w]=dp[i][w]
    print(dp)
    return dp[N][W]

if __name__ == "__main__":
    limit = 21
    weights = [11, 2, 3, 1, 4, 6, 8, 2, 4, 7, 5, 9, 3, 8, 10, 12, 5, 1, 6, 5]
    values = [15, 3, 2, 2, 4, 5, 7, 2, 5, 6, 8, 10, 4, 10, 11, 13, 9, 1, 6, 6]
    res = knapsack(limit, weights, values)
    print("Max_value: " + str(res))
