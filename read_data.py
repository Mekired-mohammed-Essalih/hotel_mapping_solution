import pandas as pd 

def readJuniper():
    #read the csv file
    dfA = pd.read_csv("Juniper.csv")
    # adding column name to the respective columns
    dfA.columns =["id", "name", "zone_code", "category" , "address" , "latitude" , "longitude" , "phone_number" , "mail" , "fax" , "description" , "image" , "zone_jpd_code" , "tripadvisor" , "tripadvisor_reviews"]
    
    return dfA 

def readTboHotel():
   #read the csv file
   dfB = pd.read_csv("tbo_hotel.csv")
   #get only the att we need
   dfB.columns =["id", "name", "category" , "address" , "latitude" , "longitude" , "phone_number" , "mail" , "fax" , "description" , "image" , "zone_jpd_code" , "tripadvisor" , "tripadvisor_reviews"]

   dfBcopie = pd.DataFrame(dfB)

   hotel = dfBcopie['id'].tolist()

   my_list = [str(i) for i in hotel]

   dfB["id"] = my_list 

   return dfB

def readHotelBeds():
    #read the csv file
    dfC = pd.read_csv("hotelBeds_hotel.csv")
    #get only the att we need
    dfC.columns =['id', 'name', 'category' , 'address' , "latitude" , "longitude" , "phone_number" , "mail" , "fax" , "description" , "image" , "zone_code" ]

    dfCcopie = pd.DataFrame(dfC)

    hotel = dfCcopie['id'].tolist()

    my_list = [str(i) for i in hotel]

    dfC["id"] = my_list

    dfC = dfC.drop_duplicates(subset='id')

    return dfC