import git
import os, shutil
import yaml, csv
import datetime

GIT_LINK = "https://github.com/Neo23x0/sigma.git"
DEST_FOLDER = "sigma"
OUTPUT = open("sigma_references_output.csv", "w", newline="")
CSV_WRITER = csv.writer(OUTPUT)

def clone_repo(git_link, dest_folder):
    os.mkdir(dest_folder)
    try:
        dest_repo = git.Repo.init(dest_folder)
        origin = dest_repo.create_remote("origin", git_link)
        origin.fetch()
        origin.pull(origin.refs[0].remote_head)
        print("Done cloning")
    except git.GitError as err:
        print(err)


def get_files(dir):
    filenames = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if ".yml" in name:
                filenames.append(os.path.join(root,name))
    return filenames


def write_to_csv(files):
    CSV_WRITER.writerow(["id", "reference", "date", "modified", "file"])
    for file in files:
        print("working on yml file: "+ file)
        with open(file, "r") as f:
            try:
                data = yaml.load_all(f, Loader= yaml.FullLoader)
                document = list(data)[0]
                if "references" not in document and "modified" not in document:
                    CSV_WRITER.writerow([document["id"], "", document["date"], "", document["title"] ])
                elif "modified" not in document:
                    for reference in document["references"]:
                        CSV_WRITER.writerow([document["id"], reference, document["date"], "", document["title"] ])
                elif "references" not in document:
                    CSV_WRITER.writerow([document["id"], "", document["date"], document["modified"], document["title"] ])
                    
                else:
                    for reference in document["references"]:
                        CSV_WRITER.writerow([document["id"], document["title"], reference, document["date"], document["modified"] ])

            except yaml.composer.ComposerError as err:
                print(err)
        print("\n")
        


if __name__ == "__main__":
    #Uncomment if repo not cloned yet
    #clone_repo(GIT_LINK, DEST_FOLDER)

    files = get_files("sigma/rules/")
    #[print(file) for file in files]
    write_to_csv(files)
    
    [print(file) for file in files]