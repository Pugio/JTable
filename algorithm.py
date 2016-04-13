from pulp import *

def check_host_guest_match(host, guest):
	match_result = True
	host_seats = host["seats_available"]
	#print "seats in host = ", host_seats
	guest_seats = guest["seats_requested"]
	#print "seats for guest = ", guest_seats
	if(host_seats < guest_seats):
		match_result = False
	if((host["children_ok"] == False) and (guest["children_requested"] == True)):
		match_result = False
	if((host["babies_ok"] == False) and (guest["babies_requested"] == True)):
		match_result = False
	if((host["vegetarians_ok"] == False) and (guest["vegetarians_requested"] == True)):
		match_result = False
	#check if host banned the guest
	guest_id = guest["user_id"]
	for banned_guest_id in host["Banned_users"]:
		if(guest_id == banned_guest_id):
			match_result = False
	#check if guest banned the host
	host_id = host["user_id"]
	for banned_host_id in guest["Banned_users"]:
		if(host_id == banned_host_id):
			match_result = False

	return match_result

def matching_algorithm(info_dict):
    #create the list of variables

    edge_num = -1;
    edges = []
    for host in info_dict["hosts"]:
    	for guest in info_dict["guests"]:
    		if (check_host_guest_match(host,guest)):
    			edge_num+=1
    			variable_name = "edge"+str(edge_num)
    			print variable_name
    			var = LpVariable(variable_name, 0, 1)
    			edge = {"variable": var, "guest_id": guest["user_id"], "host_id": host["user_id"], "weight": guest["seats_requested"]}
    			edges.append(edge)

    print "The total number of edges is ", len(edges)


    prob = LpProblem("MealMatch", LpMinimize)


    # create cost function 
    prob += 0.013*edges[0]["variable"] + 0.008*edges[1]["variable"], "Total Cost of Ingredients per can"

	# create constraints
    prob += edges[1]["variable"] + edges[1]["variable"] == 100, "PercentagesSum"

    prob.solve()

    print("Status:", LpStatus[prob.status])

    for v in prob.variables():
        print(v.name, "=", v.varValue)




host0 = {"user_id": 0, "seats_available": 3, "children_ok": False, "vegetarians_ok": False, "babies_ok": False,  "Is_Meat": True, "Banned_users": [10]}
host1 = {"user_id": 1, "seats_available": 2, "children_ok": False, "vegetarians_ok": False, "babies_ok": False,  "Is_Meat": True, "Banned_users": [10]}
host2 = {"user_id": 2, "seats_available": 3, "children_ok": False, "vegetarians_ok": True, "babies_ok": False,  "Is_Meat": False, "Banned_users": [10]}
host3 = {"user_id": 3, "seats_available": 4, "children_ok": True, "vegetarians_ok": True, "babies_ok": True,  "Is_Meat": True, "Banned_users": [11,12]}
host4 = {"user_id": 4, "seats_available": 2, "children_ok": False, "vegetarians_ok": False, "babies_ok": False,  "Is_Meat": True, "Banned_users": []}
host5 = {"user_id": 5, "seats_available": 3, "children_ok": False, "vegetarians_ok": True, "babies_ok": False,  "Is_Meat": True, "Banned_users": [19]}
host6 = {"user_id": 6, "seats_available": 2, "children_ok": False, "vegetarians_ok": True, "babies_ok": False,  "Is_Meat": False, "Banned_users": []}



guest0 = {"user_id": 10, "seats_requested": 1, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": True, "Banned_users": []}
guest1 = {"user_id": 11, "seats_requested": 2, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": True, "Banned_users": [0]}
guest2 = {"user_id": 12, "seats_requested": 1, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": False, "Dairy_ok": True, "Banned_users": []}
guest3 = {"user_id": 13, "seats_requested": 2, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": True, "Banned_users": [0,2,3]}
guest4 = {"user_id": 14, "seats_requested": 2, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": True, "Banned_users": []}
guest5 = {"user_id": 15, "seats_requested": 1, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": True, "Banned_users": [0,4]}
guest6 = {"user_id": 16, "seats_requested": 2, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": False, "Dairy_ok": True, "Banned_users": []}
guest7 = {"user_id": 17, "seats_requested": 2, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": False, "Banned_users": []}
guest8 = {"user_id": 18, "seats_requested": 4, "babies_requested": False, "children_requested": True, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": True, "Banned_users": []}
guest9 = {"user_id": 19, "seats_requested": 1, "babies_requested": False, "children_requested": False, "vegetarians_requested": False, "Meat_ok": True, "Dairy_ok": True, "Banned_users": []}


check = check_host_guest_match(host0,guest0)
print "the host and guest 0 match as: ", check

x = {"hosts": [host0, host1, host2, host3, host4, host5, host6], "guests": [guest0, guest1, guest2, guest3, guest4, guest5, guest6, guest7, guest8, guest9]}
matching_algorithm(x)



