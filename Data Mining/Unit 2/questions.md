## Given the foliowing database, show all rules that one can generate from the set
--- 
- Confidence = sup(ABE)/ sup(antecedent)
![alt text](image.png)

## Maximal frequent itemsets are sufficient to determine all frequent itemsets with their supports. ??
- Answer: FALSE
Reason:
- Maximal frequent itemsets do not store support counts of their subsets.
- We can infer which subsets are frequent (because all subsets of a frequent itemset are frequent), but we cannot know their support values.
- Example:
- Suppose transactions produce these frequent itemsets:
- Frequent itemsets: {A}, {B}, {C}, {A,B}, {A,C}, {A,B,C}
- Maximal frequent itemset: {A,B,C} only.
- We cannot determine:
    - support({A})
    - support({A,B})
    - support({B,C})
- Only storing {A,B,C} does NOT give information about supports of its subsets.
- Hence maximal frequent itemsets are NOT sufficient to determine all supports.

## ✅ b) The set of all maximal frequent sets is the set of longest possible frequent sets.
- Answer: TRUE
Reason:
- A maximal frequent itemset is defined as a frequent itemset that has no frequent superset.
- That means:
- It is the longest possible frequent itemset in its branch of the lattice.
- You cannot add any more items to it while keeping it frequent.
- Example:
- Frequent itemsets:
{A}, {B}, {A,B}, {A,B,C}
- Maximal frequent itemset is: {A,B,C}
- Because no larger set containing A, B, C is frequent.
- Thus maximal frequent itemsets are exactly the longest frequent itemsets.

