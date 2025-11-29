## 1. Association Rule Mining (ARM)
- Association Rule Mining discovers relationships among items in large transactional datasets.
- Example Rule
- If a customer buys Bread and Butter, they are likely to buy Milk.
- Written as:
> {Bread, Butter} → {Milk}

## 2. Market Basket Analysis
- MBA is a major application of ARM that analyzes customer purchasing behavior.
- Goals:
    - Identify items frequently bought together
    - Suggest product placement
    - Build recommendation systems
    - Improve cross-selling

## 3. Frequent Itemsets
- A frequent itemset is a set of items that appear together in a dataset with support ≥ minimum support threshold.
- Support(X) = Number of transactions containing 𝑋 / Total number of transactions
- Frequent itemsets are backbone of association rules.

## Closed Itemsets
- An itemset is closed if no superset has the same support count.
- Why important?
    - Reduces number of patterns
    - Eliminates redundant itemsets
    - More compact representation
- Example:
If itemset {A,B} has support 10 and its superset {A,B,C} also has support 10 → {A,B} is not closed.

## 5. Maximal Frequent Itemsets
- A frequent itemset is maximal if none of its supersets is frequent.
- Importance:
    - Provides most compact representation
    - Identifies boundaries of large frequent patterns

## 6. Association Rules
- Association rules describe relationships of the form:
- 𝑋 → 𝑌 
- Where X and Y are disjoint itemsets.

> Confidence(X→Y)= Support(X) / Support(X∪Y)
- Meaning: if X occurs, how often Y also occurs.

> Lift(X→Y)= Confidence(X→Y) /  Support(Y).
- Lift is a measure used to evaluate the strength of an association rule in market basket analysis.
- Lift > 1 → positive correlation
- Lift = 1 → independence
- Lift < 1 → negative correlation

## 7. Apriori Algorithm (Mining Frequent Itemsets Using Candidate Generation)
- Apriori is a classic algorithm for mining frequent itemsets.
- Key Concept — Apriori Property
    - All subsets of a frequent itemset must also be frequent.
    - Allows pruning of search space.
- Steps of Apriori Algorithm
    - Generate C1: list all candidate 1-itemsets
    - Prune to get L1: keep only frequent ones
    - Use Lk to generate C(k+1) (candidate generation)
    - Prune candidates using Apriori property
    - Count support of candidates
    - Generate L(k+1)
    - Stop when no more itemsets can be generated
- Time complexity is high due to:
    - Huge number of candidates
    - Multiple database scans

## 8. Generating Association Rules from Frequent Itemsets
- Steps:
- For each frequent itemset L, generate all possible rules
- Example: L = {A,B,C} → candidates:
    - A → BC
    - B → AC
    - C → AB
    - AB → C
    - AC → B
    - BC → A
- Compute confidence for each rule
- Keep rules with confidence ≥ minimum confidence threshold
- Often requires computing Lift, Leverage, Conviction etc.

## 9. Improving the Efficiency of Apriori Algorithm
- Apriori is slow due to heavy candidate generation and multiple scans.
- Efficiency can be improved using:
1. a) Hash-based technique
- Hash itemsets during candidate generation → prune unlikely candidates early.

2. b) Transaction reduction
- Remove transactions that do not contain any frequent itemsets.

3. c) Partitioning method
- Divide database into partitions.
- Frequent itemsets in each partition → possible global frequent itemsets.

4. d) Sampling
= Mine a smaller random sample of transactions.

5. e) Dynamic itemset counting (DIC)
- Count itemsets dynamically while reading database.

## 10. FP-Growth Algorithm (Frequent Pattern Growth)
- FP-Growth solves the problem of Apriori by avoiding candidate generation entirely.
- FP-Growth: Steps
1. Step 1: Build FP-tree
    - Scan database to get support of each item
    - Keep only frequent items
    - Sort items in descending frequency
    - Insert transactions into FP-tree
- FP-tree is a compressed representation of database.

2. Step 2: Mine the FP-tree
- FP-Growth uses divide-and-conquer:
- For each item:
    - Consider item as suffix pattern
    - Build its conditional pattern base
    - Build conditional FP-tree
    - Recursively mine conditional FP-tree
    - Combine results → frequent itemsets

- Advantages of FP-Growth
    - No candidate itemset generation
    - Only two scans of database
    - Much faster and more scalable than Apriori
    - Works well on dense datasets

## 11. Mining Frequent Itemsets Without Candidate Generation
- This specifically refers to FP-Growth, H-Mine, ECLAT, etc.
- Techniques:
    - Pattern growth methods (FP-growth)
    - Vertical data formats (ECLAT)
    - Diffsets

## 12. Mining Closed and Max Frequent Itemsets
- Closed Itemset Mining
- Goal: find all closed frequent itemsets.
- Uses algorithms such as:
    - CLOSET
    - CHARM
    - CLOSET+
- Maximal Frequent Itemset Mining
- Goal: find all maximal itemsets.
- Algorithms include:
    - MaxMiner
    - GenMax
    - FPMax

