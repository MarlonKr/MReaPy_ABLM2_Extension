from sws_pythoncommands import *

farbe_ab = RPR_ColorToNative(255,128,64)
grau = RPR_ColorToNative(192,192,192)
gelb = RPR_ColorToNative(255, 255, 0)

rot = RPR_ColorToNative(255, 0, 0)
rotdunkel = RPR_ColorToNative(128, 0, 0)
rothell = RPR_ColorToNative(255, 128, 128)

violetthell = RPR_ColorToNative(255, 128, 255)
violettdunkel = RPR_ColorToNative(64,0,64)
lavendel = RPR_ColorToNative(128, 128, 255)


blaudunkel = RPR_ColorToNative(0, 0, 160)
blauhell = RPR_ColorToNative(0, 128, 255)

gruen = RPR_ColorToNative(0,255,64)
gruenhell = RPR_ColorToNative(128,255,128)
gruenekel = RPR_ColorToNative(128,128,0)
gruenazur = RPR_ColorToNative(0,128,128)

weiss = RPR_ColorToNative(255, 255, 255)
schwarz = RPR_ColorToNative(0, 0, 0)

pink = RPR_ColorToNative(255,0,128)




def settrackcolor(farbe):
    test = RPR_GetSelectedTrack(0, 0)
    RPR_SetTrackColor(test, farbe)
