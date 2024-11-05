import os
os.chdir('C:/Users/OWNER/Desktop/sample12/val/joker\\')
i=1
for file in os.listdir():
    src=file
    dst="1"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

