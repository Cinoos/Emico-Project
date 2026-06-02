import json

ALLOWED_ACTIONS = [
    "TURN_LIGHT_ON",
    "TURN_LIGHT_OFF",
    "TURN_ROOM_COZY"
]
# TESTING (UNCOMMENT BELOW): 
# #STRING SIMULATION========================================================

# # REMEMBER JSON IS JUST TEXT DATA SO WE HAVE TO CONVERT THIS TEXT INTO A PYTHON DICT/OBJECT HENCE WHY THE ''' BEGINNING AND END
# testing_json = '''
# {
#     "action": "turn_on_light"
# }
# '''

# # Converts JSON to Python Dict and saves into command var
# command = json.loads(testing_json)

# #Check if key "action" exist in dictionary
# if "action" in command:
#     print("There is an action key")
# else:
#     print("There is no key called action")

# #Since action key exist we save whatever value it is paired into "action" variable
# action = command["action"]
# print(action)

# #Check if action value exists in allowed actions
# if "action" in command:
#     print("Action is in allowed actions")
# else:
#     print("Action is now in allowed actions")

def validate_command(command):
    if "action" not in command:
        return False
    
    action = command["action"]

    if action not in ALLOWED_ACTIONS:
        return False

    return True