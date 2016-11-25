function WebSocketTest(){
    if ("WebSocket" in window){
        $('#sse').append('Connecting to server...');
        var ws = new WebSocket("ws://127.0.0.1:9000");

        ws.onopen = function(){
            $('#sse').append('<p>Connection Successful!</p>');
            ws.send("JS Has joined the party!");
            $('button').on('click', function(){
                ws.send($('#text').val())
                $('#text').val('')
            });
            $('#text').keypress(function(e){
                if(e.which == 13){
                    ws.send($('#text').val())
                    $('#text').val('')
                }
            })
        };

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            $('#sse').append("<p>" + received_msg + "</p>");
            updateScroll();
        };

        ws.onclose = function(){
            $('#sse').append('<p>Connection Closed.</p>');
        };

    } else {
        alert("WebSocket NOT supported by your Browser!");
    }
}
WebSocketTest();
