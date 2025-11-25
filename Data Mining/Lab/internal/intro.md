## 🌳 1. Decision Tree
- A Decision Tree is a supervised machine learning model used for classification and regression.
    - It works like a flowchart: you keep splitting data based on the most informative features.

- How it works:
    - Select a feature that best separates the data
    (using Gini Index, Entropy, or Information Gain)
    - Split the dataset into branches
    - Repeat splitting until: nodes become pure or stopping criteria is met
    - Final leaf node gives the output class/value
- The Gini Index measures the probability of incorrectly classifying a randomly chosen sample if the node’s class distribution is used as a predictor.
    - Gini Index=1-∑pi^2.
     - Where: pi = proportion of class i in that node && k = number of classes
- Advantages
    - Easy to understand
    - Works with numerical + categorical data
    - No need for feature scaling

- Disadvantages
    - Can overfit
    - Unstable with small changes in data

- Applications
    - Medical diagnosis
    - Loan approval
    - Fraud detection
    - Classification tasks


## 📧 2. Naive Bayes Classifier
- A probabilistic classifier based on Bayes’ Theorem with the assumption of independence among features (hence “naive”).
- Formula:
> P(Class∣Features)= P(Features) / P(Features∣Class)⋅P(Class)

- Types
    - Gaussian Naive Bayes – continuous values
    - Multinomial Naive Bayes – text classification
    - Bernoulli Naive Bayes – binary features

- Advantages
    - Very fast
    - Works well with high-dimensional data
    - Excellent for text classification

- Disadvantages
    - Assumes independence, which may not always be true

- Applications
    - Email spam detection
    - Sentiment analysis
    - Document classification

## K-Means Clustering 
An unsupervised cluster algorithm that groups data into K clusters based on similarity (distance).

- How it works:
    1. Choose number of clusters K
    2. Randomly pick K centroids
    3. Assign each point to the nearest centroid
    4. Update centroids by averaging assigned points
    5. Repeat steps 3–4 until convergence

- Advantages
    - Simple and fast
    - Works well with large datasets

## 🔗 4. AGNES (Agglomerative Hierarchical Clustering)
(Agglomerative Nesting)
- A hierarchical clustering method that builds a tree-like structure called a dendrogram.
> Agglomerative = Bottom-Up

- Start with each data point as its own cluster
- Merge clusters step-by-step based on similarity
- Continue until all points merge into one cluster

- How clusters are merged?
- Using distance metrics like:
    - Single linkage (minimum distance)
    - Complete linkage (maximum distance)
    - Average linkage

Advantages
- No need to choose number of clusters initially
- Produces a hierarchy useful for exploration

Disadvantages
- Slow for large datasets
- Once clusters merge, they cannot be undone

Applications
- Gene expression analysis
- Taxonomy/classification trees
- Document clustering