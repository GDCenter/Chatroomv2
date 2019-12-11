$(function () {
    $(".button1").click(function () {
        var ctype = $(this).html();
        if(ctype ==="好友"){
            $.ajax(
                {
                    url:'http://127.0.0.1:8000/chat_list/Getchat/',
                    datatype: 'json',
                    type:'post',
                     data:{'code':ctype},
                    timeout:2000,//超时
                    success:function(data,status){
					alert(data);
					alert(status);
				},

                }
            )
        }
    })

})
