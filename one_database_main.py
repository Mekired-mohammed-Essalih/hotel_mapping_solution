import  pandas as pd 
import sys
from preprocessing import preprocessing
from geo_clustering import geo_cluster
from geo_cluster_cleaning import geo_cluster_cleaning_one_database
from indexing import indexing1 , indexing_one_database
from comparison import comparison
from organization import organize_data
from print_result import print_hotel_data
from classification import normal_classification


def one_database_main (dfList):
   #applied preprocessing on each one (return all database preprocessing and merged in one database hotel_df)
   hotel_df = preprocessing(dfList)
   #we applied geo clustering and return labels
   labels = geo_cluster(hotel_df)
   #add new column for each hotel with his label
   hotel_df["labels"] = labels
   #get labels with hotel that belong to more then database
   same_db_index_df = geo_cluster_cleaning_one_database (hotel_df)
   # we create paires of hotels
   result = indexing_one_database(same_db_index_df,hotel_df)
   #we convert them to multiindex so we can use them in comparison
   candidate_links = pd.MultiIndex.from_tuples(result)
   #we compare between paires
   features = comparison(hotel_df , candidate_links)
   #classification step 
   final = normal_classification(features , 2)
   #organize the results
   final_result = organize_data(final)
   df = pd.DataFrame (final_result, columns = ['id0', 'id1'])

   # Set the encoding to UTF-8 so we can read arabic
   if sys.stdout.encoding != 'utf-8':
       sys.stdout.reconfigure(encoding='utf-8')
   #read data line 0 to 50
   for i in range(0,50):
      hotels = print_hotel_data(i , df , hotel_df)
      print("ligne number " + str(i) )
      print(hotels[['name']].to_string(index=False))
      print(hotels[['address']].to_string(index=False))
      print("\n----------")
  