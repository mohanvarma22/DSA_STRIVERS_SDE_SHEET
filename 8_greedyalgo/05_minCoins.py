#greedy approach traverse from right 
if __name__ == '__main__':
    V = 49
    ans = []
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = 9
    for i in range(n - 1, -1, -1):
        while V >= coins[i]:
            V -= coins[i]
            ans.append(coins[i])
    print("The minimum number of coins is", len(ans))
    print("The coins are")
    for i in range(len(ans)):
        print(ans[i], end=" ")