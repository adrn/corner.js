# coding: utf-8

from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Standard library
from datetime import datetime, date, timedelta

# Third-party
import numpy as np
from flask import session, render_template, request, make_response, jsonify

# Project
from . import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/plot/', methods=['POST'])
def plot():
    return
