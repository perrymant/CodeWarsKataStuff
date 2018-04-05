t = '###########  ###########\n##########    ##########\n#########      #########\n########        ########\n#######          #######\n######            ######\n#####              #####\n####                ####\n###                  ###\n##                    ##\n#                      #\n                        \n'
def invert_triangle(t):
    temp = t.replace(" ","a")
    temp = temp.replace("#"," ")
    temp = temp.replace("a","#")
    return("\n".join(temp.split('\n')[-1::-1]))
