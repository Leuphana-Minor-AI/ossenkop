import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ==========================================
# 1. DATA CREATION (The "Input")
# ==========================================
# make_blobs creates groups of data points. 
# centers=4 means we are pre-programming 4 "natural" groups into the data.
X, _ = make_blobs(n_samples=500, n_features=3, centers=4, cluster_std=1.0, random_state=42)
df = pd.DataFrame(X, columns=['Income_Level', 'Spending_Score', 'Account_Age'])

# ==========================================
# 2. PREPROCESSING (The "Cleaning")
# ==========================================
# K-Means calculates distance. Standardizing makes sure a feature with 
# large numbers (like Income) doesn't drown out small numbers (like Age).
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# ==========================================
# 3. ELBOW METHOD (The "Planning")
# ==========================================
# We calculate 'Inertia' (how far points are from their center) for 1-10 clusters.
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Save the Elbow Plot to your VS Code folder
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), inertia, 'go-')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.grid(True)
plt.savefig('elbow_plot.png') # <--- SAVES FILE TO VS CODE
plt.show()

# ==========================================
# 4. TRAINING (The "Learning")
# ==========================================
# We saw the "elbow" was at 4, so we tell the model to find 4 groups.
optimal_k = 4
model = KMeans(n_clusters=optimal_k, n_init=10, random_state=42)

# fit_predict does two things: 
# 1. Finds the centers. 2. Labels every row in our data with a Cluster ID.
df['Cluster'] = model.fit_predict(scaled_features)

# ==========================================
# 5. OUTPUT & ANALYSIS (The "Results")
# ==========================================
# Look at the average values for each group to understand who they are.
cluster_analysis = df.groupby('Cluster').mean()
print("\n--- Cluster Mean Values ---")
print(cluster_analysis)

# Save the model 'brain' so you can use it tomorrow without retraining.
joblib.dump(model, 'clustering_model.pkl')
joblib.dump(scaler, 'feature_scaler.pkl')
print("\nFiles saved: 'clustering_model.pkl' and 'feature_scaler.pkl'")

# ==========================================
# 6. VISUALIZATION (The "Proof")
# ==========================================

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Income_Level', y='Spending_Score', hue='Cluster', palette='viridis')
plt.title(f'Final Customer Segments (k={optimal_k})')

# Save the Final Clusters Plot to your VS Code folder
plt.savefig('final_clusters.png') # <--- SAVES FILE TO VS CODE
plt.show()