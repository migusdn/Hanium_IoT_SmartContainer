function send(){

var form = $("form")[0];
var formData = new FormData(form);

$.ajax({
    cache: false,
    url: "http://127.0.0.1:8000/main/container_input",
    processData:false,
    contentType:false,
    type:'POST',
    data : formData,
    success: function(data){
        if(data=="True"){
            alert("현재 사용중인 컨테이너 ID입니다.");
        }else if(data=="Success"){
            alert("저장에 성공하였습니다.")

            setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
        }
    },
    error: function(){
        alert("에러가 발생했습니다.");
    }
});



}