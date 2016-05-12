var gulp = require('gulp');
var os = require('os');
var path = require('path')


var EXPRESS_PORT = 4001;
var EXPRESS_ROOT = __dirname;
var LIVERELOAD_PORT = 35729;

var getNetworkInformation = function(){
    console.log("Starting Express on local host: " + EXPRESS_PORT);
    var interfaces = os.networkInterfaces();
    var addresses = [];
    for (var k in interfaces)
    {
        for (var k2 in interfaces[k])
        {
            var address = interfaces[k][k2];
            if (address.family === 'IPv4' && !address.internal)
            {
                addresses.push(address.address);
            }
        }
    }

    return addresses;
}

function startExpress(){
    console.log("Initializing Express");
    var express = require('express');
    var app = express();
    app.use(require('connect-livereload')());
    app.use(express.static(EXPRESS_ROOT));
    app.listen(EXPRESS_PORT);
}

var lr;

function startLiveReload(){
    console.log("Initializing Live-Reload");
    lr = require('tiny-lr')();
    lr.listen(LIVERELOAD_PORT);
}

function notifyLivereload(event){
    var fileName = path.relative(EXPRESS_ROOT, event.path);
    console.log("   Change on " + event.path);
    console.log("   File type: " + path.extname(event.path));


    lr.changed({
        body: {
        files: [fileName]
    }
    })
}

gulp.task('default', function()
{
    console.log("Current network information")
    console.log(getNetworkInformation());
    startExpress();
    startLiveReload();
    gulp.watch(['*.html', 'css/*.css', 'js/**/*', 'img/**/*', 'img/*'], notifyLivereload);
})
