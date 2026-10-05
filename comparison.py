import recordlinkage

def comparison(hotel_df  , candidate_links):

  compare = recordlinkage.Compare()

  compare.exact('phonetic_trans_name', 'phonetic_trans_name', label="phonetic_trans_name")
  compare.exact('phonetic_trans_address', 'phonetic_trans_address', label='phonetic_trans_address')


  compare.string("trans_name", "trans_name", method="jarowinkler", label="trans_name")
  compare.string("trans_address", "trans_address" ,method="jarowinkler" ,  label="trans_address")

  #compare.exact("phone_number", "phone_number",label="phone_number")
  features = compare.compute(candidate_links, hotel_df)
  return features