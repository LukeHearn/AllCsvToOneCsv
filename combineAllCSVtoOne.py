import pandas as pd
import os
from glob import glob







#YOUR PATH
PATH = r'C:\Users\test'
#Your File Name, in this example JPM.CSV
EXT = "*JPM.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]
#Find all Files that Match JPM.CSV keyword
print(all_csv_files)




combined_csv = pd.concat( [ pd.read_csv(f) for f in all_csv_files ] )
#output to current working directory of file
combined_csv.to_csv( "combined_csv.csv", index=False )