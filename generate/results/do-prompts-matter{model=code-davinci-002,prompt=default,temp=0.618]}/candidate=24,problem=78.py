
class Solution:
    def solve(self, n, T, songs):
        """
        :type n: int
        :type T: int
        :type songs: List[List[int]]
        :rtype: int
        """
        dp = [[[0 for __ in range(3)] for ___ in range(T+1)] for ____ in range(n+1)]
        if songs[0][0] == 1:
            for i in range(1,4):
                if i != songs[0][1]:
                    dp[1][1][i-1] = 1
            dp[1][1][songs[0][1]-1] = 0
        else:
            dp[1][1][songs[0][1]-1] = 1
        
        for i in range(2, n+1):
            t = songs[i-1][0]
            g = songs[i-1][1]
            for j in range(1, T+1):
                for k in range(3):
                    if k+1 != g:
                        dp[i][j][k] = dp[i-1][j][k]
                    if j >= t:
                        dp[i][j][g-1] += dp[i-1][j-t][k]
        return sum(dp[n][T]) % 1000000007


if True:
    n, T = map(int, input().strip().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().strip().split())))
    s = Solution()
    result = s.solve(n, T, songs)
    print(result)