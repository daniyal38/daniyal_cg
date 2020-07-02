import sys
import os


#Current Working Directory
current_dir = os.getcwd()

#Input project name
try:
    project = sys.argv[1]
except:
    print("Please provide a name for your project.")
    exit(1)

#Base folder for the project:
project_dir = os.path.join(current_dir,project)

#Create a directory
def create_dir(folder_name):
    folder_dir = os.path.join(project_dir,folder_name)
    try:
        os.makedirs(folder_dir)
        return folder_dir
    except OSError as e:
        print("Project Folder cannot be created due to : "+e)

#create a file in the given directory


def main():

    #Sub folders:
    folder_a = 'Folder_A'
    folder_b = 'Folder_B'
    folder_c = 'Folder_C'
    folder_d = 'Folder_D'

    #create project skeleton:
    #Folder A
    folder_dir = create_dir(folder_a)

    #Folder B
    folder_dir = create_dir(folder_b)

    #Folder C
    folder_dir = create_dir(folder_c)

    #Folder D
    folder_dir = create_dir(folder_d)

if __name__ == '__main__':
    main()
