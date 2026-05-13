# My first repository
Micromodule 1: Meta-Data |
Generated a simple ESG Data Set using AI to learn how to create Metadata and how those can be relevant to add context when training a model. Dataset includes Hourly environmental performance data including energy consumption, Scope 1 emissions, water usage, and waste generation for CSRD reporting compliance.

Micromodule 2: Webscraping |
Scraped structured data from a publicly available web page designed for webscraping training purposes called "Books to Scrape". Built a scraping tool using python libraries request, beautifulsoup, csv and time and collected data of the demo book store including name of the book, price (with change from GBP to EUR) and rating (1-5).
URL: https://books.toscrape.com/
In the first run only the first 5 pages were scraped. The updated scraping tool collects data from every page (1000 books in total) that can be found in books.csv.
Range of pages to be scraped can be changed in line 28.
Data collected for testing purposes only. The prices and ratings of the books were randomly assigned and have no real meaning.

Micromodule 3: Auto-feature Generation |
Used a kaggle dataset with information about trips taken by yellow cabs in New York from January 2023 to June 2023.
This includes fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts.
https://www.kaggle.com/datasets/nagasai524/nyc-taxi-trip-records-from-jan-2023-to-jun-2023
The dataset was transformed into an hourly aggregated time series. At first I did not sample the data causing the TSFRESH to freeze and crashing my computer. In the fixed version it uses only n=50.000 observations. TSFRESH was used to extract 4,698 statistical and time-based features such as trends and autocorrelations saved in tsfresh_features.csv. Pylance thinks it is missing an import but if it works don't touch it.
There are a lot of features, that were created that are totally irrelevant for me, but it still definitely saved me some time.
If done manually, I would likely have created only basic features such as averages. However, the quality of the features is mixed: some are really good but others need to be checked before used in modeling.

Micromodule 4: Train a Clustering Model
Created a model to group unlabeled data into meaningful clusters. Using the K-Means algorithm on a synthetically generated dataset, identified patterns in customer behavior based on three features: Income Level, Spending Score, and Account Age. The function used to create the dataset is called make_blobs (a standard tool for testing and demonstrating clustering algorithms).
Used StandardScaler to normalize data, ensuring features with larger numerical ranges do not bias the distance calculations.
Number of k`s: Implemented the Elbow Method to determine that 4 clusters provide the best balance.
Saved both the trained model and the scaler as .pkl files to allow for the categorization of new data without retraining.
The model successfully divided the data into 4 distinct segments. While the specific means may shift with new data, the general profiles identified are:
Cluster 1: These are our best customers. They earn a lot and spend a lot. They have been with our company for a long time (high Account Age).
Cluster 2: These people have the money but aren't spending it with our company.
Cluster 0: Low income but high spending.
Relevant Files:
clustering_model.pkl: The trained model containing cluster centroids.
feature_scaler.pkl: scale and normalize new data.
elbow_plot.png: Visualization confirming the choice of 4 clusters.
final_clusters.png: scatter plot visualizing the clear separation of customer groups.
