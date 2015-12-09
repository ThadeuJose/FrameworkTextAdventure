__author__ = 'Thadeu Jose'

#Interpreter ------------------------------------------------
TITLE = 'Title'
TITLE_INDEX=0
DESCRIPTION = "Description"
DESCRIPTION_INDEX = 1
SCENE = "Scene"
SCENE_INDEX = 2
COMMANDS_INDEX = 2 #index from the beginning of the command list
COMMAND_HANDLE = 0
COMMAND_INDEX = 0
DIRECTION_INDEX = 1
LOCAL_INDEX=2


#Debug Message------------------------------------------------
DEBUG_TITLE_SUCESS="Title successfully added"
DEBUG_DESCRIPTION_SUCESS="Description successfully added"

def archivetype(arch):
    return "Archive Type: "+str(type(arch))

def scenetype(elem):
    return "Scene Type:"+str(type(elem))

def scenename(elem):
    return "Scene:"+str(elem)


#Command Constants already implements ------------------------
COMMAND_GO="go"

#Local Messages ----------------------------------------------
COMMAND_NOT_EXECUTABLE = "This command is not executable in this room"
DIRECTION_NOT_PERMITED = "You cant go to that direction"
DIRECTION_NOT_VALID = 'The direction give is not a valid direction'