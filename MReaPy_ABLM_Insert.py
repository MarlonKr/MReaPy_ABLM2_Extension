from sws_pythoncommands import *

fxname = "ABLM2"

trk_selected = RPR_GetSelectedTrack(0,0)

# Check if ABLM2 is already implemented, if yes, delete all old instances and continue to insert new instances. 
# This way, it is not necessary to manually move ABLM instances and update calibration when adding new FX, 
# just re-trigger this action
while RPR_TrackFX_GetByName(trk_selected,fxname,0) != -1:
    fx_index = RPR_TrackFX_GetByName(trk_selected,fxname,0)
    RPR_TrackFX_Delete(trk_selected,fx_index)

# add isntances    
RPR_TrackFX_AddByName(trk_selected,fxname,False,-1000)
RPR_TrackFX_AddByName(trk_selected,fxname,False,-1040)

index_receive = RPR_TrackFX_GetCount(trk_selected) -1
index_send = 0

#auto assign
RPR_TrackFX_SetParam(trk_selected,index_send,32,1)
RPR_TrackFX_SetParam(trk_selected,index_receive,32,1)

#receive send assign
RPR_TrackFX_SetParam(trk_selected,index_receive,3,1)
RPR_TrackFX_SetParam(trk_selected,index_send,3,0)


