from typing import Self
from flask import Flask, render_template, g
from ShirtController import ShirtController
from ShirtService import ShirtService
import threading
import requests

class WebPage:
    app = Flask(__name__)
    base = str()
    endp = str()

    def __init__(self, baseurl: str, endpurl:str):
        global base, endp
        base = baseurl
        endp = endpurl

    @app.route('/page', methods=['GET'])
    def page():
        controller = ShirtController(ShirtService())
        def run_api():
            controller.run()
        background_thread = threading.Thread(target=run_api, daemon=True)
        background_thread.start()
        results = requests.get(base+endp).json()
        return render_template("index.html", **locals())
    
    def run(self):
        self.app.run(host='0.0.0.0', port = 81)