from code.classes import district, house, battery

if __name__ == "__main__":

    current_district = str(1)

    # Create a graph from our data
    data_houses = f"data/houses&batteries/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/houses&batteries/district_{current_district}/district-{current_district}_batteries.csv"
    
    district = district.District(data_houses, data_batteries)

    print(district)


    # --------------------------- Algoritmes ---------------------------------------

    # --------------------------- Visualisation --------------------------------
    