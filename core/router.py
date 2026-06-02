# ACTION FUNCTIONS
#These are the functions that will execute 
# =====================================================
def TURN_LIGHT_ON():
    print("LIGHT TURNED ON")

# ACTION ROUTER
#This is the router that will call a function from above depending what the function we need (the param) 
#========================================================
def route_action(action):

    if action == "TURN_LIGHT_ON":
        TURN_LIGHT_ON()

    else:
        print("No route found")