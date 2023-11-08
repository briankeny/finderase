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
        "-a",
        "--asset",
        required=True,
        help="The name of the folder your searching for. usage  -a FOLDER_OR_FILE or --asset FOLDER_OR_FILE ")
    
    parser.add_argument(
        "-d",
        "--directory",
        default='.',
        required=False,
        help='The directory to start the search from. Default is the current directory. usage  -d PATH_TO_DIR or --directory PATH_TO_DIR',
    )

    parser.add_argument(
        "-s",
        "--save",
        default=None,
        required=False,
        help='Save Findings From The Search to a Specified File Name. Usage  -s findings.txt  or --save results.txt',
    )


    parser.add_argument(
        "-r",
        "--rename",
        default=None,
        required=False,
        help='The New name you want to rename the target_file or target_folder with. Usage Example  -r NEW_NAME_TO_DIR or --rename NEW_NAME_TO_FILE',
    )

    parser.add_argument(
        "-del",
        "--delete",
        default=None,
        required=False,
        help='Give a Delete option to Remove the target_file or target_folder. Usage Example -del TARGET_DIR_OR_FILE or --delete TARGET_DIR_OR_FILE',
    )

    parser.add_argument(
        "-v",
        "--verbose",
        type = bool,
        default=True,
        required=False,
        help="Disable Verbose Mode to stop printing to the screen while Finding,Renaming Or Deleting Files :Usage Example -v off or --verbose False",
    )
    parser.error = error_Handler
    return parser.parse_args()


class FindErase:
    def __init__(self,target_Folder_or_File="", directory="", verbose=True,save=False, file_name="test.txt",delete=False,rename=False):
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
            print(f"\n\tBeginning Search...")

        if self.verbose:
            print(f"\n\tAttempting Search for {self.target} in folders...")

        for root, dirs, files in os.walk(self.directory):
            # Find in Directories
            if self.target in dirs:
                folder_path = os.path.join(root,self.target)
                if self.verbose:
                    print(f"\n\t\t[+]Found a Match Folder: {folder_path}")
  
            # Delete the folder if desired
                if self.delete:
                    print(f"\n\t\t[-]Deleting Folder: {self.target} from path {folder_path}")
                    shutil.rmtree(folder_path)
                
                if  self.rename:
                    print(f"\n\t\t[?]Renaming Folder: {self.target} to {self.file_name}")
                    new_path = os.path.join(root,self.new_name)
                    shutil.move(folder_path,new_path)
                    shutil.rmtree(folder_path)
                
                # Update Found List
                self.found_assets.append(folder_path)
  
        if self.verbose:
            print(f"\n\t[{len(self.found_assets)}] Search Complete...")

    
    # save results to a file
    def saveResults(self):
        if self.save:
            if self.verbose == True:
                print("s\n\t [-] Saving Found File/Folders In file %s \n" % (self.file_name))
  
            with open(str(self.file_name), "wt") as f:
                for name in self.found_assets:
                    name = f"{name}"
                    f.write("\n%s" %(name))
         
def main():
    args = argument_handler()
    target_Folder_or_File = args.asset
    directory = args.directory
    save = args.save
    delete = args.delete
    rename = args.rename
    verbose = args.verbose

    new_name = ""
    file_name = "" 
 
    if save and 0 < len(save) < 20:
        file_name = f'{save}.txt'
        save = True
    

    if delete and  0 < len(delete) < 20 :
        delete = True

    if  rename and  len(delete)< 0 and 0 < len(rename) < 20:
        new_name = rename
        rename = True
          
    action = FindErase(target_Folder_or_File=target_Folder_or_File, directory=directory, verbose=verbose,save=save, file_name=file_name,delete=delete,rename=rename)    
    action.asset_Finder()

    if save:
        action.saveResults()

    print('\n\t [!] Process Completed With Exiting Status 0 Ok!...\n')

if __name__ == "__main__":    
    main()

