# Weakly Supervised Severity Estimation of Apple Scab Using CNN and Grad-CAM (Gradient-weighted Class Activation Mapping)

- Severity -> `suh·veh·ruh·tee`
- Scab -> `skab`
- orchards -> `aw·chuhdz`
- lesions -> `lee·zhnz`
- defoliation -> `duh·foh·lee·ay·shn`
- Venturia inaequalis -> `ven-TOO-ree-uh in-ay-KWA-lis`
- agronomists -> `uh·graw·nuh·muhsts`


### importance
- Apples are a great global importance 
    • Among the top four most cultivated fruits worldwide (>80M tons annually).

- and in India 
    • Though only Himachal Pradesh & Jammu & Kashmir are major producers.
    • Still it Contributes substantially to horticulture sector and in turn horticulture contributes ≈30% to Indian agriculture GDP . 
    However, despite a 20% increase in the area of apple cultivation, production has risen by only 1–2%. The main reason is frequent disease outbreaks.

### Apple Scab: A Major Threat
    Among these diseases, the most destructive is Apple Scab, caused by the Venturia inaequalis fungus. 
    It appears as olive-green to dark lesions on leaves and fruits, leading to defoliation, reduced photosynthesis, degraded fruit quality, and yield losses.

### Here is the Problem statement
    Apple Scab is global problem , caused by Venturia inaequalis, is a serious threat to apple production. It reduces photosynthesis, lowers fruit quality, and ultimately causes large economic losses worldwide, including in India.

#### Traditional methods to detect severity have limitations:

    - Manual inspection is slow, subjective, and labor-intensive.
    - Laboratory methods like PCR or serological tests are accurate but expensive, time-consuming, and not feasible for large-scale farm use.

#### With the progress of deep learning, CNNs 
    - can now classify apple leaves with over 95% accuracy – but these models mostly tell whether a leaf is healthy or diseased, not how severe the infection is.

- The challenge/Research gap is that most severity estimation methods require pixel-level lesion masks, which need expert annotation, are costly, and don’t scale well for large datasets.

- So, there is a critical need for a method that is:
    - Weakly supervised (works with only image-level labels),
    - Scalable and cost-effective,
    - And provides fast severity estimation to support better crop management.

--------------------------------------------------------------------------------------------------------------------------------------------

## From “What” to “How Much”

### What We Know
   - Currently, CNNs are extremely powerful in classifying plant diseases. In fact, they achieve more than 98% accuracy. This means we can confidently answer the question: ‘What disease is present?’
    - But in real-world crop management, knowing what disease is present is not enough. Farmers and agronomists need to know ‘How much’ of the plant is affected – in other words, the severity percentage of the infection.”

### The Problem
- To estimate severity, the traditional approach has been fully supervised segmentation.
    That means creating pixel-level masks of lesions for every training image.
- But this process is very expensive, time-consuming, and requires domain experts.
So, it is not practical for building large-scale severity estimation systems.


### So whats The Opportunity
- With weakly supervised methods like Grad-CAM, we can localize diseased regions using only image-level labels – no need for detailed pixel annotations.
- In fact, prior research – like Shukla et al., 2020 – has already shown that this approach is feasible.
But their work stopped at visual localization. In other words, they generated heatmaps, but did not convert them into severity estimates.

### The Gap & Our Contribution

Currently, there is no validated method to convert Grad-CAM heatmaps into quantitative severity scores.

- And this is where our contribution comes in.
    - We propose a method to transform Grad-CAM heatmaps into pseudo-masks.
    - From these masks, we derive severity scores that represent the percentage of area infected.
    - This gives us actionable insights for farmers and crop managers.
    - Most importantly, our framework is low-cost, scalable, and deployable – making severity estimation feasible at field scale.


## Data Sets :
- For this study, we used data from the PlantVillage dataset, specifically focusing on the Apple category.

- We created two versions of the dataset:
    - Dataset 1 – Original: Raw leaf images with natural backgrounds.
    - Dataset 2 – Background Removed: Pre-processed images where the leaf was segmented, removing background noise for cleaner feature extraction.”

### Dataset Statistics (Train/Test Split)












--------------------------------------------------------------------------------------------------------------------------------------------
- Severity Estimation of Apple Scab using Convolutional Neural Networks and Gradient-weighted Class Activation Mapping.
- 
    - CNN → Feature extraction & classification for images.
    - Grad-CAM → Visualization tool showing why CNN predicted something (regions of focus).
- Example:
    - Input: Image of a cat 🐱.
    - CNN predicts: "cat" with 92% confidence.
    - Grad-CAM highlights the face region of the cat → shows that’s what influenced the decision.

- Apple Scab is one of the most harmful fungal diseases in apple orchards.
Traditionally, severity estimation requires expert knowledge and is time-consuming.


