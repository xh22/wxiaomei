$(document).ready(function() {
    jwplayer("container").setup({  
        flashplayer: "/static/plugin/player.flash.swf",  
        file: "/static/video/video1.mp4",  
        image:"static/img/full/26.jpg",
        height: 197,  
        width:350,  
        stretching : 'fill',  
        streamer:"start",  
        provider:"http",  
    });  
});  
