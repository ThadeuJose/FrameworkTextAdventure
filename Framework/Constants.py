from enum import IntEnum, Enum

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


class Printm:
    NOT_PRINT = 0
    ON_SCREEN = 1
    ON_FILE = 2






class CommandIndex(IntEnum):
    Command = 0
    Name = 1
    Description = 2


#Constants of Commands already implements ------------------------
class CommandConst:
    GO = "go"
    SEE = "see"
    GET = "get"
    ITEM = "item"
    START = "start"
    NPC = "npc"
    END = "end"
    STATUS = "status"
    OPEN = "open"
    END = "end"
    INV = "inv"

#GO.
DIRECTION_INDEX = 1
LOCAL_INDEX = 2

ITEM_STATUS_INDEX = 3


#Constants of Status already implements ------------------------
class StatusConst:
    INVENTORY = 'inventory'
    COLLECTABLE = 'collectable'
    QUANT = 'quant'
    CONTAINER = 'container'
    INSIDE = 'inside'
    VISIBLE = "visible"


#Local Messages ----------------------------------------------
COMMAND_NOT_EXECUTABLE = "This command is not executable in this room"
DIRECTION_NOT_PERMITED = "You cant go to that direction"
DIRECTION_NOT_VALID = 'The direction give is not a valid direction'
