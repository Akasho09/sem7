## Single Linkage Clustering | Agglomerative Clustering :
- Single linkage clustering is one of the simplest forms of agglomerative hierarchical clustering.
- Agglomerative = Bottom-Up Approach
    - Start with each data point as its own cluster
    - Repeatedly merge the two closest clusters
    - Continue until only one cluster remains (or until a stopping condition)

## Complete Linkage Clustering | Agglomerative Clustering :
- Complete linkage clustering is a type of agglomerative (bottom-up) hierarchical clustering method.
- Agglomerative = Start with each point as its own cluster
- Then repeatedly merge clusters based on a distance rule.
> d(A,B)=i∈A,j∈B max​ d(i,j)
- Because of this, complete linkage is also called:
    - Furthest-neighbor clustering
    - Maximum linkage

## K-medoids Clustering :
- K-Medoids is a partitioning clustering algorithm similar to k-means, but instead of using the mean, it chooses an actual data point (called a medoid) as the center of each cluster.
- A medoid is the object in a cluster whose average dissimilarity (distance) to all other points in the cluster is minimum.

### ✅ Why K-Medoids?
- Because K-means is sensitive to outliers, since means shift easily.
- K-Medoids is more robust because:
    - Medoid = actual point
    - Extreme values affect it less

### steps:
1. Select k representative points randomly as medoids.
2. Step 2 — Assign Points to Nearest Medoid
3. Step 3 — Update Medoids
- For each cluster:
    - Try selecting every non-medoid point as a potential medoid.
    - Compute total clustering cost = sum of distances from all points to the medoid.
    - Choose the candidate point that gives the lowest total cost.
4. Step 4 — Iterate
- Repeat:
    - Reassign points
    - Recompute best medoid
- Until:
- Medoids do not change anymore
or
- Maximum number of iterations reached.


## Both k-means and k-medoids algorithms can perform effective clustering. Illustrate the strength and weakness of k-means in comparison with the k-medoids
- k-means: represents each cluster by its centroid (mean of points). Minimizes sum of squared Euclidean distances.
- k-medoids: represents each cluster by an actual data point (medoid) — the point with minimum total dissimilarity to other points in the cluster. Can use arbitrary distance/dissimilarity.

### 🔸 Strengths of k-means
1. Fast and scalable
- Complexity roughly  O(n⋅k⋅t⋅d) where 
- n=points, 
- k=clusters, 
- t=iterations, 
- d=dimensions. Works well on large datasets.

2. Simple & easy to implement
- Very few implementation details; many optimized libraries.

3. Good for compact, spherical clusters
- When clusters are roughly spherical and similar size, k-means is excellent.

4. Works with continuous numeric data (means are meaningful)
- Converges quickly in practice

5. Minimizes SSE (sum of squared errors), converges to a local optimum.

### Weaknesses of k-means
1. Sensitive to outliers and noise
- A single extreme point can move the centroid and distort clustering.

2. Requires numeric data and Euclidean geometry
- Centroid (mean) only makes sense for continuous attributes.

3. Assumes spherical clusters of similar size
- Performs poorly for clusters with different shapes, sizes, or densities.

4. Centroid not necessarily a real data point
- Less interpretable when you want a representative example.

5. Sensitive to initialization
- Different seeds → different local minima. (Mitigations: k-means++, multiple restarts.)

### Strengths of k-medoids
1. Robust to outliers and noise
- Medoid is an actual central point; outliers won’t drag it as centroid is dragged.

2. Works with arbitrary distance/dissimilarity
- Can use Manhattan, Gower (mixed data), categorical dissimilarities, etc.

3. Medoid is interpretable
- Each cluster center is an actual data item (useful for prototypes).

4. Better for non-Euclidean data or mixed attributes
- Because it uses pairwise dissimilarities only.

### Weaknesses of k-medoids
1. Slower / less scalable (naive PAM)
- PAM (Partitioning Around Medoids) has high cost: often O(k(n−k)^2) per iteration in basic form — expensive for large n. Variants (CLARA, CLARANS) try to improve scalability.

2. Still assumes partitioning into k clusters
- Like k-means, needs k and can get stuck in local optima.

3. Quality depends on chosen dissimilarity
- Good choice of distance function is required.

4. Fewer optimized, highly parallel implementations (compared to k-means)

| Feature                      |                                   k-means | k-medoids                                  |
| ---------------------------- | ----------------------------------------: | ------------------------------------------ |
| Cluster center               | Centroid (mean) — may not be a data point | Medoid — actual data point                 |
| Distance type                |               Usually Euclidean (squared) | Any dissimilarity (flexible)               |
| Robustness to outliers       |                                      Poor | Good                                       |
| Works with categorical/mixed |                                        No | Yes (with appropriate dissimilarity)       |
| Scalability                  |                          Excellent (fast) | Slower (PAM), but CLARA/CLARANS improve it |
| Interpretability of center   |                                     Lower | Higher                                     |
| Typical algorithms           |                        Lloyd’s, k-means++ | PAM, CLARA, CLARANS                        |
| Best for                     |        Large datasets, spherical clusters | Noisy data, arbitrary distance, prototypes |

