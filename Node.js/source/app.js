var SerialPort = require('serialport');
var robot = require("robotjs");

var sleep = require('sleep');


var argv = require('optimist')
    .usage('Presentation Driver 1.0 Node.js Edition\nUsage: $0 ')
    .alias({'p': 'port', 'l': 'list', 'h': 'help'})
    .describe('l', 'list of available serial port')
    .describe('p', 'serial port name')
    .describe('h', 'help')
    .argv;


if (argv.l || argv.list) {
    console.log("List of serial port:");

    SerialPort.list(function (err, ports) {
        ports.forEach(function (port) {
            console.log(port.comName + " - " + port.manufacturer);
        });
    });

} else if (argv.p || argv.port) {
    var port = new SerialPort(argv.p,
        {parser: SerialPort.parsers.readline('\n')}
    );

    process.on('SIGINT', function () {
        port.close();
        process.exit();
    });

    port.on('open', function () {
        console.log("Start listen remote command. Open presentation and use remote")
    });

    port.on('error', function (err) {
        console.log('Error: ', err.message);
    });

    port.on('data', function (data) {
        if (data == "forward") {
            console.log("Next Slide");
            tapCall();

            console.log("test");
        } else if (data == "back") {
            console.log("Prev Slide");
            robot.keyTap("left");
        }
    });

    function tapCall(){
        robot.keyTap("right");
        for (i=0;i<1000000000;i++){

            }
    }

    port.on('disconnect', function (data) {
        console.log('Port disconnected');
        process.exit();
    });

} else {
    //Show help
    require('optimist').showHelp(console.info);
}