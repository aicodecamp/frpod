import os

from pathlib import Path



# combine_txt: Appends the content of a text file to another file, with a header indicating the source file.
def combine_txt( from_file, to_file):
    basename = Path(from_file).stem

    with open(to_file , 'a', encoding='utf-8') as fh_to:
        fh_to.writelines( ["###"+basename+".\n"])
        with open(from_file, 'r', encoding='utf-8') as fh_from:
            lines = fh_from.readlines()

        fh_to.writelines(lines)




# combine_folder: Combines all text files in a folder into a single file, appending their content sequentially.
def combine_folder(path : str , to_file: str)  :
 
 
    for ( dirpath, dirnames, filenames ) in os.walk( os.path.abspath(path)):
    # print(filenames)
    # print(dirpath)
        for filename in sorted(filenames):
            basename, extension = os.path.splitext(filename)
            if extension =='.txt':
                from_file = os.path.join(dirpath, filename)
                combine_txt(from_file, to_file)
    


if __name__ == '__main__':
    from_dir = 'D:\\jason\\projects\\frpod\\build\\Job-Interview-Preparation-Simplified'
    to_file = 'D:\\jason\\projects\\frpod\\build\\combined-interview.txt'
    combine_folder( from_dir, to_file )