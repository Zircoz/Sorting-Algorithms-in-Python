import threading 
import time
  
def sort(num): 
    time.sleep(num)
    print(num, end = ' ') 
 
to_sort = [9,8,7,6,5,4,3,2,1,0]
for x in to_sort:
    t = threading.Thread(target=sort, args=(x,))
    t.start()