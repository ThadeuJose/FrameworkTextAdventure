from enum import IntEnum
__author__ = 'Thadeu Jose'

#Parser ------------------------------------------------
TITLE = 'Title'
TITLE_INDEX = 0 
DESCRIPTION = "Description"
DESCRIPTION_INDEX = 1
SCENE = "Scene"
SCENE_INDEX = 2
COMMANDS_INDEX = 2 #index from the beginning of the command list

#Debug Message------------------------------------------------
DEBUG_TITLE_SUCESS = "Title successfully added"
DEBUG_DESCRIPTION_SUCESS = "Description successfully added"


def archivetype(arch):
    return "Archive Type: "+str(type(arch))


def scenetype(elem):
    return "Scene Type:"+str(type(elem))


def scenename(elem):
    return "Scene:"+str(elem)


class CommandIndex(IntEnum):
    Command = 0
    Name = 1
    Description = 2

#COMMAND_INDEX = 0
#COMMAND_NAME_INDEX = 1
#COMMAND_DESCRIPTION_INDEX = 2
#Constants of Commands already implements ------------------------
COMMAND_GO = "go"
#GO.
DIRECTION_INDEX = 1
LOCAL_INDEX = 2

COMMAND_SEE = "see"

COMMAND_GET = "get"

COMMAND_ITEM = "item"
ITEM_STATUS_INDEX = 3

COMMAND_START = "start"

COMMAND_NPC = "npc"

COMMAND_END = "end"

COMMAND_STATUS = "status"

#Constants of Status already implements ------------------------
STATUS_INVENTORY = 'inventory'
STATUS_NOT_COLLECTABLE = 'notcollectable'
STATUS_QUANT = 'quant'

#Local Messages ----------------------------------------------
COMMAND_NOT_EXECUTABLE = "This command is not executable in this room"
DIRECTION_NOT_PERMITED = "You cant go to that direction"
DIRECTION_NOT_VALID = 'The direction give is not a valid direction'
