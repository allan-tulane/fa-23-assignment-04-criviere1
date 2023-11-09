# CMPS 2200 Assignment 4
## Answers

**Name: Collette Riviere**


Place all written answers from `assignment-04.md` here for easier grading.

**1a)** The greedy algorithm would be to take as many coins of the largest denomination as possible. Then you drop to the next denomination and do the same thing. This is continued until exact change is made. This is called "largest denomination first".

**1b)** If we say A is the optimal solution (optimal sequence of coins), then Ai is the number of coins of denomination 2^i. If we took two coins of 2^i value, they could be replaced by an 2^(i+1) coin, so taking more than 2 coins of 2^i (i less than k) would contradict optimality. So for any i < k (2^k is max coin denomination), Ai will be less than 2. So for the denomination 2^k, the max amount of coins must be selected, which is the greedy algorithm, so it is optimal.

**1c)** The algorithm has work os O(log n) and span of O(log n).



**2a)** If you want change for 20 and the bank has coin denominations of 1, 10, and 11, the greedy algorithm would take 1 coin of value 11 and 9 coins of value 1 while the optimal solution would be 2 coins of value 10.

**2b)** Let A(n,k) be the minimum number of coins to make change n using denominations of 0 to k (if it is not possible to make change, A is infinity). Because the solution is not greedy, the largest coin denomination may or maynot be used. If it is not used, then we don't need it and we can say A(n,k) = A(n,k-1). If it is used, we can say A(n,k) = 1 + A(n-D_k, k), where we can still consider using coin denomination D_k again to get change (n-D_k). So the optimal substructure can be written as: A(n,k) = min{A(n-D_k, k), 1 + A(n, k-1)}.

**2c)** If you use top-down or bottom-up memoization, the work and span are both O(nk) because the number of unique subproblems is nk and each minimization comparison takes O(1) so O(nk) * O(1) = O(nk).
