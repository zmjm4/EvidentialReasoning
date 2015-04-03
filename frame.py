from analysis import *

# Author Tami Hong Le
# 3/7/2015
#
# organize_frames:  Organizes the frames information and propositions into another list
#
# loops over each index of the frames list, extract the frame information and
# propositions. Each elements are assigned in a new list called framesInfo and
# propositions.


class Frames:

    propositions = []
    frameInfo = []

    def __init__(self):
        pass

    def organize_frames(self,frames):

        for elements in frames:
            splitter = elements.split(":")

            self.frameInfo.append(splitter[1:7])
            self.propositions.append(splitter[6].split('/'))

        return self.frameInfo, self.propositions





