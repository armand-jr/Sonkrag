from code.classes import district, house, battery

if __name__ == "__main__":

    current_district = 1

    # Create a graph from our data
    data_district = f"data/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/district_{current_district}/district-{current_district}_batteries.csv"

    district = district.District(data_district, data_batteries)

    # --------------------------- Algoritmes ---------------------------------------

    # --------------------------- Visualisation --------------------------------
    