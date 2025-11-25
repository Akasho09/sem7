## 📌 What is Data Preprocessing?

Data preprocessing is a crucial step in the Knowledge Discovery process. It involves preparing and cleaning raw data before applying data mining techniques. The goal is to improve data quality, remove inconsistencies, and transform data into a suitable format for analysis.
(CS IT)


## DATA 
- Collection of data objects and their attributes 
- atribute is the property of data and collection of atributes descrbe a object

### Types of atributes : 
1. Nominal atributes :
    - cant be compared eg serial no , account no , name , zip code .

2. Ordinal : 
    - ranikng , height , taste , marks etc.

3. Interval 
4. Ratio


### Discrete vs Continous Attributes :
- Continous : Attributes that can take any value within a given range.
eg : Temperature , weight etc 

- Discrete : Attributes that take specific, separate values.
eg: Color , Pincode 

### 🔑 2. Descriptive Data Summarization
1. Measuring Central Tendency
- Mean: The average value of the dataset.
- Median: The middle value when data is sorted.
- Mode: The most frequently occurring value.

2. Measuring Dispersion
- Range: Difference between the highest and lowest values.
- Variance: Measures how data points vary from the mean.
- Standard Deviation: Square root of variance; shows the spread of data.

### 🔑 3. Visualization of Descriptive Data Summaries
Helps to understand patterns and distributions in data.

- Common techniques:
    - Histograms – frequency distribution.
    - Box plots – identify outliers and spread.
    - Scatter plots – relationships between two variables.
    - Bar charts – compare categories.


### types of data sets :
1. Record Data :
    - Data Matrix 
    - Data Transaction 
    - Document Data

2. Graph :
    - WWW
    - Molecular Data 

3. Ordered
    - Spatial Data 
    - Temporal 
    - Sequential
    - Genetic Seq data


### Data Quality : 
1. Noise 
2. Outliers 
3. Missing values 
4. Duplicate v


### 🔑 4. Data Cleaning
- Handling Missing Values
    - Ignore missing values – if few are present.
    - Fill with global constant – such as 0 or “unknown.”
    - Fill with mean or median – for numerical data.
    - Predict missing values – using regression or classification.
- Filtering Noisy Data – Binning Method
    - Sort data and group it into equal-sized bins.
    - Replace values within each bin by the bin’s mean or boundary values.
    - Reduces noise while preserving data trends.


### 🔑 5. Data Integration
- Combines data from multiple sources.
- Resolves data redundancy and inconsistency.
- Ensures that data across different datasets is aligned and merged correctly.


### 🔑 6. Data Transformation
1. Smoothing
- Reduces noise and irregularities in data.
- Techniques include binning, regression, and clustering.

2. Aggregation
- Combines data to produce summary information.
- combinig 2 or more attributes into single .
- Example: Summarizing sales data by region or month.

- Purpose :
    - Data Reduction
    - Change of scale : eg regions , cities , states to country .
    - More stable data


3. Generalization
- Replaces detailed data with higher-level concepts.
- Example: Converting age into categories like “20–30,” “31–40.”

4. Normalization
- Rescales data to a standard range.
- Methods:
- Min-max normalization – scales data between 0 and 1.
- Z-score normalization – standardizes based on mean and standard deviation.

5. Feature Selection
- Identifies relevant features (attributes) and removes irrelevant or redundant ones.
- Improves model accuracy and reduces computational complexity.


### 🔑 7. Data Reduction
Reduces the volume of data while maintaining its integrity.

- Techniques:
    - Dimensionality reduction – removing less important attributes.
    - Data compression – encoding data efficiently.
    - `Sampling` – selecting a representative subset.
    - 📊 Types of Sampling Methods
     -  1️⃣ Random Sampling
        - Every record has an equal chance of being selected.
        - Helps reduce bias in sample selection.
        - Example: Picking 100 students randomly from a college.

     -  2️⃣ Stratified Sampling
        - Population is divided into subgroups (strata) based on certain characteristics, and samples are taken from each group proportionally.
        - Ensures representation from all subgroups.
        - Example: Dividing students by department and sampling equally from each.

     -  3️⃣ Systematic Sampling
        - Selects every k-th record after a random start point.
        - Simple and efficient.
        - Example: Select every 10th product in a production line.

     -  4️⃣ Cluster Sampling
        - Population is divided into clusters, and a few clusters are chosen randomly.
        - Used when data is geographically spread out.
        - Example: Selecting certain cities and using all students from those cities.

     -  5️⃣ Convenience Sampling
        - Samples are chosen based on ease of access.
        - May introduce bias but is useful for quick insights.
        - Example: Surveying people in a nearby shopping mall.


### 🔑 8. Data Discretization and Concept Hierarchy Generation
- Data Discretization
    - Converts continuous data into discrete intervals.
    - Helps simplify analysis and modeling.

- Concept Hierarchy Generation
    - Organizes data attributes into hierarchical levels.
    - Example: “City → State → Country.”
    - Supports classification and aggregation tasks.



