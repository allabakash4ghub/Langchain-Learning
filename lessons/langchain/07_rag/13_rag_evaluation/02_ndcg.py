import math


# ============================================================
# Calculate DCG
# ============================================================

def dcg(relevance_scores):

    score = 0

    for rank, relevance in enumerate(
        relevance_scores,
        start=1
    ):

        score += (
            relevance /
            math.log2(rank + 1)
        )

    return score


# ============================================================
# Calculate NDCG
# ============================================================

def ndcg(relevance_scores):

    # Actual ranking
    actual_dcg = dcg(relevance_scores)

    # Ideal ranking
    ideal_scores = sorted(
        relevance_scores,
        reverse=True
    )

    ideal_dcg = dcg(ideal_scores)

    if ideal_dcg == 0:
        return 0

    return actual_dcg / ideal_dcg


# ============================================================
# Example 1
# ============================================================

ranking_1 = [3, 2, 1, 0]

print("Ranking 1:")
print(ranking_1)

print("DCG:", dcg(ranking_1))
print("NDCG:", ndcg(ranking_1))


# ============================================================
# Example 2
# ============================================================

ranking_2 = [0, 1, 3, 2]

print("\nRanking 2:")
print(ranking_2)

print("DCG:", dcg(ranking_2))
print("NDCG:", ndcg(ranking_2))


# ============================================================
# Example 3
# ============================================================

ranking_3 = [0, 0, 1, 2]

print("\nRanking 3:")
print(ranking_3)

print("DCG:", dcg(ranking_3))
print("NDCG:", ndcg(ranking_3))