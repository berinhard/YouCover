// This function is called when an error is thrown by the player
function onPlayerError(errorCode) {
    alert("An error occured of type:" + errorCode);
}


//function playVideo() {
//    if (ytplayer) {
//        ytplayer.playVideo();
//    }
//}
//
//function pauseVideo() {
//    if (ytplayer) {
//        ytplayer.pauseVideo();
//    }
//}
//
//function muteVideo() {
//    if(ytplayer) {
//        ytplayer.mute();
//    }
//}
//
//function unMuteVideo() {
//    if(ytplayer) {
//        ytplayer.unMute();
//    }
//}


// This function is automatically called by the player once it loads
function onYouTubePlayerReady(playerId) {
    ytplayer = $("video_" + playerId);
    ytplayer.cueVideoById(playerId);
}

// The "main method" of this sample. Called when someone clicks "Run".


google.setOnLoadCallback(function()
{
    vController = new VideoController();
    
    vController.loadVideos([
        { "id" : "ylLzyHk54Z0", "nome" : "Google Video" },
        { "id" : "e9wo5lHWhiM", "nome" : "Video do carro" }, 
        { "id" : "Y4oFnnAL4Wc", "nome" : "Pedro cade meu chip" },
    ], "mainContent");

});