// 图片分组
var kTypes = function() {
    var args = document.location.search.replace('?', '').split('&');
    for (var i = 0; i < args.length; ++i) {
        var kv = args[i].split('=');
        if (kv[0] == 'type') {
            return kv[1];
        }
    }
    return "all";  // 所有图片
}();

// 重新加载图片
function reloadPictures(num, style) {
    var keys = new Array();
    var args = {};
    args.style = style;
    if (metaData[kTypes]) {
        args.typ = kTypes;
        keys = Object.keys(metaData[kTypes]).map(function(v, idx) {
            return '<img src="img/' + this.typ + "/" + v + '.jpg" typ="' + this.typ + '" tname="' + v + '" ' + style + '/>';
        }, args);
    } else {
        var allType = Object.keys(metaData);
        for (var i=0; i < allType.length; ++i) {
            args.typ = allType[i];
            var tmp = Object.keys(metaData[args.typ]).map(function(v, idx) {
                return '<img src="img/' + this.typ + "/" + v + '.jpg" typ="' + this.typ + '" tname="' + v + '" ' + style + '/>';
            }, args);
            keys = keys.concat(tmp);
        }
    }
    keys.shuffle();
    var images = "";
    num = num < keys.length ? num : keys.length;
    for (var i = 0; i < num; ++i) {
        //$("#pics").append(keys[i]);
        images += keys[i];
    }
    return images;
}

// 随机重排
if (!Array.prototype.shuffle) {
    Array.prototype.shuffle = function() {
        for (var j, x, i = this.length; i; 
                j = parseInt(Math.random() * i), x = this[--i], this[i] = this[j], this[j] = x)
            ;
        return this;
    }
}

//Creating 50 thumbnails inside .grid
//the images are stored on the server serially. So we can use a loop to generate the HTML.
//var images = "", count = 15;
//for(var i = 1; i <= count; i++)
//	images += '<img src="http://thecodeplayer.com/u/uifaces/'+i+'.jpg" />';
// var images = reloadPictures(15, "");
	
//appending the images to .grid
// $(".grid").append(images);

var d = 0; //delay
var ry, tz, s; //transform params

//animation time
$(".animate").on("click", function(){
	//fading out the thumbnails with style
	$("img").each(function(){
		d = Math.random()*1000; //1ms to 1000ms delay
		$(this).delay(d).animate({opacity: 0}, {
			//while the thumbnails are fading out, we will use the step function to apply some transforms. variable n will give the current opacity in the animation.
			step: function(n){
				s = 1-n; //scale - will animate from 0 to 1
				$(this).css("transform", "scale("+s+")");
			}, 
			duration: 1000, 
		})
	}).promise().done(function(){
        // 替换素材
        images = reloadPictures(15, 'style="transform: scale(1); opacity: 0; z-index:99"');
        $(".grid").html("");
        $(".grid").append(images);

		//after *promising* and *doing* the fadeout animation we will bring the images back
		storm();
	})
})

//bringing back the images with style
function storm()
{
	$("img").each(function(){
		d = Math.random()*1000;
		$(this).delay(d).animate({opacity: 1}, {
			step: function(n){
				//rotating the images on the Y axis from 360deg to 0deg
				ry = (1-n)*360;
				//translating the images from 1000px to 0px
				tz = (1-n)*1000;
				//applying the transformation
				$(this).css("transform", "rotateY("+ry+"deg) translateZ("+tz+"px)");
			}, 
			duration: 3000, 
			//some easing fun. Comes from the jquery easing plugin.
			easing: 'easeOutQuint', 
		})
	})
}




