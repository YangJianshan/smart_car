class Servo{
    constructor() {
        this.pitchTimer = null;
        this.horizontalTimer = null;
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
    // 俯仰角度
    //
    static _pitchAngle(angle) {
        let data = JSON.stringify({'method': 'pitch', 'operate': 'set', 'param': {'angle': angle}})
        Servo._post_message('pan-tilt', data, function(res){
            console.log(res);
            let angle = res['result']["angle"];
            $("#pitch_up").attr("value", angle);
            $("#pitch_down").attr("value", angle);
        })
    }

    //
    // 水平角度
    //
    static _horizontalAngle(angle) {
        let data = JSON.stringify({'method': 'horizontal', 'operate': 'set', 'param': {'angle': angle}})
        Servo._post_message('pan-tilt', data, function(res){
            console.log(res);
            let angle = res['result']["angle"];
            $("#horizontal_left").attr("value", angle);
            $("#horizontal_right").attr("value", angle);
        })
    }

    //
    // 关闭俯仰定时器
    //
    clear_pitch_timer(){
        clearInterval(this.pitchTimer);
    }

    //
    // 关闭水平定时器
    //
    clear_horizontal_timer(){
        clearInterval(this.horizontalTimer);
    }

    //
    // 上
    //
    up(){
        this.pitchTimer = setInterval(function(){
            // 获取当前俯仰角度
            let angle = parseInt($("#pitch_up").attr("value")) + 5;
            Servo._pitchAngle(angle);
        }, 400);
    }

    //
    // 下
    //
    down() {
        this.pitchTimer = setInterval(function () {
            // 获取当前俯仰角度
            let angle = parseInt($("#pitch_down").attr("value")) - 5;
            Servo._pitchAngle(angle);
        }, 400);
    }

    //
    // 左
    //
    left() {
        this.horizontalTimer = setInterval(function () {
            // 获取当前俯仰角度
            let angle = parseInt($("#horizontal_left").attr("value")) + 5;
            Servo._horizontalAngle(angle);
        }, 200);
    }

    //
    // 右
    //
    right() {
        this.horizontalTimer = setInterval(function () {
            // 获取当前俯仰角度
            let angle = parseInt($("#horizontal_right").attr("value")) - 5;
            Servo._horizontalAngle(angle);
        }, 200);
    }

    //
    // 复位
    //
    reset(){
        Servo._pitchAngle(90);
        Servo._horizontalAngle(90);
    }

}