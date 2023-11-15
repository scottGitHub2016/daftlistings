from daftlistings import Daft, Location, SearchType, PropertyType, Distance

daft = Daft()

#Distance = Distance.KM0;
daft.set_location([Location.SLIGO, Location.ROSCOMMON], Distance.KM20)#probably wouldnt needd the distance thing just cover all counties and then use google maps
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_property_type(PropertyType.HOUSE)
daft.set_min_price(150000)
daft.set_max_price(320000)


listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print("Agent Name:",listing.agent_name)
    print("Agency:",listing.agent_branch)
    print("Longatude:", listing.latitude)
    print("Latitude:", listing.longitude)   
    print(listing.size_meters_squared, "m²")
    print(listing.bathrooms)
    print( listing.bedrooms)
    print("**TODO**")
    print("Mortgage Monthly Est")
    print("Mortgage Total Interest")
    print("Distance to Crozon")
    print("Fibre BB")
    print("5G Signal")
    #print(listing.distance_to(54.2612883,-8.4743678))
    print()
