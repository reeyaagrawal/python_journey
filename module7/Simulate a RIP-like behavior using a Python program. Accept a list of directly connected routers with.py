n = int(input("Enter number of routers: "))

routing_table = {}

print("Enter router and hop count:")

for i in range(n):
    router, hop = input().split()
    routing_table[router] = int(hop)

for r in range(1, 4):

    print("\nRound", r)

    for router in routing_table:
        new_hop = routing_table[router] + 1

        if new_hop < routing_table[router]:
            routing_table[router] = new_hop

    print("Routing Table:", routing_table)