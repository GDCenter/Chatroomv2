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
function btnAjax(){
            //1.创建xhr
            var xhr = createXhr();
            //2.创建请求
            xhr.open("post","http://127.0.0.1:8000/chat_list/Getchat/",true);
            //3.设置回调函数
            xhr.onreadystatechange = function(){
                if(xhr.readyState==4 && xhr.status==200){
                    //接收响应数据 - xhr.responseText
                    document.getElementById("show").innerHTML = xhr.responseText;
                }
            }
            //4.发送请求
            xhr.send(null);
        }

        function btnUname(){
            //1.创建xhr
            var xhr = createXhr();
            //2.创建请求
            var uname = document.getElementById("uname").value;
            var url = "/02-server-param?uname="+uname;
            xhr.open("get",url,true);
            //3.设置回调函数(业务处理)
            xhr.onreadystatechange = function(){
                if(xhr.readyState==4 && xhr.status==200){
                    var res = xhr.responseText;
                    var show = document.getElementById("show-name");
                    show.innerHTML = res;
                }
            }
            //4.发送请求
            xhr.send(null);
        }