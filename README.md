# Smart Customer Segmentation: Optimizing Marketing Campaign using K-Means Clustering
Tech Stack: Python (Pandas, Scikit-Learn, Matplotlib), Google Looker Studio.

# Problem Statement: 
"The Mall Marketing Team* struggled to target promotions appropriately due to mixed customer data. A "one-size-fits-all" strategy proved cost-effective. This project aimed to segment customers based on spending behavior and income for more targeted promotions."

# Methodology
1. Data Cleaning
   I standardized column names and ensured there were no missing values. I chose Annual Income and Spending Score as the primary segmentation variables.

2. Determining Number of Cluster


   Although the Elbow graph shows a slowing inertia decline at k=4, I decided to use k=5. This decision was made based on business domain knowledge to separate the relatively large 'Average' segment from the 'Sensible' or 'Careless' segments.
