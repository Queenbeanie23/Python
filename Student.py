# this is the Pickle Version Of student Information
class studentInfo:
    def __init__(self, name, ID, major, height):
        self.name = name
        self.ID = ID
        self.major = major
        self.height = height

    def set_name(self, name):
        self.name = name

    def set_ID(self, ID):
        self.ID = ID

    def set_major(self, major):
        self.major = major

    def set_height(self, height):
        self.height = height

    def get_name(self):
        return self.name

    def get_ID(self):
        return self.ID

    def get_major(self):
        return self.major

    def get_height(self):
        return self.height

import pickle

FILENAME = 'contactdata.dat'

def main():
        repeat = 'y'
        output_file= open(FILENAME, 'wb')

        while repeat.lower() == 'y':
            name = input("Enter Name: ")
            ID= input("Enter ID: ")
            major= input("Enter major: ")
            height= input("Enter height: ")

            Info = studentInfo(name,ID,major,height)

            pickle.dump(Info,output_file)

            repeat = input('Enter more data? (y/n): ')

            output_file.close()
            print('The data  was written to', FILENAME)

main()




