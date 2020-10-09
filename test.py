import git
import os, shutil
import yaml, csv
import datetime


def get_files(dir):
    filenames = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if ".yml" in name:
                filenames.append(os.path.join(root,name))
    return filenames


def get_reference_tags(files):
    for file in files:
        print("working on yml file: "+ file)
        with open(file, "r") as f:
            try:
                count = 0
                data = yaml.load_all(f, Loader= yaml.FullLoader)
                for document in data:
                    count +=1
                
            except yaml.composer.ComposerError as err:
                print(err)
            print(count)
        print("\n")
        


if __name__ == "__main__":
    #Uncomment if repo not cloned yet
    #clone_repo(GIT_LINK, DEST_FOLDER)

    files = get_files("sigma/rules/")
    #[print(file) for file in files]
    get_reference_tags(files)
    
    [print(file) for file in files]