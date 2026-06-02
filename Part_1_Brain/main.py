# Imports all the functions we made from the other py files into here
from Part_1_Brain.listen import record_audio
from Part_1_Brain.transcribe import transcribe_audio
from Part_1_Brain.brain import brain
from Part_1_Brain.speak import speak
from core.validator import validate_command
from core.router import route_action
#parses our JSON from the llm
import json 

# get audio (note: param is length of time of listening. ie listen for 5 seconds)
#Makes a variable and we run the function record_audio() and whatever it returns is saved into the var. In this case audio_file is our recorded audio
audio_file = record_audio(5)

# transcribe audio
#Same thing here with variable and function but the transcribed audio is saved into text
text = transcribe_audio(audio_file)

# give to llm and save response SHOULD BE JSON**
res = brain(text)

#Parse the json and save to command
command = json.loads(res)

#Validate and save if its true or false (valid or not)
is_valid = validate_command(command)

#Checks the result if it is valid or not
if is_valid:
    print("Command is valid!")
    action = command["action"]
    route_action(action)
else:
    print("Command not valid ;(")

# #Have it speak our response out loud
# speak(res)
