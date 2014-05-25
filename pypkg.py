import os, sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("pypkg <type> <script/command> <arguments>")
        print("<type> can be -s for a script, -c for a command, or -h to print this help message")
        print("<script/command> is what is being run")
        print("<arguments> are handled on a per-command basis.")
        sys.exit()
    elif sys.argv[1] == '-h':
        print("pypkg <type> <script/command> <arguments>")
        print("<type> can be -s for a script, -c for a command, or -h to print this help message")
        print("<script/command> is what is being run")
        print("<arguments> are handled on a per-command basis.")
        sys.exit()
    elif sys.argv[1] == '-s':
        script = sys.argv[2]
        defpy = []
        with open("config.cfg", "r+") as inf:
            lines = inf.readlines()
            define = [s for s in lines if "#definepy" in s]
            matching = [s for s in lines if script in s]
            for numline, entry in enumerate(define):
                defpy.append(entry.split(" ", 3))
            for numline, entry in enumerate(matching, 1):
                if entry.startswith('Script'):
                    scriptcmd = entry.split(" | ")
                    for i, elem in enumerate(defpy):
                        for j, version in enumerate(elem):
                            if scriptcmd[1] in version:
                                os.system(defpy[i][j+1].rstrip() + " " + os.path.join(scriptcmd[3].rstrip(), scriptcmd[2] + ".py") + " " + str(" ".join(sys.argv[3:])))
            inf.close()
    elif sys.argv[1] == '-c':
        script = sys.argv[2]
        defpy = []
        with open("config.cfg", "r+") as inf:
            lines = inf.readlines()
            define = [s for s in lines if "#definepy" in s]
            for numline, entry in enumerate(define):
                defpy.append(entry.split(" ", 3))
            for i, s in enumerate(lines, 1):
                if script in s:
                    if s.startswith("Command"):
                        scriptcmd = s.split(" | ")
                        endloop = int(scriptcmd[2])
                        array = []
                        chkindex = []
                        testarr = []
                        for x in range(endloop):
                            linenum = i-1+x
                            test2 = lines[linenum].split(" | ")
                            array.append(" ".join(test2).rsplit())
                            testchk = array[0][3].split(";")
                        for y, z in enumerate(testchk):
                            if z.startswith("!"):
                                chkindex.append(1)
                            else:
                                chkindex.append(0)
                        needarg = chkindex.count(0)
                        oparg = chkindex.count(1)
                        testarr.append(str(needarg))
                        for test3 in range(oparg):
                            testarr.append(str(needarg+test3+1))
                        if str(len(sys.argv[3:])) not in testarr:
                            print("Not enough arguments!")
                        else:
                            for w, v in enumerate(array):
                                if w == 0:
                                    for q, elem in enumerate(defpy):
                                        for r, version in enumerate(elem):
                                            if array[w][4] in version:
                                                os.system(elem[2].rstrip() + " " + os.path.join(array[w][6], array[w][5] + ".py") + " " + str(" ".join(sys.argv[3:])))
                                else:
                                    for q, elem in enumerate(defpy):
                                        for r, version in enumerate(elem):
                                            if array[w][0] in version:
                                                os.system(elem[2].rstrip() + " " + os.path.join(array[w][2], array[w][1] + ".py") + " " + str(" ".join(sys.argv[3:])))
