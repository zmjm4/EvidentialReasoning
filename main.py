
from parseDataToClass import *
from frame import *
from compatibilityRelations import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print (parse.frames)
    print(parse.CR)
    print(parse.questionFrame)
    print('\n')


    frames = Frames()
    frames.organize_frames(parse.frames)
    print(frames.frameInfo)
    print(frames.propositions)

    relations = CompatibilityRelations()
    relations.organize_relations(parse.CR)







if __name__ == "__main__":
    main()


