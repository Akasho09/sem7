## Association rule mining 
is a technique in data mining that finds interesting relationships (associations) among a large set of data items. It’s commonly used to uncover patterns in transactional datasets, such as in market basket analysis.

### 📌 1. Market Basket Analysis
- Analyzes the purchase behavior of customers by finding associations between items bought together.
- Example: If customers buy bread, they are likely to also buy butter.
- Used in retail for cross-selling, promotions, product placement.

### 📌 2. Frequent Itemsets, Closed Itemsets
- Itemset : 
    - collection of one or more items .
    - eg: { Milk , Bread , Diaper }
- Support count (sigma) 
    - Freq of occurence of a itemset
- Support : 
    - Fraction of Support count .
- Lift = s(A union B)/ s(A).s(B).
- Lift measures how much more likely A and B occur together compared to if they were independent.

- ✅ Frequent Itemsets
    - Itemset whose support is greater than minSup(user defined).
    - Example: {milk, bread} occurs in 40% of all transactions → frequent wrt 30%(minSup)
    - If a itemset is frequent then all its subsets are frequent .
    - If a itemset is Infrequent then all its superSets are Infrequent .

- ✅ Closed Itemsets
    - Frequent itemsets for which none of their supersets have the same frequency.
    - freq + no immediate superset has same support .
    - Helps reduce redundant patterns.

- Maximal Itemset :
    - Freq + no Immediate superset is frequent.


### ✅ Association Rules
    - Implication expressions in the form A → B, meaning if A occurs, B is likely to occur.
    - Example: {bread} → {butter} means if a customer buys bread, they are likely to buy butter.

#### Support and Confidence for Association Rule.
- For A->B , Following conditions shoukd satisfy : 
    - ✅ Support
        - Support refers to the relative frequency of an item set in a dataset. 
        - S = sigma(A union B)/Total 

    - ✅ Confidence
        - Measures the reliability of the inference made by the rule.
        - Confidence is a measure that indicates how likely it is that item Y will appear in a transaction given that item X is already in the transaction.
        - Confidence = Support(A union B)/Support(A).
    
    - Lift :
        - In data mining, lift is a measure that evaluates the effectiveness of a predictive model or association rule by comparing its results to a random chance baseline.
        

> Support >= minSup Threshold
> Confidence >= minConf Threshold


### 📌 4. Apriori Algorithm for Mining Frequent Itemsets
The Apriori algorithm is one of the earliest and most popular algorithms for finding frequent itemsets using candidate generation.

- ➤ Key Steps:
    - Generate candidate itemsets of length k from frequent itemsets of length k−1.
    - Count the occurrences of these candidates in the dataset.
    - Prune candidates that don’t meet the minimum support threshold.
    - Repeat until no more frequent itemsets are found.

- ➤ Example workflow:
    - Find frequent 1-itemsets (e.g., {milk}, {bread}).
    - Use them to generate candidate 2-itemsets (e.g., {milk, bread}).
    - Count support and prune those below the threshold.
    - Continue for 3-itemsets, 4-itemsets, etc.

- start with 1 length fre items and continue to +1 length with only freq items => reduced complexity.


### 📌 5. Generating Association Rules from Frequent Itemsets
- to get subsets A,B from freqs calculated 
 => start with PQRS=>{}
 the PQR=>S ,   PQS=>R ,...
 ... So on ....

- if Confidence is lesser => lower levels can be ommited .
