def print_hotel_data(row_number, result, hotel_df):
    # Get the IDs from the specified row
    ids = result.loc[row_number, ['id0', 'id1']].tolist()

    # Flatten the IDs into a single list
    flat_ids = [id for sublist in ids for id in sublist]

    # Get the rows from the hotel_df that match the IDs
    matching_rows = hotel_df[hotel_df.index.isin(flat_ids)]

    # Print the matching rows
    return matching_rows