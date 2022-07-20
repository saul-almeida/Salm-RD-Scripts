# This script will zero all atributes translate, rotate and scale selected objects
# For Dp_Ar_control will copy originalRotate values to Rotate.
from maya import cmds

# Declaring variables
selList = cmds.ls(sl=True)
axisList = ['X','Y','Z']
dpControl = 'originalRotate'

for item in selList:
    for axis in axisList:
        try:
            cmds.setAttr(item+'.translate'+axis, 0)
        except Exception as e:
            print(e)
        try:
            cmds.setAttr(item+'.rotate'+axis, 0)
            # Check if 'useOriginalRotation' atribute exist.
            if not cmds.objExists(item+'.useOriginalRotation'):
                origRotate = cmds.getAttr(item+'.'+dpControl+axis)
                copyAtribute = cmds.setAttr(item+'.rotate'+axis,origRotate)
        except Exception as e:
            print(e)
        try:
            cmds.setAttr(item+'.scale'+axis, 1)
        except Exception as e:
            print(e)