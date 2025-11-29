## 1. Introduction to Data Mining
- What is Data Mining?
- Data mining = process of discovering useful patterns, knowledge, and relationships from large amounts of data.
- It is a core step of KDD (Knowledge Discovery in Databases).
- Focus: automatic/semi-automatic analysis using algorithms (classification, clustering, association rules, etc.).
- Data Mining vs. KDD
- KDD = complete process from raw data → useful knowledge.
- Data mining = one step in KDD where actual algorithms are applied to extract patterns.

## 2. KDD Process and Data Mining
KDD (Knowledge Discovery in Databases) Definition
- A multi-step, iterative process of extracting valid, novel, potentially useful, and ultimately understandable patterns from data.
- KDD Steps (standard sequence)
1. Data Cleaning
- Remove noise, duplicate records, handle missing values.
- Example: replacing missing age with mean age.
2. Data Integration
- Combine data from multiple sources (databases, files, web).
- Example: merging sales DB and customer DB.
3. Data Selection
- Choose the part of data important for analysis (specific tables/attributes).
4. Data Transformation
- Convert data into suitable format:
- Normalization, aggregation, feature construction.
- Example: converting “date” into “month”, log-scaling skewed data.
5. Data Mining ✅
- Apply algorithms to extract patterns:
- Association rules, classification models, clustering, etc.
6. Pattern Evaluation
- Find interesting patterns using measures like support, confidence, lift, accuracy, etc.
- Remove trivial/irrelevant ones.
7. Knowledge Presentation
- Visualize and represent patterns:
- Tables, charts, rules, decision trees, reports.

> Data mining itself is mainly step 5 but depends strongly on previous steps.


## 3. Types of Data for Data Mining
1. Relational Data
- Stored in tables (rows = records, columns = attributes).
- Example: RDBMS like MySQL, Oracle.
2. Transactional Data
- Sequence of transactions; each transaction is a set of items.
- Example: market basket data, web click-streams.

3. Time-Series and Sequence Data
- Values recorded over time.
- Example: stock prices, sensor data, ECG.
4. Spatial Data
- Data with spatial location (coordinates, regions).
- Example: GIS data, maps.
5. Text Data
- Unstructured or semi-structured text.
- Example: documents, emails, web pages.
6. Multimedia Data
- Images, audio, video.
7. Web Data
- Web content, web structure (links), web usage (logs).
8. Data Streams
- Continuous fast data (IoT devices, network traffic).

## 4. Data Mining Functionalities
- These are what data mining can do (types of knowledge it can discover).
1. 4.1 Data Characterization
- Produces summarized description of a target class.
- Example: summarize characteristics of “loyal customers”:
    - avg age, income range, typical region.
- Techniques: simple aggregation, OLAP, descriptive statistics.

2. 4.2 Data Discrimination
- Compares target class vs. contrasting class.
- Example: “loyal customers” vs. “non-loyal customers”.
- Output: discriminant rules like
    - Loyal customers: age 25–40, income > 40k
    - Non-loyal: age < 25, income < 25k.

3. Mining Frequent Patterns
- Find patterns that occur frequently in data:
- frequent itemsets, subsequences, substructures.
- Basis for association rule mining, sequential pattern mining.

4. Association
- Discover association rules of the form X → Y.
- Example: {bread, butter} → {milk}.
- Measures: support, confidence, lift.

5. Correlation
- Find correlated attributes/items (positive or negative).
- Goes beyond support–confidence, using statistical correlation measures.

6. Classification
- Learn a model that maps data items to predefined class labels.
- Supervised learning.
- Example: classify emails as spam / not spam.

7. Prediction
- Predict continuous numeric values or future trends.
- Example: predict tomorrow’s temperature, stock price.
- Techniques: regression, time-series analysis.

8. Cluster Analysis
- Group data into clusters such that objects in same cluster are similar.
- Unsupervised learning.
- Example: customer segmentation.

9. Outlier Analysis
- Detect data objects that are very different from others.
- Possible causes: fraud, errors, rare events.
- Example: unusual credit card transaction.

10. Evolution Analysis
- Study changes and trends over time.
- Example:
- customer behavior changes across years,
- seasonal trends in sales.
- Includes time-series mining, sequence mining, trend and deviation analysis.

## Classification of Data Mining Systems
- Systems can be classified in several ways:
- According to Type of Data Source
    - Relational DB, data warehouse, transactional DB, spatial/temporal, text, multimedia, web, data streams.
- According to Data Model
    - Relational, object-oriented, object-relational, hierarchical, network, etc.
- According to Kind of Knowledge Discovered
    - Characterization/discrimination systems
    - Association rule mining systems
    - Classification/prediction systems
    - Clustering systems
    - Outlier detection systems, etc.
- According to Mining Techniques Used
    - Machine learning based (neural nets, SVM)
    - Statistical methods
    - Pattern recognition
    - Database-oriented (OLAP, SQL-based)
    - Visualization-based.
- According to Degree of User Interaction
    - Autonomous (fully automatic)
    - Interactive exploratory tools.

