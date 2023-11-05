import os
import sys
import argparse
import shutil
# error messaging
def error_Handler(errmsg):
    print(f"\t Usage: python {sys.argv[0]} -h for help\n")
    print("\t [?] Error: %s \n" % (errmsg))
    sys.exit()

# parse arguments
def argument_handler():
    parser = argparse.ArgumentParser("FindErase")

    parser.add_argument(
        "target_Folder_or_File", 
        required=True,
        help="The name of the folder to search for.")
    
    parser.add_argument(
        "-d",
        "--directory",
        default='.',
        required=False,
        help='The directory to start the search from. Default is the current directory ex -d PATH_TO_DIR or --directory PATH_TO_DIR',
    )

    parser.add_argument(
        "-s",
        "--save",
        default='example.txt',
        required=False,
        help='Save Findings From The Search to a Specified File Name  ex -s findings.txt  or --save results.txt',
    )


    parser.add_argument(
        "-r",
        "--rename",
        type=str,
        default=None,
        required=False,
        help='The New name you want to rename the target_file or target_folder with ex -r NEW_NAME_TO_DIR or --directory NEW_NAME_TO_FILE',
    )

    parser.add_argument(
        "-d",
        "--delete",
        type=str,
        default=False,
        required=False,
        help='Give a Delete option to Remove the target_file or target_folder ex -d TARGET_DIR_OR_FILE or --directory TARGET_DIR_OR_FILE',
    )

    parser.add_argument(
        "-v",
        "--verbose",
        type=bool,
        default=True,
        required=False,
        help="Disable Verbose Mode to stop printing to the screen while Finding,Renaming Or Deleting Files :ie -v off or --verbose False",
    )
    parser.error = error_Handler
    return parser.parse_args()


class FindErase:
    def __init__(self,target_Folder_or_File, directory, verbose,save, file_name,delete,rename):
        self.verbose = verbose
        self.target = target_Folder_or_File
        self.directory = directory     
        self.file_name = file_name
        self.found_assets = []
        self.save = save
        self.delete =delete
        self.rename = rename

    # Find The Asset File Or Directory
    def asset_Finder(self):
        if self.verbose:
            print(f"\tBeginning Search For: {self.target}")

        if self.verbose:
            print(f"\tAttempting Search for folders... {self.target}")

        for root, dirs, files in os.walk(self.directory):
            if self.target in dirs:
                folder_path = os.path.join(root,self.target)
                if self.verbose:
                    print(f"\n\t\tFound a Match Folder: {folder_path}")
                if self.save:
                    self.found_assets.append(folder_path)
                if self.delete:
                    print(f"Deleted Folder: {folder_path}")
                    shutil.rmtree(folder_path)

            # Add code here to delete the folder if desired
            # Example: shutil.rmtree(folder_path)
    
    # save results to a file
    def saveResults(self):
        if self.save:
            if self.verbose == True:
                print("s\n\t [-] Saving Found File/Folders In file %s \n" % (self.file_name))
  
            with open(str(self.file_name), "wt") as f:
                for name in self.found_assets:
                    name = f"{name}"
                    f.write("\n%s" %name)
         
def main():
    args = argument_handler()
    save = args.save
    action = FindErase()
    
    action.nameGenerator()
    if save:
        action.saveResults()
    print('\n\t [!] Process Completed With Exiting Status Ok!...')

if __name__ == "__main__":
    
    main()









