$(document).ready(function() {
    $(".myvideo").each(function(){
    jwplayer($(this).attr("id")).setup({  
        flashplayer: "/static/plugin/player.flash.swf",  
        file: "/static/video/"+$(this).attr("id")+"."+$(this).attr("type"),  
        image:"static/img/full/26.jpg",
        height: 197,  
        width:350,  
        stretching : 'fill',  
        streamer:"start",  
        provider:"http",  
    });  
    });
});  
