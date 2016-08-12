import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from scipy.cluster.vq import kmeans2

# Define a Function to make clusters in the data based on the feature vector and the no. of clusters required.
def clustering (data,num_clusters):
    x, y = kmeans2(data, num_clusters , iter = 20)
    return (x,y)

# Define a function to make a plot of the crime location and the centeroids based on clusters.   
def plot_clusters(data,centeroids,clusters):
    plt.scatter(data['Latitude'], data['Longitude'], c=clusters, alpha=0.33333)
    plt.scatter( centeroids[:,0],centeroids[:,1],c='red',marker= 'x',alpha=1 )
    plt.show()
    
# Read the CSV file into a DataFrame
crime = pd.read_csv('Police_Incidents_2015.csv')

# Create a dataframe with only the required features for clustering
crime_location = DataFrame()
crime_location['Latitude'] = crime['Lat']
crime_location['Longitude'] = crime['Long']

# Specify the no. of clusters required
num_clusters = 13

# Function call to create clusters using Kmeans2
centeroid,cluster =clustering(crime_location,num_clusters)

# Function to plot the Co-Ordinates on the map as per clusters.
plot_clusters(crime_location,centeroid,cluster)

