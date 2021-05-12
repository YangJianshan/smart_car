//
// 小车控制
//
class CarControl {
    constructor() {
        this._add_on();
    }

    _add_on() {
        let other = this;
        if (CarControl._isMobile()) {  // 移动端
            // 左前
            $("#car_left_ahead").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setLeftAhead();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

            // 前
            $("#car_ahead").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setAhead();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

            // 右前
            $("#car_right_ahead").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setRightAhead();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });


            // 左
            $("#car_left").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setLeft();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

            // 转向
            $("#car_turn_round").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setTurnRound();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

            // 右
            $("#car_right").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setRight();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

            // 左后
            $("#car_left_backward").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setLeftBackward();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

            // 后
            $("#car_backward").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setBackward();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

            // 右后
            $("#car_right_backward").on("touchstart touchend", function (event) {
                if ("touchstart" == event.type) {
                    other.setRightBackward();
                } else if ("touchend" == event.type) {
                    other.setStop();
                }
            });

        } else {  // pc端
            // 左前
            $("#car_left_ahead").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setLeftAhead();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });

            // 前
            $("#car_ahead").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setAhead();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });

            // 右前
            $("#car_right_ahead").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setRightAhead();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });


            // 左
            $("#car_left").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setLeft();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });

            // 转向
            $("#car_turn_round").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setTurnRound();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });

            // 右
            $("#car_right").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setRight();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });

            // 左后
            $("#car_left_backward").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setLeftBackward();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });

            // 后
            $("#car_backward").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setBackward();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });

            // 右后
            $("#car_right_backward").on("mousedown mouseup", function (event) {
                if ("mousedown" == event.type) {
                    other.setRightBackward();
                } else if ("mouseup" == event.type) {
                    other.setStop();
                }
            });
        }
    }

    static _isMobile() {
        let userAgentInfo = navigator.userAgent;
        let mobileAgents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
        let mobile_flag = false;
        //根据userAgent判断是否是手机
        console.log(userAgentInfo);
        for (let v = 0; v < mobileAgents.length; v++) {
            if (userAgentInfo.indexOf(mobileAgents[v]) > 0) {
                console.log(mobileAgents[v]);
                mobile_flag = true;
                break;
            }
        }
        let screen_width = window.screen.width;
        let screen_height = window.screen.height;
        //根据屏幕分辨率判断是否是手机
        if (screen_width < 500 && screen_height < 800) {
            mobile_flag = true;
        }
        return mobile_flag;
    }

    static _post_message(url, data, success) {
        $.post({
            url: url,
            data: data,
            success: success,
            dataType: "json",
        })
    }

    //
    // 停止
    //
    setStop() {
        let data = JSON.stringify({'method': 'stop', 'operate': 'set'});
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 向前
    //
    setAhead() {
        let data = JSON.stringify({'method': 'straight_ahead', 'operate': 'set', 'param': {'direction': 'ahead'}});
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 向后
    //
    setBackward() {
        let data = JSON.stringify({'method': 'straight_ahead', 'operate': 'set', 'param': {'direction': 'backward'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 向左
    //
    setLeft() {
        let data = JSON.stringify({'method': 'side_way', 'operate': 'set', 'param': {'direction': 'left'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 向右
    //
    setRight() {
        let data = JSON.stringify({'method': 'side_way', 'operate': 'set', 'param': {'direction': 'right'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 左前
    //
    setLeftAhead() {
        let data = JSON.stringify({'method': 'diagonal', 'operate': 'set', 'param': {'direction': 'left_ahead'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 右前
    //
    setRightAhead() {
        let data = JSON.stringify({'method': 'diagonal', 'operate': 'set', 'param': {'direction': 'right_ahead'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 左后
    //
    setLeftBackward() {
        let data = JSON.stringify({'method': 'diagonal', 'operate': 'set', 'param': {'direction': 'left_backward'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 右后
    //
    setRightBackward() {
        let data = JSON.stringify({'method': 'diagonal', 'operate': 'set', 'param': {'direction': 'right_backward'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }

    //
    // 转向
    //
    setTurnRound() {
        let data = JSON.stringify({'method': 'turn_round', 'operate': 'set', 'param': {'direction': 'clockwise'}})
        CarControl._post_message('/car', data, function (res) {
            console.log(data);
        })
    }
}
