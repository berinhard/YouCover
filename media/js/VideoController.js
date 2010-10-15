var VideoController = Class.create({

    
    
    initialize : function()
    {
        this.params = {
            allowScriptAccess: "always"
        };

        this._videoHolders = new Array();
    },

    loadVideos : function(videoInfos, container)
    {
       if( !Object.isArray(videoInfos) )
       {
            throw Error("VideoController.loadVideos diz: videoIds não é um array")
       }

       videoInfos.each(function(videoInfo)
       {
            this._videoHolders.push(this._createVideoHolder(videoInfo, container));

       }.bind(this));

    },


    _createVideoHolder : function(videoInfo, container)
    {
        container = $(container);
        
        var _videoSpan;
        var _videoHolder = new Element('span', { 'class' : 'videoHolder' }).insert(
            _videoSpan = new Element('span', { 'id' : ('video_' + videoInfo.id) })
        ).insert(
            new Element("span", { 'class' : 'videoTitle'}).update(videoInfo.nome)
        );

        container.insert(_videoHolder);

        swfobject.embedSWF("http://www.youtube.com/v/" + (videoInfo.id) +
            "&enablejsapi=1&playerapiid=" + (videoInfo.id),
            ('video_' + videoInfo.id), "240", "148", "8", null, null, this.params, { "id" : ('video_' + videoInfo.id) });
    }

});

