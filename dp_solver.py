# --- Constants for standard edit distance costs ---
COST_INSERTION = 1
COST_DELETION = 1
COST_SUBSTITUTION = 2

def solve_dynamic_programming(str1, str2):
    """
    Solves the alignment problem using classic dynamic programming.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 1. Initialize DP table
    for i in range(m + 1):
        dp[i][0] = i * COST_DELETION
    for j in range(n + 1):
        dp[0][j] = j * COST_INSERTION

    # 2. Fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sub_cost = 0 if str1[i - 1] == str2[j - 1] else COST_SUBSTITUTION
            
            cost_sub = dp[i - 1][j - 1] + sub_cost
            cost_del = dp[i - 1][j] + COST_DELETION
            cost_ins = dp[i][j - 1] + COST_INSERTION
            
            dp[i][j] = min(cost_sub, cost_del, cost_ins)

    final_cost = dp[m][n]

    # 3. Backtrack to find the alignment
    aligned1, aligned2 = [], []
    i, j = m, n
    while i > 0 or j > 0:
        sub_cost = 0 if i > 0 and j > 0 and str1[i - 1] == str2[j - 1] else COST_SUBSTITUTION
        
        # Check which move led to the current cell's value
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + sub_cost:
            aligned1.append(str1[i - 1])
            aligned2.append(str2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + COST_DELETION:
            aligned1.append(str1[i - 1])
            aligned2.append('-')
            i -= 1
        else: # (j > 0 and dp[i][j] == dp[i][j - 1] + COST_INSERTION)
            aligned1.append('-')
            aligned2.append(str2[j - 1])
            j -= 1
            
    return final_cost, "".join(reversed(aligned1)), "".join(reversed(aligned2))