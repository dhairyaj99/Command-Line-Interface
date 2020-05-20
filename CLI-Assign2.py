from cmd import Cmd
import os
import sys
import fnmatch

class MyCLI(Cmd):

    prompt = ">> "

    def do_exit(self, args):
        """
        Exits the system
        """

        raise SystemExit()

    def do_pwd(self, args):
        """
        Prints current working directory of the shell
        """
        currentdirectory = os.getcwd()
        print(currentdirectory)

    def do_ls(self, arg):
        """
        Prints all files and folders in the working directory
        """
        filesinfolder = os.listdir(os.curdir)

        print(*filesinfolder, sep=" ")

    def do_cd(self, arg):
        """
        Changes the current working directory to the one given by the user
        :param arg: Input given by the user- represents new working directory in this case
        :return:
        """
        t = os.path.isdir(arg)
        if t != True:
            print("Directory doesn't exist")
        else:
            os.chdir(arg)

    def do_find(self, arg):
        """
        Prints files and folders within a folder of the working directory
        :param arg: Name of the folder given by the user
        :return:
        """
        filess = []
        if arg == "":
            for root, dirs, files in os.walk(os.curdir):
                if arg in files:
                    filess.append(os.path.join(root, arg))
                    print(*filess, sep=" ")
        else:
            print("Write a filename")

    def do_search(self, arg):
        """
        Locates files with matching content
        :param arg: User inputted text to locate
        :return:
        """

        for root, dirs, files in os.walk(os.curdir):
            filess = [f for f in files if os.path.isfile(root + '\\' + f)]

            for file in filess:
                file = root + '\\' + file
                fileo = open(file)

                for line in fileo:
                    line = line.lower()

                    if re.search(arg, line):
                        print("Text given: " + args + " was found in" + file)

                fileo.close()

    def do_head(self, arg):
        """
        Allows user to preview file content- max 5 lines
        :param arg: Name of file
        :return:
        """
        i = 0
        file = os.curdir + "\\" + arg
        filer = open(file)
        for l in filer:
            print(l, end='')
            i += 1
            if i == 5:
                break

    def do_run(self, arg):
        """
        Allows user to run scripts
        :param arg: File name of the script
        :return:
        """
        file = os.curdir + "\\" + arg

        try:
            os.system(arg+ ".scriptscript")
        except:
            print("An error has occurred")

    def do_ln(self, arg):
        """
        Displays names of note files
        :param arg: name of note files
        :return:
        """
        filess = fnmatch.filter(os.listdir(os.curdir), "*.notenote")
        print(*filess, sep=" ")

    def do_tn(self, arg, name):
        """
        Allows user to append text to a file
        :param arg: Text the user would like to append
        :param name: Name of file
        :return:
        """
        if arg != "" & name != "":
            fo = open(name +'.notenote', 'w+')
            fo.write(arg)
            fo.close()
        else:
            print("Please add content for file or write name of file")

    def do_vn(self, arg):
        """
        Displays the content of the note
        :param arg: File name of the note
        :return:
        """

        if arg != "":
            fo=open(arg+'.notenote')
            for line in fo:
                print(line)
        else:
            print("Please add a file name")

if __name__ == "__main__":

    app = MyCLI()
    app.cmdloop('Enter a command to do something: ')
