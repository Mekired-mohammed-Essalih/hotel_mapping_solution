from read_data import readJuniper , readTboHotel , readHotelBeds
from more_then_database_main import more_then_database_main
from one_database_main import one_database_main

#read the csv file
dfA = readJuniper()
dfB = readTboHotel()
dfC = readHotelBeds()


#one database code 
#dfList = [dfA ]
#one_database_main(dfList)

#two databases code
dfList = [dfA , dfB]
more_then_database_main(dfList)


#three databases code
#dfList = [dfA , dfB , dfC]
#more_then_database_main(dfList)