from sws_python import *
from colors import *
from datetime import datetime

def mine_track_find_loudness():
    i = 0
    while RPR_GetTrack(0,i) != mediatracknumberError():
        if "LiveLoudness" in getname(RPR_GetTrack(0,i)):
            return i
        i += 1

def mine_projectname():
    return RPR_GetProjectName(0, "", 100)[1]

def mine_tracks_hideunselected():
    sws_command("_SWSTL_HIDEUNSEL")
def mine_tracks_unselect_all():
    sws_command("40297")

def mine_randomizer():
    now = datetime.now().time()  # time object
    now = str(now)
    now = float(now[-1])
    now = now / 2
    now = str(now)
    now = now[-1]
    #debug(now)

    if now == "5":
        now = 1
    else:
        now = 0
    return now

def mine_trackselection_save():
    sws_command("_SWS_SAVESEL")

def mine_trackselection_restore():
    sws_command("_SWS_RESTORESEL")

def selectonlychildren():
    sws_command("_SWS_SELCHILDREN")

def parentsend(track,boolean):
    RPR_SetMediaTrackInfo_Value(track, "B_MAINSEND", boolean)


def UserInput(Title, Caption, Inputs,Feldtext):
    input = RPR_GetUserInputs(Title,Inputs,Caption,Feldtext,20)

    return input[4]

def mediatracknumberError():
    return "(MediaTrack*)0x0000000000000000"

def gettracknumber(track):
    number = RPR_GetMediaTrackInfo_Value(track, "IP_TRACKNUMBER")
    number = int(number)
    return number

def sws_command(id):
    id = RPR_NamedCommandLookup(id)
    RPR_Main_OnCommand(id,0)

# make-commmands
def rename(track, name):
    RPR_GetSetMediaTrackInfo_String(track, "P_NAME", name, 1)

def inserttrackabove():
    inserttrackabove = RPR_NamedCommandLookup("_SWS_INSRTTRKABOVE")
    RPR_Main_OnCommand(inserttrackabove, 0)

def scriptmode():
    mode = RPR_GetTrack(0,0)
    if getname(mode) == "thisisamix":
        return "mix"
    
    elif getname(mode) == "thisissoundesign":
        return "sounddesign"

    elif getname(mode) == "thisismastering":
        return "mastering"

    else:
        return 0

def selectparent():
    temp = RPR_NamedCommandLookup("_SWS_SELPARENTS")
    RPR_Main_OnCommandEx(temp, 0, 0)


# group
def overview():
    overview = RPR_NamedCommandLookup("_44d3efc3ed9804448b267b20200595c6")
    RPR_Main_OnCommand(overview, 0)


def getgroupfree():
    track_selected = RPR_GetSelectedTrack(0, 0)
    inserttrackatend()
    track_index = RPR_GetSelectedTrack(0, 0)
    index = RPR_GetMediaTrackInfo_Value(track_index, "I_TRACKNUMBER")
    cuttrack()
    i = 0
    for i in range(int(index)):
        track_scan_fx_current = RPR_GetTrack(0, i)
    if RPR_GetSetTrackGroupMembership(i, "VOLUME_LEAD", 1, 1) == 1:
        freegroup = i

def insertpluginspecific(fxname):

    trk_selected = RPR_GetSelectedTrack(0, 0)
    fx_count = RPR_TrackFX_GetCount(trk_selected)
    fx_count = int(fx_count)
    i = 0
    instance =0
    while i < fx_count:
        name = RPR_TrackFX_GetFXName(trk_selected,i,"",100)[3]
        if "ablm" in name.lower():
            if instance == 1:

                index2 = i

            if instance == 0:
                index1 = i
                instance += 1

        i+= 1
        pass

    position = -1000 - index2


    RPR_TrackFX_AddByName(trk_selected, fxname, False, position)
    fx_index = RPR_TrackFX_GetByName(trk_selected, fxname, 0)
    RPR_TrackFX_Show(trk_selected, fx_index, 1)


def focus(string):
    #overview()
    counter = 0
    while RPR_GetTrack(0, counter) != "(MediaTrack*)0x0000000000000000":
        target = RPR_GetTrack(0, counter)
        target_name = RPR_GetTrackName(target, "", 1000)[2]

        if string in target_name:
            RPR_SetOnlyTrackSelected(target)
            selectalsochildrenandzoom()
            break
        else:
            counter += 1

            continue




def gettrack(trackname):
    counter = 0


    while RPR_GetTrack(0, counter) != "(MediaTrack*)0x0000000000000000":
        target = RPR_GetTrack(0, counter)
        target_name = RPR_GetTrackName(target, "", 1000)[2]

        if trackname in target_name:
            return target

        else:
            counter += 1



def checkifmix():
    track1 = RPR_GetTrack(0, 0)
    checknameraw = RPR_GetTrackName(track1, "", 100)
    checkname = checknameraw[2]
    if checkname == "thisisamix":
        return True
    else:
        return False


# check if track exists
def checktrackexist(name):
    i = 0
    is_mixbus_true = False
    while i < 300:
        check = RPR_GetTrack(0, int(i))
        checknameraw = RPR_GetTrackName(check, "", 100)
        checkname = checknameraw[2]
        if checkname == name:
            # is_mixbus_true = True
            return True
            pass

        else:
            i += 1
            is_mixbus_true = False

    if is_mixbus_true == False:
        return False


# def checkifinstrumentexists:

"""
    if is_mixbus_true == False:

        if name == "top":
            maketracktop()

        elif name == "mixbus":
            maketrackmixbus()

        elif name == "arrangement":
            maketrackarrangement()

    else:
        pass

"""


def inserttrackhere():
    RPR_Main_OnCommandEx(40001, 0, 0)


def inserttrackatend():
    RPR_Main_OnCommandEx(40702, 0, 0)


def inserttrackatbeginning():
    RPR_InsertTrackAtIndex(0, 0)




def timeselection_equals_itemrange():
    itemrange = RPR_NamedCommandLookup("_RS794b356600321b50864219ba254b268f9dc1973d")
    RPR_Main_OnCommandEx(itemrange, 0, 0)


def insert_empty_item():
    RPR_Main_OnCommandEx(40142, 0, 0)


def cuttrack():
    RPR_Main_OnCommandEx(40059, 0, 0)


def copytrack():
    RPR_Main_OnCommandEx(40057, 0, 0)


def pastetrack():
    RPR_Main_OnCommandEx(42398, 0, 0)


def maketrackarrangement():
    if checktrackexist("top") == False:
        maketracktop()
    else:
        pass
    # create arrangement
    findandselect("top", "only")
    inserttrackhere()
    global track_arrangement
    track_arrangement = RPR_GetSelectedTrack(0, 0)
    RPR_GetSetMediaTrackInfo_String(track_arrangement, "P_NAME", "arrangement", 1)
    settrackcolor(rot)
    # select top and reorder

    findandselect("top", "only")
    track_top = RPR_GetSelectedTrack(0, 0)
    RPR_SetOnlyTrackSelected(track_top)
    findandselect("arrangement", "add")
    makeselectedparent()


def maketracksounddesign():
    RPR_InsertTrackAtIndex(0, 0)
    global track_sounddesign
    track_sounddesign = RPR_GetSelectedTrack(0, 0)
    # reorder
    RPR_SetOnlyTrackSelected(track_sounddesign)
    RPR_ReorderSelectedTracks(0, 0)
    RPR_SetOnlyTrackSelected(track_arrangement)
    RPR_ReorderSelectedTracks(0, 0)
    RPR_SetOnlyTrackSelected(track_top)
    RPR_ReorderSelectedTracks(0, 0)




# Command-Aliases
def debug(x, *argv):
    try:
        argv
    except NameError:
        argv = x
        # funktioniert noch nicht :(
    RPR_ShowMessageBox(x, str(argv), 0)


# transport
# record

def setloopstart():
    RPR_GetPlayPositionEx(0)
    RPR_Main_OnCommandEx(40222, 0, 0)


def setloopend():
    RPR_GetPlayPositionEx(0)
    RPR_Main_OnCommandEx(40223, 0, 0)


def midirec():
    # enableMetronome
    RPR_Main_OnCommandEx(41745, 0, 0)  # inGeneral
    metr_playback_off = RPR_NamedCommandLookup("_SWS_AWMPLAYOFF")
    RPR_Main_OnCommandEx(metr_playback_off, 0, 0)  # disablePlaybackMetronome
    metr_rec_on = RPR_NamedCommandLookup("_SWS_AWMRECON")
    RPR_Main_OnCommandEx(metr_rec_on, 0, 0)

    # Record
    recordtoggle = RPR_NamedCommandLookup("_SWS_RECTOGGLE")
    selected = RPR_GetSelectedTrack(0, 0)
    # deselect all the other tracks

    # TPC wiederherstellen
    show = RPR_NamedCommandLookup("_SWSTL_SHOWALL")
    RPR_Main_OnCommandEx(show, 0, 0)

    # disarm
    RPR_Main_OnCommandEx(40035, 0, 0)
    RPR_Main_OnCommandEx(40491, 0, 0)

    # Arm
    RPR_SetOnlyTrackSelected(selected)
    RPR_SetMediaTrackInfo_Value(selected, "I_RECARM", 1)
    RPR_SetMediaTrackInfo_Value(selected, "I_RECINPUT", 4096 | 0 | (63 << 5))

    RPR_Main_OnCommandEx(recordtoggle, 0, 0)


# Tracks

def settoprevioustrackfolder():
    folderprev = RPR_NamedCommandLookup("_SWS_FOLDERPREV")
    RPR_Main_OnCommandEx(folderprev, 0, 0)

def selectalsochildrenandzoom():

    selecttrackchildren = RPR_NamedCommandLookup("_0a042c85b261804ca5b910076a87f9b2")
    RPR_Main_OnCommand(selecttrackchildren, 0)
    zoom_tracks = RPR_NamedCommandLookup("_SWS_VZOOMFITMIN")  # zoom to tracks
    RPR_Main_OnCommand(zoom_tracks, 0)
    RPR_Main_OnCommand(40421, 0)  # select items
    zoom_items = RPR_NamedCommandLookup("_SWS_HZOOMITEMS")  # zoom to items
    RPR_Main_OnCommand(zoom_items,0)

def selectchildren():
    selchildren = RPR_NamedCommandLookup("_SWS_SELCHILDREN2")
    RPR_Main_OnCommandEx(selchildren, 0, 0)


def hideunselected():
    hideunsel = RPR_NamedCommandLookup("_SWSTL_HIDEUNSEL")
    RPR_Main_OnCommandEx(hideunsel, 0, 0)


def makeselectedparent():
    makeparent = RPR_NamedCommandLookup("_XENAKIOS_SELTRACKSASFOLDER")
    RPR_Main_OnCommandEx(makeparent, 0, 0)


def makefirstselectedparent():
    makechildren = RPR_NamedCommandLookup("SWS_MAKEFOLDER")
    RPR_Main_OnCommandEx(makechildren, 0, 0)


def makefolder(track, name):
    makefolder = RPR_NamedCommandLookup("_SWS_MAKEFOLDER")
    RPR_Main_OnCommandEx(makefolder, 0, 0)
    RPR_GetSetMediaTrackInfo_String(track,"P_NAME",f"{name} bus",1)


# envelopes
def showenvelopes():
    showenraw = RPR_NamedCommandLookup("_BR_T_SHOW_ACT_FX_ENV_SEL_TRACK")
    RPR_Main_OnCommandEx(showenraw, 0, 0)


def uncollapseall():
    uncollapseraw = RPR_NamedCommandLookup("_SWS_UNCOLLAPSE")
    RPR_Main_OnCommandEx(40035, 0, 0)
    RPR_Main_OnCommandEx(uncollapseraw, 0, 0)


# fx

def showfxchain():
    showfx = RPR_NamedCommandLookup("_S&M_TOGLFXCHAIN")
    RPR_Main_OnCommandEx(showfx, 0, 0)


# def userinput(title, text, example):
def getguid():
    selected = RPR_GetSelectedTrack(0, 0)
    trackguid = RPR_GetTrackGUID(selected)
    return str(trackguid)


def findandselectguid(trackguid):
    for i in range(300):
        selected = RPR_GetSelectedTrack(0, 0)
        selectedguid = RPR_GetTrackGUID(selected)
        if selectedguid == trackguid:
            RPR_SetOnlyTrackSelected(selected)
            break
        else:
            continue


def findandselect(stringor0, onlyoradd):
    if stringor0 == 0:
        targetraw = RPR_GetUserInputs("Trackfinder-Terminal", 1, "Which track to find?", "trackname", 30)
        target = targetraw[4]
    else:
        target = stringor0

    all_tracks_count = 0
    while all_tracks_count < 400:
        fx_current_track = RPR_GetTrack(0, all_tracks_count)
        fx_currentnameraw = RPR_GetTrackName(fx_current_track, "", 100)
        fx_currentname = fx_currentnameraw[2]

        if fx_currentname == target:
            if onlyoradd == "only":
                RPR_SetOnlyTrackSelected(fx_current_track)
            else:
                RPR_SetTrackSelected(fx_current_track, 1)
            break

        else:
            all_tracks_count += 1
            continue


def selectall():
    RPR_Main_OnCommandEx(40035, 0, 0)


def minimumtracksize():
    RPR_Main_OnCommandEx(40110, 0, 0)


def nexttrack():
    next_track_raw = RPR_NamedCommandLookup("_XENAKIOS_SELNEXTTRACK")
    next_track = RPR_Main_OnCommandEx(next_track_raw, 0, 0)


def previoustrack():
    prev_track_raw = RPR_NamedCommandLookup("_XENAKIOS_SELPREVTRACK")
    prev_track = RPR_Main_OnCommandEx(prev_track_raw, 0, 0)


def bpmfinder():
    startposition = RPR_GetPlayPositionEx(0)
    bpmtrack = RPR_TimeMap_GetDividedBpmAtTime(startposition)

    bpmcalc = bpmtrack / float(60)
    debug(bpmcalc, "Schläge pro Sekunde")

    beat = startposition * bpmcalc

    debug(float(beat), "Takt an dieser Stelle")


def selectnextenvelopepoint():
    nextenvpoint = RPR_NamedCommandLookup("_BR_ENV_SEL_NEXT_POINT")
    RPR_Main_OnCommandEx(nextenvpoint, 0, 0)


def selectpreviousenvelopepoint():
    prevenvpoint = RPR_NamedCommandLookup("_BR_ENV_SEL_PREV_POINT")
    RPR_Main_OnCommandEx(prevenvpoint, 0, 0)

def getname(track):
    name= RPR_GetTrackName(track, "", 1000)[2]
    return name

"""

    bpm2 = float(beat - int(beat))

    # RPR_ShowMessageBox(startposition, "start", 0)

    if round(bpm2, 1) == 0.0:
        bpm2 = 1
    elif round(bpm2, 1) == 0.2:
        bpm2 = 2
    elif round(bpm2, 1) == 0.5:
        bpm2 = 3
    elif round(bpm2, 1) == 0.75:
        bpm2 = 4

    bpm1 = math.floor(beat)

    debug(bpm1, "bpm1")

    bpm = float(f"{bpm1}.{bpm2}")
    # debug(bpm,"bpm")
    setloopstart()

    # RPR_ShowMessageBox(startposition, "start", 0)
    # RPR_ShowMessageBox(bpm, "start", 0)

    # RPR_ShowMessageBox(round(beat, 2), "full", 0)
    # PR_ShowMessageBox(math.floor(beat), "math.floor", 0)
    # RPR_ShowMessageBox(bpm2, "decimal", 0)
    # RPR_ShowMessageBox(bpm, "result",0)

    # endposition = startposition +
    # RPR_GetSet_LoopTimeRange(1, 1, startposition, endOut, allowautoseek)
    
    """
