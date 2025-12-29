# Smart Customer Segmentation: Optimizing Marketing Campaign using K-Means Clustering
Tech Stack: Python (Pandas, Scikit-Learn, Matplotlib), Google Looker Studio.

# Problem Statement: 
"The Mall Marketing Team* struggled to target promotions appropriately due to mixed customer data. A "one-size-fits-all" strategy proved cost-effective. This project aimed to segment customers based on spending behavior and income for more targeted promotions."

# Methodology
1. Data Cleaning
   I standardized column names and ensured there were no missing values. I chose Annual Income and Spending Score as the primary segmentation variables.

2. Determining Number of Cluster

--- posisi gambar elbow method

   Although the Elbow graph shows a slowing inertia decline at k=4, I decided to use k=5. This decision was made based on business domain knowledge to separate the relatively large 'Average' segment from the 'Sensible' or 'Careless' segments.

# Clustering Result
VIP (Target): High Income, High Spending. (Top Priority)
Miser: High Income, Low Spending. (Untapped Potential)
Careless: Low Income, High Spending. (Credit Risk)
Sensible: Low Income, Low Spending.
Standard: Average Income, Average Spending.

# Code Snippet
```python
def get_cluster_name(row):
    income = row['Annual_Income']
    spending = row['Spending_Score']

/// Ambil nilai rata-rata income dan spending score dari seluruh populasi sebagai patokan
    avg_income_population = df['Annual_Income'].mean()
    avg_spending_population = df['Spending_Score'].mean()

    /// Logika Penamaan (Rule Based)
    if income > avg_income_population and spending > avg_spending_population:
        return 'VIP (Target)'
    elif income > avg_income_population and spending < avg_spending_population:
        return 'Miser (Berduit tapi Hemat)'
    elif income < avg_income_population and spending > avg_spending_population:
        return 'Careless (Boros)'
    elif income < avg_income_population and spending < avg_spending_population:
        return 'Sensible (Hemat)'
    else:
        return 'Standard (Menengah)'
```
        
