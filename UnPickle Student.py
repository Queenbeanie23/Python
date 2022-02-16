# this is the UnPickle Version Of student Information
import Student
import pickle

FILENAME = 'contactdata.dat'

def main():
    end_of_file = False

    input_file= open(FILENAME, 'rb')

    while not end_of_file:
        try:
            inform = pickle.load(input_file)

            display_data(inform)
        except EOFError:
            end_of_file = True

    input_file.close()


def display_data(inform):
    print('name:', inform.get_name())
    print('ID:', inform.get_ID())
    print('Major:', inform.get_major())
    print('height:', inform.get_height())
    print()

main()
