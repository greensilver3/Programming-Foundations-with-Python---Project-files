import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program is sKriLLex" +time.ctime())
while(break_count < total_breaks):
 time.sleep(10)
 print("take a break")
 webbrowser.open("https://www.youtube.com/watch?v=ZkqyIoYAXV8")
 break_count = break_count + 1
