## Filter Example using Zero Padding and Pixel Replication Neighbourhood avereging:
- avereging => 1/9*sum of all elements .

## Q4) “Quality of picture depends on number of pixels and number of gray levels.” — Justify.
- Spatial resolution (pixels): More pixels → finer sampling → sharper details and fewer jaggies. Too few pixels cause aliasing and loss of detail.

Intensity resolution (gray levels): More quantization levels → smoother tonal transitions and less banding/posterization. Too few levels yield visible steps/noise.

Hence image quality depends jointly on sampling density and quantization precision.


## Q5) Can two different images have the same histogram?
Yes. The histogram ignores spatial arrangement of pixels and only counts how many of each intensity occur.
- Different images with the same set of pixel values arranged differently (e.g., shuffled pixels, or many results of histogram equalization) can share identical histograms while looking visually very different.


