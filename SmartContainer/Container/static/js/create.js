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
/*
$(document).ready(function(){
    $("#sendbtn").click(function(){
    var result = txtFieldCheck() == true ? true : false;
        console.log(result);
    });
});
function txtFieldCheck(){ // form안의 모든 text type 조회
    var txtEle = $("#frm input[type=text]");
    for(var i = 0; i < txtEle.length; i ++){
    // console.log($(txtEle[i]).val());
        if("" == $(txtEle[i]).val() || null == $(txtEle[i]).val()){
    var ele_id = $(txtEle[i]).attr("id");
    var label_txt = $("label[for='" + ele_id +"']").text();
    console.log("id : " + ele_id + ", label : " + label_txt);
    showAlert(ele_id, label_txt);
    return true;
        }
    }
}



function showAlert(ele_id, label_txt){
    alert(label_txt + " is null");
    $("#" + ele_id).focus(); // 해당 id에 focus.
}

*/



/*
function required(){
    var empt = new Array();
     empt[1] = document.form.ContainerID.value;
     empt[2] = document.form.SizeType.value;
     empt[3] = document.form.TotalWeight.value;
     empt[4] = document.form.GoodsName.value;
     empt[5] = document.form.GoodsClassify.value;
     empt[6] = document.form.Section.value;
     empt[7] = document.form.LeavePlace.value;
     empt[8] = document.form.CarryingDate.value;

    for(var i=0; i<empt.length; i++){
        if (!empt[i]){
             alert("Please input a Value");
              return false;
       }
       else {
          alert('Code has accepted : you can try another');
          return true;
                }
            }
    }*/

function send(){

            if (    $('input[name=ContainerID]').val()=="" ||
                    $('input[name=SizeType]').val()=="" ||
                    $('input[name=TotalWeight]').val()=="" ||
                    $('input[name=GoodsName]').val()=="" ||
                    $('input[name=GoodsClassify]').val()=="" ||
                    $('input[name=Section]').val()=="" ||
                    $('input[name=LeavePlace]').val()=="" ||
                    $('input[name=CarryingDate]').val()==""){
                    alert('필수 항목을 기입해주세요!');
                    e.preventDefault();
                    return false;
                }

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