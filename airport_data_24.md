#### All 24 airports with their geographic coordinates
> Note: Longitude values should be NEGATIVE for US airports (Western Hemisphere)
```
AIRPORTS = {
    "ATL": Airport("ATL", "Atlanta", "GA", -84.3880, 33.7490),
    "AUS": Airport("AUS", "Austin", "TX", -97.7431, 30.2672),
    "BOS": Airport("BOS", "Boston", "MA", -71.0096, 42.3656),
    "BWI": Airport("BWI", "Baltimore", "MD", -76.6413, 39.2904),
    "DCA": Airport("DCA", "Washington D.C.", "VA", -77.0369, 38.9072),
    "DEN": Airport("DEN", "Denver", "CO", -104.9903, 39.7392),
    "DFW": Airport("DFW", "Dallas", "TX", -96.7967, 32.7767),
    "DTW": Airport("DTW", "Detroit", "MI", -83.0458, 42.3314),
    "EWR": Airport("EWR", "Newark", "NJ", -74.1745, 40.7357),
    "IAD": Airport("IAD", "Washington D.C.", "VA", -77.4558, 38.8821),
    "IAH": Airport("IAH", "Houston", "TX", -95.3698, 29.7604),
    "JFK": Airport("JFK", "New York City", "NY", -73.7781, 40.6413),
    "LAS": Airport("LAS", "Las Vegas", "NV", -115.1398, 36.1699),
    "LAX": Airport("LAX", "Los Angeles", "CA", -118.2437, 34.0522),
    "MDW": Airport("MDW", "Chicago", "IL", -87.6298, 41.8781),
    "MIA": Airport("MIA", "Miami", "FL", -80.1918, 25.7617),
    "MSP": Airport("MSP", "Minneapolis", "MN", -93.2650, 44.9778),
    "PDX": Airport("PDX", "Portland", "OR", -122.6762, 45.5051),
    "PHL": Airport("PHL", "Philadelphia", "PA", -75.1652, 39.9526),
    "RDU": Airport("RDU", "Raleigh-Durham", "NC", -78.7870, 35.7796),
    "SAN": Airport("SAN", "San Diego", "CA", -117.1611, 32.7157),
    "SEA": Airport("SEA", "Seattle", "WA", -122.3321, 47.6062),
    "SFO": Airport("SFO", "San Francisco", "CA", -122.4194, 37.7749),
    "SLC": Airport("SLC", "Salt Lake City", "UT", -111.8910, 40.7608),
}
```

#### Route connections (bidirectional edges)
> Format: source airport code -> list of destination airport codes
```

ROUTES = {
    "ATL": ["RDU", "AUS", "BOS", "BWI", "DCA", "DEN", "DFW", "DTW", "EWR", 
            "IAD", "IAH", "JFK", "LAS", "LAX", "MDW", "MIA", "MSP", "PDX", 
            "PHL", "SAN", "SEA", "SFO", "SLC"],
    "AUS": ["ATL", "BOS", "DTW", "JFK", "RDU", "LAS", "LAX", "MSP", "SEA", "SLC"],
    "BOS": ["SLC", "RDU", "AUS", "ATL", "DTW", "MSP", "SEA", "LAX", "DEN", 
            "JFK", "IAD", "MIA", "PHL", "IAH", "LAS"],
    "BWI": ["ATL", "DTW", "MSP", "JFK", "SLC", "BOS"],
    "DCA": ["ATL", "JFK", "BOS", "DTW", "MSP", "SLC"],
    "DEN": ["ATL", "MSP", "SLC", "DTW"],
    "DFW": ["ATL", "MSP", "DTW", "SLC"],
    "DTW": ["ATL", "MSP", "DTW", "SLC", "LAX"],
    "EWR": ["BOS", "JFK", "ATL", "RDU", "MIA", "LAX", "SFO", "SEA"],
    "IAD": ["ATL", "BOS", "DTW", "MSP", "RDU", "SLC"],
    "IAH": ["ATL", "DTW", "SLC"],
    "JFK": ["ATL", "DTW", "MSP", "SLC"],
    "LAS": ["LAX", "ATL", "MIA", "DFW", "BOS", "SFO", "DTW", "SEA", "MSP"],
    "LAX": ["ATL", "MSP", "DTW", "SLC", "LAX", "SEA", "SFO", "DFW"],
    "MDW": ["JFK", "SFO", "SLC", "ATL", "LAS", "MSP", "BOS", "DTW", "SEA", "PDX"],
    "MIA": ["ATL", "DTW", "MSP"],
    "MSP": ["ATL", "JFK", "LAX", "BOS", "DFW", "DCA"],
    "PDX": ["ATL", "DEN", "DFW", "SEA", "LAS", "LAX"],
    "PHL": ["SEA", "LAX", "SFO", "SLC", "MSP", "ATL", "DTW"],
    "RDU": ["ATL", "BOS", "JFK", "DTW", "MSP", "SLC"],
    "SAN": ["ATL", "BOS", "DTW", "MSP", "LAX", "SLC"],
    "SEA": ["MSP", "SEA", "SLC", "ATL", "DTW", "JFK"],
    "SFO": ["LAX", "SLC", "ATL", "MSP", "SFO", "DFW", "DEN", "LAS"],
    "SLC": ["LAX", "JFK", "SAN", "SEA", "DEN", "SLC", "DFW", "PDX"],
}
```
