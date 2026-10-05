import re
import phonetics
import pandas as pd
import numpy as np
from transliterate import buckwalter

# define function to clean phone number
def clean_phone(phone):
    return re.sub(r'\D+', '', str(phone))

def detect_numbers(string):
    numbers = re.findall(r'\d+', string)
    return numbers

def phonetic_name(string):
    metaphone_result =  phonetics.metaphone(string)
    numbers = detect_numbers(string)
    return metaphone_result + ''.join(numbers)

def preprocessing (dfList):

  hotel_df  = [None] * len(dfList)

  for i in range(len(dfList)):
    df = dfList[i].loc[:, ["id" , "name" , "address" , "latitude" , "longitude" , "phone_number" ]].values
    df = pd.DataFrame(df)
    # adding column name to the respective columns
    df.columns =["id", "name" , "address" ,  "lat" , "long", "phone_number" ]
    #add column db_index
    df["db_index"] = i
    #replace nan address with "" so we don't have problems
    df['name'] = df['name'].replace(np.nan, "")
    df['address'] = df['address'].replace(np.nan, "")

    #delete row with null lat and long
    df = df.dropna(axis=0, subset=['lat'])

    #clean phone
    df['phone_number'] = df['phone_number'].apply(clean_phone)

    # create a new column trans_name and trans_address
    df['trans_name'] = df.apply(lambda row: buckwalter.transliterate(row['name']), axis = 1)

    df['trans_address'] = df.apply(lambda row: buckwalter.transliterate(row['address']), axis = 1)

    #create a new column phonetic_trans_name and  phonetic_trans_address
    df["phonetic_trans_name"] = df.apply(lambda row: phonetic_name(row['trans_name']), axis = 1)

    df["phonetic_trans_address"] = df.apply(lambda row: phonetics.metaphone(row['trans_address']), axis = 1)

    #make id the index to help us in indexing step so it use ids instand of  normal index
    df.set_index('id', inplace=True)

    hotel_df[i] = df


  hotel_df = pd.concat(hotel_df)
  
  return hotel_df