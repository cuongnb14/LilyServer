$(document).ready(function(){

    var lefElement = $("#left-model");
    var rightElement = $("#rigth-model");
    var chatBox = $("#chat-box");

    $("#btn-send").click(function(){
        var msg = $("#message").val();
        $("#message").val("")
        temp = rightElement.clone();
        temp.removeAttr('id');
        temp.css("display", "block");
        temp.find(".chat-message").text(msg);
        console.log(temp.find(".chat-message").text());
        chatBox.append(temp);
        $('#box').animate({
            scrollTop: $('#box').get(0).scrollHeight
        }, 1500);
        $("#loading").css("display", "block");

        $.ajax({
            url: "/v1/lily?q="+encodeURI(msg),
            dataType: "json",
            success: function(data){
                console.log(data);
                temp = lefElement.clone();
                temp.removeAttr('id');
                temp.css("display", "block");
                var msg = "Xin lỗi , tôi chưa được học điều này!"
                if(data.action == "WIKI_SEARCH"){
                    msg = data.params[0];
                }
                temp.find(".chat-message").text(msg);
                $("#loading").css("display", "none");
                chatBox.append(temp);


                $('#box').animate({
                    scrollTop: $('#box').get(0).scrollHeight
                }, 1500);
            }
        });
    });


    $("#message").keyup(function(event){
        if(event.keyCode == 13){
            $("#btn-send").click();
        }
    });


});
