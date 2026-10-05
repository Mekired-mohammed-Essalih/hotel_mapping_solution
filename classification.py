import recordlinkage
import numpy as np


def normal_classification(features , i ):
    matches = features[features.sum(axis=1) >= i] 
    mi= matches.index
    final = mi.to_frame()
    final = final.reset_index(drop=True)
    return final 

def threshold_Based_classification(features):
    scores = np.average(features.values , axis=1 , weights = [30 , 20 , 30 , 20] )
    scored_comparison = features.assign(score = scores)
    theshold_based_matches = features[scored_comparison['score'] >= 0.85]
    return theshold_based_matches

def kmeans_classifier(features):
    kmeans = recordlinkage.KMeansClassifier()
    result_kmeans = kmeans.fit_predict(features)
    result_kmeans = result_kmeans.to_frame()
    result_kmeans = result_kmeans.reset_index(drop=True)
    return result_kmeans

def ECM_classifier(features):
    ecm = recordlinkage.ECMClassifier(binarize=0.8)
    result_ecm = ecm.fit_predict(features)
    result_ecm = result_ecm.to_frame()
    result_ecm = result_ecm.reset_index(drop=True)
    return result_ecm