import pandas as pd
from itertools import combinations


#the purpuse of this function is devide hoteldf to each database
def indexing1 (dfList , hotel_df):
#create a list with len of the number of databases then put hotels that belong too
  hotel_df_different_db_list  = [None] * len(dfList)
  for i in range(len(dfList)):
    hotel_df_different_db = hotel_df[hotel_df['db_index']==i]
    hotel_df_different_db_list[i] = hotel_df_different_db
  return hotel_df_different_db_list

def indexing_more_than_database(dfList , diff_db_index_df , hotel_df_different_db_list):
  result = []
  #more_one_db_index_group = la list labels
  #we loop on the labael list
  for i in diff_db_index_df:
    #list have 2 case if we have 2 database
    hotels_db_list  = [None] * len(hotel_df_different_db_list)

    j= 0
    #we loop in the each database to get hotels that belong to label i
    #we do that to put each hotel that belog to this label alone
    for hotels_db in hotel_df_different_db_list:
      hotels_db = hotels_db[hotels_db['labels'] == i].index.tolist()
      hotels_db_list[j] =  hotels_db
      j = j +1

    #creat to database combanision that we should have
    #for example 3 database we do (0,1) (0,2) (1,2)
    my_list = list(range(0,len(dfList)))
    pairs = list(combinations(my_list, 2))

    #based on the database combanision we create our paires
    for item in pairs:
      product = pd.MultiIndex.from_product([hotels_db_list[item[0]] ,hotels_db_list[item[1]] ]).tolist()
      result = result + product

  return result

def indexing_one_database(one_db_index_group , hotels_db):
  result = []
  #one_db_index_group = list of label that have one database items
  for i in one_db_index_group:
    #we get the item with this labael
    hotels_dbA = hotels_db[hotels_db['labels'] == i].index.tolist()
    #create paire
    product = list(combinations(hotels_dbA, 2))
    result = result + product

  return result