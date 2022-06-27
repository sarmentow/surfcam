from flask import Flask, request, render_template
import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from utils import make_gif
app = Flask(__name__)

state = dict()
state["cam_state"] = 0
state["img_number"] = 0
state["burst_state"] = 0
state["BURST_IMAGE_SIZE"] = 91
state["delay_state"] = 0
state["last_pic_time"] = ""

@app.route("/status", methods=["GET"])
def status():
    global state
    if state["cam_state"] == 1:
        return "1"
    else:
        return "0" 

@app.route("/mode/<int:mode>", methods=["POST"])
def set_mode(mode):
    global state
    if mode == 1:
        state["cam_state"] = 1
    else:
        state["cam_state"] = 0

    return "OK"


@app.route("/pics", methods=["POST"])
def receive_pics():
    global state
    print(state["img_number"])

    if state["img_number"] >= state["BURST_IMAGE_SIZE"] and state["burst_state"] == 1:
        state["img_number"] = 0
        state["cam_state"] = 0
        state["burst_state"] = 0
        state["delay_state"] = 0
        state["last_pic_time"] = str(datetime.datetime.now(tz=datetime.timezone(-datetime.timedelta(hours=3))))
        make_gif()
        return "OK"


    filename = state['img_number'] if state['img_number'] >= 10 else f'0{state["img_number"]}'
    with open(f"static/images/{filename}.jpeg", "wb") as i:
        i.write(request.get_data())

    state["img_number"] += 1 

    return "OK"


@app.route("/burst", methods=["POST"])
def start_burst():
    global state

    if state["burst_state"] == 0:
        state["delay_state"] = 1
        state["cam_state"] = 1
        state["burst_state"] = 1
        state["img_number"] = 0

        return "OK"
    else:
        return "Can't start burst state; It's already on"

@app.route("/delay", methods=["GET"])
def get_delay_flag():
    global state

    if state["delay_state"] == 1:
        return "1"
    else:
        return "0"
@app.route("/", methods=["GET"]) 
def index():
    global state
    return render_template("index.html", last_time=state["last_pic_time"])
