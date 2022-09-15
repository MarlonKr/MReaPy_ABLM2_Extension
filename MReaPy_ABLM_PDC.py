from sws_pythoncommands import *


current = RPR_GetSelectedTrack(0,0)

i = 0
while RPR_GetTrack(0,i) != mediatracknumberError():
    target = RPR_GetTrack(0,i)
    count = RPR_TrackFX_GetCount(target)
    fx = 0
    pdc = 0
    instance =0
    success = False
    while fx < count:
        if RPR_TrackFX_GetEnabled(target,fx) == 1:
            fxname = RPR_TrackFX_GetFXName(target,fx,"",200)[3]
            pdc_new = RPR_TrackFX_GetNamedConfigParm(target, fx, "pdc", "", 20)[4]
            if pdc_new == "":
                pdc_new = "0"
            pdc_new = int(pdc_new)
            pdc += pdc_new

            if fxname == "":
                success = False
                break

            if "ABLM2 (TBProAudio)" in fxname:
                instance += 1
                success = True
                if instance == 1:
                    pass
                if instance == 2:
                    break
        else:
            pass

        fx += 1

    if success == True:
        RPR_TrackFX_SetParam(target,fx,5,pdc/176400)

    if success == False:
        pass

    i+= 1

RPR_SetOnlyTrackSelected(current)
