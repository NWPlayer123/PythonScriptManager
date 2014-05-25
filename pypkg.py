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
                                os.system(defpy[i][j+1].rstrip() + " " + os.path.join(scriptcmd[3].rstrip(), scriptcmd[2] + ".py") + " " + str(sys.argv[3]))
            inf.close()