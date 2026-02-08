# airports contains a list of airport names ["ATL", "JFK", "LAX"]
# routes contains a list of tuples [("ATL", "JFK", 800), ("JFK", "LAX", 2500)]
# each tuple: (source_airport, destination_airport, distance_in_miles)
def build_matrix(airports, routes): 
    # create empty dictionary to map airport name to a number (human readable names to matrix redable indices)
    name_to_idx = {}
    # create empty list to map indices back to airport names for displaying results back to users
    idx_to_name = []

    # assign each airport a unique index
    # enumerate enumerate(airports) produces pairs: (0, "ATL")(1, "JFK")(2, "LAX")
    for i, name in enumerate(airports):
        name_to_idx[name] = i       # e.g. {"ATL": 0, "JFK": 1, "LAX": 2} after three iterations
        idx_to_name.append(name)    # e.g. ["ATL", "JFK", "LAX"] after three iterations

    # number of airports
    N = len(airports)

    # build the adjacency matrix
    # if no route exists between airports distance = infinity
    INF = float("inf")

    # a N * N matrix, and every element initialized to infinity (the weight)
    # loop N times and don't use the counter (_)
    # graph = [
    # [INF, INF, INF],  # Row 0: distances from airport 0
    # [INF, INF, INF],  # Row 1: distances from airport 1
    # [INF, INF, INF]   # Row 2: distances from airport 2
    # ]

    #        To:    ATL(0)  JFK(1)  LAX(2)
    # From: ATL(0)  [  ?   ,  ?  ,   ?   ]
    #       JFK(1)  [  ?   ,  ?  ,   ?   ]
    #       LAX(2)  [  ?   ,  ?  ,   ?   ]

    graph = [[INF]*N for _ in range(N)]

    # set diagonal to zero
    for i in range(N):
        # diagonal
        graph[i][i] = 0 #airport to itself is 0

    # tuple unpacking。 e.g. src, des, dist = ("ATL", "JFK", 800)
    for src, des, dist in routes:
        u = name_to_idx[src]    # u = 0
        v = name_to_idx[des]    # v = 1
        graph[u][v] = dist      # access row u, column v, which is the distance in the matrix, store it to dist
    return graph