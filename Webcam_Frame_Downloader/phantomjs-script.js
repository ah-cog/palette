var page = require('webpage').create();

// page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36';
page.viewportSize = { width: 1680, height: 1050 };

// var url = 'http://184.7.223.152/view/viewer_index.shtml?id=678';
//var url = "https://www.google.com/";
//var url = 'http://phantomjs.org/api/webpage/property/clip-rect.html';
//var url = 'http://stackoverflow.com/questions/16716753/how-to-download-images-from-a-site-with-phantomjs';
var url = 'http://www.insecam.org/en/view/278081/';

page.open(url, function(status) {

  if (status !== 'success') {
      console.error('Unable to load the address!');
      phantom.exit();
  } else {
    console.error('Page loaded.');

    page.includeJs('//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js',function() {

        var images = page.evaluate(function() {
            var images = [];
            function getImgDimensions($i) {
                return {
                    top : $i.offset().top,
                    left : $i.offset().left,
                    // top : $i.top,
                    // left : $.left,
                    width : $i.width(),
                    height : $i.height()
                }
            }
            $('#image0').each(function() {
                var img = getImgDimensions($(this));
                images.push(img);
            });

            // page.render();

            return images;
        });

        images.forEach(function(imageObj, index, array){
            page.clipRect = imageObj;
            page.render('images/'+index+'.png')
        });

        phantom.exit();
    });
  }
});
