import os
os.chdir('C:\\Users\\OWNER\\Desktop\\Dataset-20231018T214536Z-001.zip\\Dataset\\train\\joker\\')
i=1
for file in os.listdir():
    src=file
    dst="0"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

