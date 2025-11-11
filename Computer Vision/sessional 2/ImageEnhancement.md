## Image Enhancement 

is the process of improving the visual appearance of an image or making it more suitable for analysis by a computer vision algorithm.

- In short — it’s about making an image clearer, cleaner, and more informative, either for human viewing or machine processing.

### Types :

![alt text](image.png)

1. Point Transformations:
    1. Inversion Trans:

    ![alt text](image-1.png)

- Digital negative :

    ![alt text](image-7.png)

2. Thresholding with T=4

    ![alt text](image-8.png)

3. Clipping with r1=2 , r2 = 5.

    ![alt text](image-9.png)

4. Contrast Stretching :

    ![alt text](image-10.png)

    ![alt text](image-11.png)

5. Intensity Level Slicing :
    1. without bg (~ cliping)

        ![alt text](image-12.png)

2. with bg

        ![alt text](image-13.png)

6. Log transfromations :

    ![alt text](image-14.png)

- 2 cases

  1. c=1

    ![alt text](image-15.png)

  2. c=L/(log(1+L)) =~ 61

    ![alt text](image-16.png)

7. Power law trans :

    ![alt text](image-17.png)

8. Bit planes :

    ![alt text](image-41.png)

## Histogram Equalizations :

1. question :

![alt text](image-18.png)

- input image 

![alt text](image-19.png)

- histo table :

![alt text](image-20.png)

- o/p image 

![alt text](image-21.png)

2. Modify histo 1 as given by 2:

![alt text](image-22.png)

- make histograms of both and map 

![alt text](image-23.png)

## Fundamentals of Spatial Filtering

### Convolution :

![alt text](image-24.png)

![alt text](image-25.png)

![alt text](image-26.png)

### Correlation :

- no roation of mask.

![alt text](image-27.png)

![alt text](image-28.png)

### Question :

![alt text](image-29.png)

- answer

#### Convolution :

- keep shitfing mask after roation from 0,0 -> n-2,n-2

![alt text](image-30.png)

![alt text](image-31.png)

### Correlation :

- same steps but no rotation 

## Smoothing Spatial Filters

![alt text](image-32.png)

1. Linear filters:

![alt text](image-33.png)

![alt text](image-34.png)

2. Non-Linear Filter:

## Question :

1. Box/Mean filter 

![alt text](image-35.png)

2. Weighted Avg filter :

![alt text](image-36.png)

3. Median , Min , Max

![alt text](image-37.png)

## Questions

![alt text](image-38.png)

![alt text](image-39.png)

- wrapping the image 
- => top row to bottom and vicer versa . 
- first element to last and so on .

![alt text](image-40.png)

<!-- 
2. No Linear :
    1. Square
    2. Square Root 
    ![alt text](image-2.png)
    g(x,y)= root(255. f(x,y))
    3. Lograthimaic :
    ![alt text](image-3.png)
    4. Exponential:
    ![alt text](image-4.png)
    5. pOWER Fn :
    ![alt text](image-5.png)
    6. Gamma Correction :
    ![alt text](image-6.png) -->

### 🎯 2. Goals of Image Enhancement

1. Improve contrast and brightness
2. Reduce noise and blurring
3. Highlight important features or edges
4. Restore details lost during capture

5, Prepare images for further processing (segmentation, recognition, etc.)

## ⚙️ 3. Types of Image Enhancement Techniques

| Type                            | Description                                                     |
| ------------------------------- | --------------------------------------------------------------- |
| **Spatial Domain Techniques**   | Directly operate on pixel values                                |
| **Frequency Domain Techniques** | Operate on the image’s Fourier transform (frequency components) |

### 🧩 A. Spatial Domain Techniques

1. 1️⃣ Gray Level Transformations

- Used to modify brightness or contrast.

| Method                               | Description                                                      |
| ------------------------------------ | ---------------------------------------------------------------- |
| **Linear Contrast Stretching**       | Expands the range of pixel intensities to improve contrast.      |
| **Log Transformation**               | Enhances dark regions; compresses bright areas.                  |
| **Power-Law (Gamma) Transformation** | Adjusts brightness based on γ value: ( s = c \cdot r^{\gamma} ). |
| **Negative Transformation**          | Inverts pixel values — useful in X-rays, etc.                    |

2. 2️⃣ Histogram-Based Techniques

- Use image histograms for enhancement.

| Method                               | Description                                                      |
| ------------------------------------ | ---------------------------------------------------------------- |
| **Linear Contrast Stretching**       | Expands the range of pixel intensities to improve contrast.      |
| **Log Transformation**               | Enhances dark regions; compresses bright areas.                  |
| **Power-Law (Gamma) Transformation** | Adjusts brightness based on γ value: ( s = c \cdot r^{\gamma} ). |
| **Negative Transformation**          | Inverts pixel values — useful in X-rays, etc.                    |

3. 3️⃣ Smoothing (Noise Reduction)

- Removes noise using filters.

| Filter              | Type       | Description                                                                            |
| ------------------- | ---------- | -------------------------------------------------------------------------------------- |
| **Mean Filter**     | Linear     | Replaces each pixel with average of neighbors.                                         |
| **Gaussian Filter** | Linear     | Weighted averaging for smooth blur.                                                    |
| **Median Filter**   | Non-linear | Replaces each pixel with median value of neighborhood (removes salt-and-pepper noise). |

4. 4️⃣ Sharpening (Edge Enhancement)

- Highlights edges and fine details.

| Filter                        | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| **Laplacian Filter**          | Second derivative — detects edges.                        |
| **Sobel / Prewitt / Roberts** | Gradient-based edge detection.                            |
| **Unsharp Masking**           | Adds high-frequency details to original image to sharpen. |

### 🧮 B. Frequency Domain Techniques

- These methods work on frequency components of an image after performing Fourier Transform (FFT).

| Method                  | Description                                       |
| ----------------------- | ------------------------------------------------- |
| **Low-Pass Filtering**  | Removes high-frequency noise → smooths the image. |
| **High-Pass Filtering** | Enhances edges and details.                       |
| **Band-Pass Filtering** | Keeps only certain frequency ranges.              |