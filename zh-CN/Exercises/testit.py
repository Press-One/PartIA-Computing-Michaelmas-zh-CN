import os
idir = r'.\PartIA-Computing-Michaelmas-zh-CN\zh-CN\Exercises'
files = os.listdir(idir)


print(files)
for ifile in files:
    ifilename = idir+"\\"+ifile
    if ifilename.endswith("ipynb"):
        af = ifilename.replace(" ","_")
        os.rename(ifilename,af)
