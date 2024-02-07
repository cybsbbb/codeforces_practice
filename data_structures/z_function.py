## Leetcode: 3031

class Solution:
  def z_function(self, s):
    z, l, r, n = [0] * len(s), 0, 0, len(s)
    for i in range(1, n):
      if i < r:
        z[i] = min(r - i, z[i - l])

      while i + z[i] < n and s[i + z[i]] == s[z[i]]:
        z[i] += 1

      if i + z[i] > r:
        l, r = i, i + z[i]

    return z

  def minimumTimeToInitialState(self, s: str, k: int) -> int:
    z, n, res = self.z_function(s), len(s), 1

    for i in range(k, n, k):
      if z[i] == n - i:
        return res
      res += 1

    return res