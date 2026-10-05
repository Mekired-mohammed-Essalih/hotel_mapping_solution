from sklearn.cluster import DBSCAN
import numpy as np

def dbscan_cluster(latitudes,longitudes,epsilon,min_samples,**kwargs):

    # convert epsilon (the distance) from km to radians
    kms_per_radian = 6371.0088
    epsilon /= kms_per_radian

    # set up the algorithm
    dbscan = DBSCAN(
        eps = epsilon,
        min_samples = min_samples,
        algorithm = 'ball_tree',
        metric = 'haversine',
        **kwargs
    )

    # fit the algorithm
    dbscan.fit(
        np.radians(
            [x for x in zip(latitudes,longitudes)]
        )
    )

    # return the cluster labels
    return dbscan.labels_


def geo_cluster(hotel_df):
  lat = hotel_df['lat']
  long = hotel_df['long']
  #distance of 1km
  labels = dbscan_cluster(lat, long , 0.047235577913699349 ,1)
  return labels