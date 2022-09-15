from sws_pythoncommands import *

current = RPR_GetSelectedTrack(0, 0)

i = 0
j=0
while RPR_GetTrack(0, i) != mediatracknumberError():
    success = False
    target = RPR_GetTrack(0, i)
    fx = 0
    instance = 0
    fxnum = RPR_TrackFX_GetCount(target)
    while fx <= fxnum:
        fxname = RPR_TrackFX_GetFXName(target, fx, "", 200)[3]

        if fxname == "":
            success = False
            break

        if "ABLM2 (TBProAudio)" in fxname:
            instance += 1
            success = True
            if instance == 1:
                instance1_id = fx
                pass
            if instance == 2:
                instance2_id = fx

                break

        fx += 1

    if success == True:
        j = j+1
        RPR_TrackFX_SetParam(target, instance1_id, 3, 0)
        RPR_TrackFX_SetParam(target, instance2_id, 3, 1)

        RPR_TrackFX_SetParam(target, instance1_id, 4, j / 257)
        RPR_TrackFX_SetParam(target, instance2_id, 4, j / 257)
        pass
    else:
        pass

    i += 1