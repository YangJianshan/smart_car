# !/usr/bin/python3
# coding=utf-8

from app import app
from flask import render_template


@app.route('/')
def hello_world():
    return render_template('v1/index.html')


@app.route('/car-control')
def car_control():
    return render_template('v1/car_control.html')


@app.route('/pan-tilt')
def pan_tilt_control():
    return render_template('v1/pan_tilt_control.html')
