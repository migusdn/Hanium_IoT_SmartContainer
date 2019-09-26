/*
var picker = new Pikaday({
 field: document.getElementById('datepicker'),
 format: 'yyyy-MM-dd',
 toString(date, format) {
   let day = ("0" + date.getDate()).slice(-2);
   let month = ("0" + (date.getMonth() + 1)).slice(-2);
   let year = date.getFullYear();
   return `${year}-${month}-${day}`;
 }
});*/


/*$(document).ready(function() {

  $( "#datepicker" ).datepicker({
    dateFormat: 'yy-mm-dd',
    prevText: '이전 달',
    nextText: '다음 달',
    monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
    monthNamesShort: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
    dayNames: ['일','월','화','수','목','금','토'],
    dayNamesShort: ['일','월','화','수','목','금','토'],
    dayNamesMin: ['일','월','화','수','목','금','토'],
    showMonthAfterYear: true,
    changeMonth: true,
    changeYear: true,
    yearSuffix: '년'

  });
});*/
/*
function date(){
console.log("gggg");
 $( "#datepicker" ).datepicker({
    dateFormat: 'yy-mm-dd',
    prevText: '이전 달',
    nextText: '다음 달',
    monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
    monthNamesShort: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
    dayNames: ['일','월','화','수','목','금','토'],
    dayNamesShort: ['일','월','화','수','목','금','토'],
    dayNamesMin: ['일','월','화','수','목','금','토'],
    showMonthAfterYear: true,
    changeMonth: true,
    changeYear: true,
    yearSuffix: '년'
  });

}
*/




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