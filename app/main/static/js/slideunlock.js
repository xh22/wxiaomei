$(function () {
    if ($("#regist-submit")) $("#regist-submit").attr("disabled",true);
    if ($("#forget-psw")) $("#forget-psw").attr("disabled",true);
    var slider = new SliderUnlock(".slideunlock-slider", {}, function(){
        if ($("#regist-submit")) $("#regist-submit").attr("disabled",false);
        if ($("#forget-psw")) $("#forget-psw").attr("disabled",false);
    }, function(){
        $(".warn").text("index:" + slider.index + "， max:" + slider.max + ",lableIndex:" + slider.lableIndex + ",value:" + $(".slideunlock-lockable").val() + " date:" + new Date().getUTCDate());
    });
    slider.init();

    $("#reset-btn").on('click', function(){
        slider.reset();
    });
})
