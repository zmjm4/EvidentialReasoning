from compatibilityRelation import *
from parseDataToClass import *
from frame import *
from utils import *
from output import *




def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print("Information from the Input.txt are parsed :\n")
    print(parse.questionFrame)
    print (parse.frames)
    print(parse.CR)
    print(parse.FOD)
    print('\n')

    file_write("The Question is : \n\n")

    #To write out to an output text file for the question and answers
    for k,v in parse.questionFrame.items():
        print(v[0])
        file_write("\t" + v[0] + '\n\n')
        file_write("The answers to the question is : \n\n")

        for i in v[1]:
            answers = i.split(',')

            for j in answers:
                file_write("\t" + j + '\n')

    CR = CompatibilityRelations()
    CR.get_relations(parse.CR)

    frame = Frames()
    frame.organize_frames(parse.frames,parse.FOD)
    #frame.get_crossProductFrames(parse.FOD,CR.crossed_frame)

    file_write("ENTERING ANALYSIS\n\n\n")

    countFOD = len(parse.FOD)

    count = 1

    while countFOD != 0:
        try:
            frame_zero = parse.FOD[0].split(':')
            frame_one = parse.FOD[1].split(':')

            x = 4
            y = 4

            file_write('\tFrame before translation \n')
            file_write('\t_____________________________________________________________\n\n')
            file_write('\t{0:10}{1}\n\n'.format("Frame:", frame_zero[1] + ' and ' + frame_one[1]))
            file_write('\t{0:50}{1}\n\n'.format("Propositions before translating","Begin Mass"))

            len_of_frame_zero = len(frame_zero) - 2
            len_of_frame_one = len(frame_one) - 2

            while x < len_of_frame_zero:
                file_write('\t{0:50}{1:1.3f}\n'.format(frame_zero[x+1].strip(),float(frame_zero[x].strip())))
                x = x +2

            while y < len_of_frame_one:
                file_write('\t{0:50}{1:1.3f}\n'.format(frame_one[y+1].strip(),float(frame_one[y].strip())))
                y = y +2

            file_write('\n\n\n')
            frame.get_crossProductFrames(parse.FOD[0], parse.FOD[1], CR.crossed_frame,count)

            parse.FOD.remove(parse.FOD[0])
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.insert(0,frame.insertFrame)

            count = count + 1

        except IndexError:

            break

    print(parse.FOD)

    interpret = Analysis()
    interpret.interpret(interpret.b,CR.crossed_frame ,interpret.final_dic)



if __name__ == "__main__":
    main()
