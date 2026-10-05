
def geo_cluster_cleaning_one_database (hotel_df):
  
  #count the number of items for each label.
  counts = hotel_df.groupby('labels').size().reset_index(name='count')
  #Filter the labels that have only one item.
  single_items = counts[counts['count'] == 1]['labels'].tolist()
  #Remove the items that belong to labels with only one item
  df = hotel_df[~hotel_df['labels'].isin(single_items)]

  # group by labels and count the number of unique db_index values in each group
  grouped = hotel_df.groupby('labels')['db_index'].nunique().reset_index(name='unique_db_index_count')

  # divide the groups into two based on the unique db_index count
  one_db_index_group = grouped[grouped['unique_db_index_count'] == 1]['labels'].tolist()

  return one_db_index_group


def geo_cluster_cleaning_more_than_database (hotel_df):
  #count the number of items for each label.
  counts = hotel_df.groupby('labels').size().reset_index(name='count')
  #Filter the labels that have only one item.
  single_items = counts[counts['count'] == 1]['labels'].tolist()
  #Remove the items that belong to labels with only one item
  df = hotel_df[~hotel_df['labels'].isin(single_items)]

  # group by labels and count the number of unique db_index values in each group
  grouped = hotel_df.groupby('labels')['db_index'].nunique().reset_index(name='unique_db_index_count')

  # divide the groups into two based on the unique db_index count
  more_than_one_db_index_group = grouped[grouped['unique_db_index_count'] > 1]['labels'].tolist()

  return more_than_one_db_index_group