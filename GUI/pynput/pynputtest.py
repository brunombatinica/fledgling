#https://www.youtube.com/watch?v=kJshtCfqCsY

from pynput.mouse import Listener
import sys


# define 3 possible input
def on_move(x,y):
    pass

def on_click(x,y,button,pressed):
    print(x,y,button,pressed)
    
    
    
    if button == button.right:
        listener.stop()
        
    pass

def on_scroll(x,y,dx,dy):
    print(x,y,dx,dy)
    pass









with Listener(on_move = on_move, on_click = on_click, on_scroll = on_scroll) as listener:
    listener.join()
