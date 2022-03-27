from turtle import window_height, window_width
from flask import Flask, render_template
from pynput.mouse import Listener

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

def on_move(x, y):
    print("Move!")

def on_click(x, y, button, pressed):
    print("Click!")
    if {0} >= 0 and {0} <= (window_width / 2) and {1} >= 0 and {1} <= (window_height / 2):
        return render_template("img1.html")
        sleep(2)
    elif {0} >= (window_width / 2) and {0} <= window_width and {1} >= 0 and {1} <= (window_height / 2):
        return render_template("img2.html")
        sleep(2)
    elif {0} >= 0 and {0} <= (window_width / 2) and {1} >= (window_height / 2) and {1} <= window_height:    
        return render_template("img3.html")
        sleep(2)
    elif {0} >= (window_width / 2) and {0} <= window_width and {1} >= (window_height / 2) and {1} <= window_height:
        return render_template("img4.html")
        sleep(2)

def on_scroll(x, y, dx, dy):
    print("Scroll!")