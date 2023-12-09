# Hybrid MBTI-Based Job Recommender

## Description

Our application, the **Hybrid MBTI-Based Job Recommender**, combines content-based and collaborative filtering techniques to provide accurate job recommendations based on users' MBTI (Myers-Briggs Type Indicator) profiles. The system uses both individual personality traits and collective user preferences to enhance the precision and relevance of job suggestions.

### Key Features:

1. **Content-Based Recommender:**
   - Recommends jobs based on individual MBTI profiles, focusing on the ISFJ and ENTP personality types.
   - Analyzes percentage scales of ISFJ and ENTP attributes for personalized job recommendations.

2. **Collaborative Recommender:**
   - Predicts job fields based on shared preferences from multiple MBTI profiles.
   - Expands recommendations by considering the collective choices of users with similar personality types.

3. **Hybrid Recommender System:**
   - Overcomes challenges like the cold start and sparsity problems.
   - Delivers well-rounded and personalized job suggestions by merging content-based and collaborative approaches.

4. **Fuzzy Algorithm for Normalization:**
   - Utilizes a fuzzy algorithm to normalize job counts, enhancing the precision of recommendations.
   - Considers nuanced relationships between job occurrences for more accurate representation of user preferences.

### Advantages:

- **Personalized Recommendations:** Tailored job suggestions based on individual MBTI profiles.
- **Diverse Insights:** Benefit from a wide range of job recommendations derived from collaborative data.
- **Enhanced Accuracy:** The hybrid approach minimizes the limitations of individual recommender systems.
- **Overcoming Challenges:** Addresses common problems like the cold start and sparsity issues.

## Content-Based Filtering with Fuzzy Logic

### Overview

This implementation focuses on building a content-based recommendation system using a scale-based algorithm augmented with fuzzy logic. The approach involves leveraging personality scales, measuring various dimensions such as extraversion vs. introversion, sensing vs. intuition, thinking vs. feeling, and judging vs. perceiving. The goal is to provide job recommendations that align with personality traits, incorporating fuzzy logic for enhanced flexibility in handling imprecise preferences.

### Process Explanation

1. **Normalization of Scales with Fuzzy Logic:**
   - Normalizes each personality scale using Min-Max scaling with fuzzy logic for handling imprecision.

2. **Weight Calculation for Each Scale:**
   - Calculates weights for each scale based on the number of jobs in the same field, introducing fuzzy logic to accommodate uncertainties.

3. **Job Profile Formation with Fuzzy Logic:**
   - Forms job profiles by summing weighted scales, integrating fuzzy logic to capture the vagueness in psychological tendencies.

4. **Integration of MBTI and Job Profiles:**
   - Seamlessly integrates job profiles enriched with fuzzy logic-enhanced scales into the main dataframe.

5. **Unique Job Profile Creation with Fuzzy Logic:**
   - Generates unique job profiles based on personality types, incorporating fuzzy logic to handle imprecision.

## Collaborative Recommender

### Overview

Our Collaborative Recommender employs memory-based collaborative filtering, specifically the user-based approach, to provide personalized job recommendations based on MBTI profiles.

### Implementation Strategy

- **Memory-based:**
  - **User-based:** Computes similarities between users based on historical interactions with job fields.
  - **Cosine Similarity:** Measures the cosine of the angle between MBTI profiles for distance calculation.
  - **Brute-Force Algorithm:** Utilizes a brute-force algorithm for nearest neighbor search, ensuring comprehensive user analysis.

### Algorithm Feature

Focuses on user-based collaborative filtering, identifying users with comparable preferences and suggesting job fields aligned with their collective choices.

## Hybrid Recommender

Integrating both content-based and collaborative approaches, our hybrid recommender delivers highly personalized and diverse job recommendations. The system overcomes challenges and provides a comprehensive solution for individuals seeking tailored career guidance based on their unique personalities.

Feel free to explore, customize, and integrate this system into your projects for effective job recommendations tailored to MBTI profiles!

### Source Data:

The source data used for this project can be found at [Kaggle - MBTI Test](https://www.kaggle.com/datasets/pmenshih/kpmi-mbti-mod-test/discussion).
