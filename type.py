import pyautogui
import time

time.sleep(5)
f=open('sc.txt','r')
x=f.read()
print(x)
z=x.split("\n")
for i in z:
    #print(i.lstrip())
    #i=i[5:]
    pyautogui.typewrite(i.lstrip())
    pyautogui.typewrite("\n")
f.close()





 
                                           