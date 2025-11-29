## 
```yml
UNIT 5 – Complete Topic List
Cluster Analysis

Introduction to Cluster and Clustering

Features Required for Clustering Algorithms

Data Types and Dissimilarity Measures in Cluster Analysis

Categorization of Clustering Methods

Partitioning-Based Clustering

k-means Algorithms

k-Medoids Algorithms

PAM

CLARA

CLARANS

Hierarchical Clustering

Agglomerative Methods

Divisive Methods

AGNES

DIANA

BIRCH (crossed out in image but originally listed)

Density-Based Clustering

DBSCAN

OPTICS (crossed out in the image)

Outlier Analysis (also crossed out)

Web & Text Mining

Introduction to Web Mining

Introduction to Text Mining

Problem Discussion
```

## 1. Introduction to Cluster and Clustering
- Clustering is an unsupervised learning technique used to group similar data objects into clusters.
- Objects in the same cluster → high similarity
- Objects in different clusters → low similarity
- Applications
    - Market segmentation
    - Image segmentation
    - Document clustering
    - Bioinformatics
    - Fraud detection

## 2. Features Required for Clustering Algorithms
- Clustering algorithms require:
1. a) Feature Selection
- Choosing important attributes of data.

2. b) Feature Extraction
- Transforming data into meaningful features (e.g., PCA).

3. c) Normalization
Scaling values (0–1) to remove unit differences.

4. d) Distance or Similarity Measure
- Common measures:
    - Euclidean distance
    - Manhattan distance
    - Cosine similarity
    - Jaccard similarity

5. e) Cluster Validity Index
- Used to evaluate clustering quality:
    - Silhouette coefficient
    - Davies-Bouldin index

## 3. Data Types in Cluster Analysis
Clustering works on different types of variables:

1. a) Interval-scaled data
- Numerical values (e.g., age, height).

2. b) Binary data
- Two states: 0/1.

3. c) Nominal data
- Categories (e.g., color, gender).

4. d) Ordinal data
- Ranked/ordered (e.g., poor, good, excellent).

5. e) Mixed-type data
- Combination of numeric and categorical.


## 4. Dissimilarity Measures in Cluster Analysis
A dissimilarity (distance) measure quantifies how “different” two objects are.
- Common Distance Measures
1. Euclidean Distance
2. Manhattan Distance
3. Minkowski Distance
4. Cosine Distance
5. Jaccard Distance (for binary)
6. Hamming Distance

## 5. Categorization of Clustering Methods
Clustering techniques are generally categorized as:

1. Partitioning Methods
- k-means
- k-medoids

2. Hierarchical Methods
- Agglomerative
- Divisive

3. Density-Based Methods
- DBSCAN
- OPTICS

4. Grid-Based Methods
- STING

5. Model-Based Methods
- EM
- Gaussian Mixture Models

6. Constraint-Based Methods

## Partitioning-Based Clustering
1. k-means Algorithm
A popular clustering algorithm that partitions data into k clusters based on minimizing within-cluster variance.

- Steps
    - Choose k cluster centers randomly.
    - Assign each data point to the nearest centroid.
    - Recalculate centroids as mean of assigned points.
    - Repeat steps 2–3 until convergence.

- Advantages
    - Simple and fast
    - Works well with large datasets

- Disadvantages
    - Sensitive to initialization
    - Works only with numerical data
    - Assumes spherical clusters

2. k-Medoids Algorithms
Unlike k-means, k-medoids uses actual data points as cluster centers (medoids).
- Better for noisy and categorical data.
- A medoid is the most centrally located data point in a cluster (an actual object from the dataset), unlike a centroid which is a calculated mean.

### a) PAM (Partitioning Around Medoids)
- Select k medoids
- Assign data to closest medoid
- Try swapping medoids with non-medoids to reduce cost
- Computationally expensive for large datasets

#### Steps of the PAM Algorithm
PAM works in two phases:

1. BUILD Phase (Initialization)
Select k medoids from the dataset.
These are chosen to minimize total dissimilarity (distance) between data points and their medoids.

2. SWAP Phase (Optimization)
Try replacing a medoid with a non-medoid point.
Check if the total cost (sum of distances within clusters) decreases.
If it improves, accept the swap.
Continue until no better medoid can be found.


| Aspect         | PAM                               | K-Means                          |
| -------------- | --------------------------------- | -------------------------------- |
| Representative | Medoid (actual data point)        | Centroid (mean point)            |
| Robustness     | High (less sensitive to outliers) | Low (affected by extreme values) |
| Complexity     | Higher (slower on large data)     | Faster                           |


3. Hierarchical Clustering
    1. Agglomerative (Bottom-Up) Clustering
    - Begins with each object as a separate cluster
    - Merges clusters step-by-step based on similarity
    - Linkage Methods
        - Single linkage : 
            - make a triangular matrix of distances between points .
            - start with small distance and start make clusters . 
        - Complete linkage:
            - make a triangular matrix of distances between points .
            - make clusters and update distances of new clusters wrt to all ponts as max ( distance(c1,p) , distnace(c2,p) );
        - Average linkage
        - Ward’s method
    - Output
        - A dendrogram representing cluster formation

    2. Divisive (Top-Down) Clustering
    - Starts with one large cluster
    - Splits into smaller clusters recursively
    - Popular Methods
        - AGNES (Agglomerative Nesting)
        - DIANA (Divisive Analysis)


4. Density-Based Clustering
    1. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
    - Clusters are formed by dense regions of data separated by low-density areas.
    - Key Concepts
        - ε (epsilon): neighborhood radius
        - MinPts: minimum points required to form dense region
        - Core Points
        - Border Points
        - Noise/Outliers
    - steps:
    1. calculate distnaces .
    2. Make clusters wrt epsilon.
    3. identify borders which are in any of the clusters .
    4. some will be noises .
    - Advantages
        - Detects arbitrarily shaped clusters
        - Detects noise and outliers
        - No need to specify number of clusters
    - Disadvantages
        - Choosing ε and MinPts is difficult
        - Not suitable for high-dimensional data
