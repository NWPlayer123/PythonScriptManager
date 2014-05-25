Well hello there, this is just something I thought of randomly while on my way to a 24-hour hackathon and I thought I should actually make it happen. Basically, it's a way to automate python, or really any command line program, script running and processing, because I got kinda tired of having to remember what version of python a script needed and having to do multiple scripts manually in separate folders.

Specification for config.cfg:
Definitions for python's installation directory is #definepy pyXX pathtoexe EG: #definepy py27 C:/python27/python.exe
TypeScript can be a Script or Command.
If Python Script:
TypeScript | PyVersion | ScriptName | ScriptPath
If Command/List of Scripts:
TypeScript | NumScripts | (TypeScript | PyVersion | InstallPath | ScriptPath) #times NumScripts, indented to same place for each consecutive line

Command Line Syntax:
pypkg <type> <script/command> <arguments>
<type> can be -s for a script, -c for a command, or -h to print this help message
<script/command> is what is being run
<arguments> are handled on a per-command basis.