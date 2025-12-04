## Filter Example using Zero Padding and Pixel Replication Neighbourhood avereging:

- avereging => 1/9*sum of all elements .

## Q4) “Quality of picture depends on number of pixels and number of gray levels.” — Justify.

- Spatial resolution (pixels): More pixels → finer sampling → sharper details and fewer jaggies. Too few pixels cause aliasing and loss of detail.

Intensity resolution (gray levels): More quantization levels → smoother tonal transitions and less banding/posterization. Too few levels yield visible steps/noise.

Hence image quality depends jointly on sampling density and quantization precision.

## Q5) Can two different images have the same histogram?

Yes. The histogram ignores spatial arrangement of pixels and only counts how many of each intensity occur.

- Different images with the same set of pixel values arranged differently (e.g., shuffled pixels, or many results of histogram equalization) can share identical histograms while looking visually very different.

## 

| (r_k) | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (n_k) | 11  | 27  | 43  | 33  | 21  | 24  | 56  | 78  | 99  | 67  | 52  | 36  | 22  | 9   | 0   | 4   | 7   | 3   | 5   | 3   |

---

1. Compute the mean gray level

Formula: μ=1/N *  (1->k)∑​rk*​nk

=> μ=4360​ / 600  = 7.27​

2. Compute the standard deviation

- Variance:
    - σ2 = 1/N * (1->k) ∑​(rk​−μ)^2 * nk​

3. Standard deviation:

- σ= root (13.10) ≈3.62

## Quantization and sampling

![alt text](image-44.png)

## Discuss Gamma correction used for contrast enhancement of under exposed and over exposed image. Show it by drawing suitable Gamma-correction curve.
---
- Gamma correction is a nonlinear intensity transformation used to improve the visibility of under-exposed (dark) and over-exposed (bright) images.
The transformation function is: s=cr^γ.
- Where:
    - r = input intensity (normalized 0–1)
    - s = output intensity
    - c = constant (usually 1)
    - γ = gamma value

1. Gamma < 1 → Brightens Under-Exposed Images
- When γ < 1, the curve is concave upward, expanding darker pixel values.
- Effects:
    - Dark areas become brighter
    - Good for under-exposed images
    - Increases visibility of shadow details
- Common values: 0.4, 0.6, 0.8.

2. Gamma > 1 → Darkens Over-Exposed Images
- When γ > 1, the curve is convex, compressing bright pixel values.
- Effects:
    - Bright areas become darker
    - Good for over-exposed images
    - Recovers highlights and improves contrast
- Common values: 1.5, 2.0, 2.5.

![alt text](image-46.png)


## Analyse 3X3 mean filter in the frequency domain and prove that it behave like a low pass filter.
- preserves low spatial frequencies (slow intensity variations),
- suppresses high spatial frequencies (rapid changes, edges, noise).
- A low-pass filter is a filter that allows low-frequency components to pass through while reducing or blocking high-frequency components.
