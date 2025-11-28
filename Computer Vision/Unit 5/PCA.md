## 📘 PRINCIPAL COMPONENT ANALYSIS (PCA)
- PCA is a statistical technique used to reduce the dimensionality of data while retaining as much variation (information) as possible.
- It transforms the original variables into a new set of orthogonal (uncorrelated) variables called Principal Components (PCs).
- PCA is a linear transformation technique that converts high-dimensional data into a lower-dimensional space by finding directions (principal components) that capture maximum variance in the data.

- It reduces redundant or correlated features.
- It simplifies the dataset while keeping important patterns.
- It is widely used in machine learning and computer vision.

### Why PCA is Used? (Purpose)
- Dimensionality reduction (reduce number of features)
- Noise removal
- Visualization of high-dimensional data (e.g., reducing 100D → 2D)
- Avoid overfitting
- Speed up ML algorithms (less computation)
- Remove multicollinearity in features

### Steps of PCA (Important for exams)
1. Step 1: Standardize the Data
- Convert all features to the same scale using z-score normalization.

2. Step 2: Compute Covariance Matrix
- Matrix that shows how variables are related.
- [ X1       X1.X2
    X2.X1    X2   ]

3. Step 3: Compute Eigenvalues & Eigenvectors
> S = S-lamda.I = 0 .
- Perform eigen decomposition of the covariance matrix.

4. Step 4: Sort Eigenvalues
> S.  [u1   = [0
      u2]      0]
- Sort from highest to lowest variance.

5. Step 5: Select Top k Components
- Choose the top k eigenvectors (according to eigenvalues).

6. Step 6: Project Data onto New Space
- Transform original data into k-dimensional space.
> zi =u'.yi
- yi is elemests minused mean .
