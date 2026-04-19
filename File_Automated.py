import os, shutil
path =r"C:/Users/manas/OneDrive/Desktop/FILE_PYTHON/"
og_files=os.listdir(path)
file_name=['Excel file', 'Image file' , 'webp file', 'Text file']
for loop in range(0,4):
    pathname=os.path.join(path,file_name[loop])
    if not os.path.exists(pathname):
        print(pathname)
        os.makedirs(pathname)
for file in og_files:
    source=os.path.join(path,file)
    if not os.path.isfile(source):
        continue
    if file.lower().endswith(".txt") : 
        destination=os.path.join(path,"Text file", file)
    elif file.endswith(".xlsx"): 
        destination=os.path.join(path,"Excel file", file)
    elif file.endswith(".webp"): 
        destination=os.path.join(path,"webp file", file)
    elif file.endswith((".jpeg", ".jpg", ".png")): 
        destination=os.path.join(path,"Image file", file)
    else :
        print("not moved",file)  
        continue

    shutil.move(source, destination)
