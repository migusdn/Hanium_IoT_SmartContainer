$(document).ready(function(){
  var modalLayer = $("#modalLayer");
  var modalLink = $(".modalLink");
  var modalCont = $(".modalContent");
  var marginLeft = modalCont.outerWidth()/2;
  var marginTop = modalCont.outerHeight()/2;

  modalLink.click(function(){
    modalLayer.fadeIn("slow");
    modalCont.css({"margin-top" : -marginTop, "margin-left" : -marginLeft});
    $(this).blur();
    $(".modalContent > a").focus();

    return false;
  });

  $(".modalContent").click(function(){
    modalLayer.fadeOut("slow");
    modalLink.focus();
  });

   var modalLayer1 = $("#modalLayer1");
  var modalLink1 = $(".modalLink1");
  var modalCont1 = $(".modalContent1");
  var marginLeft1 = modalCont1.outerWidth()/2;
  var marginTop1 = modalCont1.outerHeight()/2;

  modalLink1.click(function(){
  console.log("ggggggsadasd");
    modalLayer1.fadeIn("slow");
    modalCont1.css({"margin-top" : -marginTop1, "margin-left" : -marginLeft1});
    $(this).blur();
    $(".modalContent1 > a").focus();
    return false;
  });

  $(".modalContent1").click(function(){
    modalLayer1.fadeOut("slow");
    modalLink1.focus();
  });


  //--------------------여기까지 모달
});

  //여기부터 온도장치,냉방장치,개폐장치 z-index
  /*온도장치*/
 function Temp_Module_Off(){
    console.log("0이 위로");
    document.getElementById('UpTemp_On').style.zIndex = 2;
    document.getElementById('Temp_Module_Off').style.zIndex = 1;
    document.getElementById('DoTemp_On').style.zIndex = 3;
    freeze()
}

function DoTemp_Off(){
    console.log("A가 위로");
    document.getElementById('UpTemp_On').style.zIndex = 3;
    document.getElementById('Temp_Module_Off').style.zIndex = 2;
    document.getElementById('DoTemp_On').style.zIndex = 1;
    heat()
}
function UpTemp_Off(){
    console.log("B가 위로");
    document.getElementById('UpTemp_On').style.zIndex = 1;
    document.getElementById('Temp_Module_Off').style.zIndex = 3;
    document.getElementById('DoTemp_On').style.zIndex = 2;

}
/*냉방장치*/
 function Humid_Module_Off(){
    console.log("0이 위로");
    document.getElementById('UpHumid_Off').style.zIndex = 2;
    document.getElementById('Humid_Module_Off').style.zIndex = 1;
    document.getElementById('UpHumid_On').style.zIndex = 3;
    humid()
}

function UpHumid_Off(){
    console.log("A가 위로");
    document.getElementById('UpHumid_Off').style.zIndex = 3;
    document.getElementById('Humid_Module_Off').style.zIndex = 2;
    document.getElementById('UpHumid_On').style.zIndex = 1;
    dehum()
}
function DoHumid_Off(){
    console.log("B가 위로");
    document.getElementById('UpHumid_Off').style.zIndex = 1;
    document.getElementById('Humid_Module_Off').style.zIndex = 3;
    document.getElementById('UpHumid_On').style.zIndex = 2;

}
/*개폐장치*/
/* function doorfunB(){
    console.log("0이 위로");
    document.getElementById('doorMacA').style.zIndex = 2;
    document.getElementById('doorMacB').style.zIndex = 1;
    document.getElementById('doorMac').style.zIndex = 3;
}*/

function doorfun0(){
    console.log("A가 위로");
    document.getElementById('doorMacA').style.zIndex = 3;
    document.getElementById('doorMac').style.zIndex = 1;
}
function doorfunA(){
    console.log("0이 위로");
    document.getElementById('doorMacA').style.zIndex = 1;
    document.getElementById('doorMac').style.zIndex = 3;
}


function checkfun0(){
    console.log("확인해야함");
    document.getElementById('checkMacA').style.zIndex = 3;
    document.getElementById('checkMac').style.zIndex = 1;
}

function checkfunA(){
    console.log("확인했음");
    document.getElementById('checkMac').style.zIndex = 3;
    document.getElementById('checkMacA').style.zIndex = 1;
}





$(document).ready(function detailpull(){
var value = $('#ConID').val();

      $.ajax({
                 url : "http://127.0.0.1:8000/api/Detail/?format=json",
                 dataType : 'json',
                 async: true,
                 success : function(data){
                        var my_json = JSON.stringify(data)
                        var filtered_json = find_in_object(JSON.parse(my_json), {ContainerID: value });
                        console.log(filtered_json);
                        console.log(value);
                        if (filtered_json.length==0){
                            document.write("상세정보가 없음")
                        }else{
                            $('#TemperY').val(filtered_json[0].Temper);
                            $('#HumidY').val(filtered_json[0].Humid);


                            var SetTemper='';
	                        for(var i=(-20); i<=20;i++){
		                        var SetTemper = SetTemper + "<option>"+i+"</option>" ;
	                        }
	                        $("#SetTemperY").append(SetTemper);		//-20~20 옵션추가
	                        $('#SetTemperY').val(filtered_json[0].SetTemper).attr("selected", "selected");//기본값설정


                            var SetHumid='';
	                        for(var i=(-20); i<=20;i++){
		                        var SetHumid = SetHumid + "<option>"+i+"</option>" ;
	                        }
	                        $("#SetHumidY").append(SetHumid);		//-20~20 옵션추가
	                        $('#SetHumidY').val(filtered_json[0].SetHumid).attr("selected", "selected");//기본값설정


                            if(filtered_json[0].Door==1){
                            $('#DoorY').val("열림")
                            }else{
                            $('#DoorY').val("닫힘")
                            }

                            if(filtered_json[0].UpTemper==1){
                            $('#UpTemperY').val("열림")
                            }else{
                            $('#UpTemperY').val("닫힘")
                            }

                            if(filtered_json[0].DoTemper==1){
                            $('#DoTemperY').val("열림")
                            }else{
                            $('#DoTemperY').val("닫힘")
                            }

                            if(filtered_json[0].UpHumid==1){
                            $('#UpHumidY').val("열림")
                            }else{
                            $('#UpHumidY').val("닫힘")
                            }

                            if(filtered_json[0].UpHumid==1){
                            $('#DoHumidY').val("열림")
                            }else{
                            $('#DoHumidY').val("닫힘")
                            }
                        }//else 문
                 }
      });
$(document).ready(function detailpull2(){   //온습도 문제시 alert
var value = $('#ConID').val();

      $.ajax({
                 url : "http://127.0.0.1:8000/api/Detail/?format=json",
                 dataType : 'json',
                 async: true,
                 success : function(data){
                        var my_json = JSON.stringify(data)
                        var filtered_json = find_in_object(JSON.parse(my_json), {ContainerID: value });
                        console.log(filtered_json);
                        console.log(value);
                        if (filtered_json.length==0){
                            document.write("상세정보가 없음");
                        }else{
                           var Hcheck=0;
                           var Tcheck=0;
                           var check=0;

                           var Temper = parseInt(filtered_json[0].Temper);
                           var SetTemper = parseInt(filtered_json[0].SetTemper);
                           var UpTemper = parseInt(filtered_json[0].UpTemper);
	                       var DoTemper = parseInt(filtered_json[0].DoTemper);
                           var Humid = parseInt(filtered_json[0].Humid);
                           var SetHumid = parseInt(filtered_json[0].SetHumid);
                           var UpHumid = parseInt(filtered_json[0].UpHumid);
	                       var DoHumid = parseInt(filtered_json[0].DoHumid);

                            if(UpTemper==1 && DoTemper==1){
                            	alert("온열기와 냉방기가 동시에 켜져있습니다");
	                            Tcheck=1;
                               	}
                            else if((Temper>SetTemper) && UpTemper==1){
                                console.log("온열기문제");
	                            alert("온열기가 켜져있습니다 온도확인좀요");
	                            Tcheck=1;
	                            }
                            else if(((Temper<SetTemper) && DoTemper==1)){
                            	alert("냉방기가 켜져있습니다 온도확인좀요");
                            	Tcheck=1;
                            	}
                            else{Tcheck=0;}


                            if(UpHumid==1 && DoHumid==1){
	                            alert("가아아아습기랑 제에에에습기 둘다켜져있습니다 가아아스키야");
	                            Hcheck=1;
                            }
                            else if((Humid>SetHumid) && UpHumid==1){
	                            alert("가습기가 켜져있습니다 확인좀");
	                            Hcheck=1;
                            }
                            else if((Humid<SetHumid) && DoTemper==1){
	                            alert("제습기가 켜져있습니다 확인좀");
	                            Hcheck=1;
                            }
                            else{Hcheck=0;}

                            if(Tcheck==1 || Hcheck==1){
                                check=1;}
                            else check==0;
                            }

                             //if(check==1){       //check==1 온도나습도에 하나라도 문제있을때 check=1
                             $.ajax({
                              url : "http://127.0.0.1:8000/main/statcheck",
                              type:'POST',
                              data : {
                                'data':value,
                                'StatCheck':check,
                                    },
                               dataType : 'json',
                              success: function(){
		                	    alert("SUCESS");
		                                  }
                                   })
                               // }
                                /*else{
                            $.ajax({
                              url : "http://127.0.0.1:8000/main/statcheck",
                              type:'POST',
                              data : {
                                'data':value,
                                'statcheck':check,
                                    },
                               dataType : 'json',
                              success: function(){
		                	    alert("SUCESS");
		                                  }
                                   })
                                }*/

                    }
                 });



         });


/*      $.ajax({
                 url : "http://127.0.0.1:8000/api/Container/?format=json",
                 dataType : 'json',
                 async: true,
                 success : function(data){
                        var my_json = JSON.stringify(data);
                        var filtered_json = find_in_object(JSON.parse(my_json), {ContainerID: value });

                        if(filtered_json[0].Check=='1'){
                            $('#CheckY').val("해야함")
                        }else{
                            $('#CheckY').val("했음")
                        }
                 }
      });*/


    $('#SetHumidY').on('change', function() {
        console.log(value)
        var humid = $(this).val();

        $.ajax({
                 url : "http://127.0.0.1:8000/detail/humid",
                 dataType : 'json',
                 data : {
                   ConID : value,
                   humid : humid
                 },
                 type : "POST",
                 success : function(){

                    alert("습도가"+humid+" 로 설정되었습니다");

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
        });

                $.ajax({
                 url : target_url+"/detail/humid",
                 dataType : 'json',
                 data : {
                   ConID : value,
                   Temper : humid
                 },
                 type : "POST",
                 success : function(){

                    console.log("습도가"+humid+" 로 설정되었습니다");

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
        });

    });


    $('#SetTemperY').on('change', function() {
        console.log(value)
        var Temper = $(this).val();

                $.ajax({
                 url : "http://127.0.0.1:8000/detail/temper",
                 dataType : 'json',
                 data : {
                   ConID : value,
                   Temper : Temper
                 },
                 type : "POST",
                 success : function(){

                    alert("온도가"+Temper+" 로 설정되었습니다");

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
        });

                $.ajax({
                 url : target_url+"/detail/temper",
                 dataType : 'json',
                 data : {
                   ConID : value,
                   Temper : Temper
                 },
                 type : "POST",
                 success : function(){

                    console.log("온도가"+Temper+" 로 설정되었습니다");

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
        });

    });


});


function find_in_object(my_object, my_criteria){

  return my_object.filter(function(obj) {
    return Object.keys(my_criteria).every(function(c) {
      return obj[c] == my_criteria[c];
    });
  });

}
target_url = "http://192.168.0.x:8000"
function freeze(){
    console.log("freeze");

    var Temper = $('#SetTemperY').val();
    var Humid = $('#SetHumidY').val();

    console.log(Temper);
    console.log(Humid);

    $.ajax({
                 url : target_url+"/status/DoTemp",
                 dataType : 'jsonp',
                 jsonp: "callback",
                 data : {
                    temper : Temper,
                    humid : Humid
                 },
                 success : function(data){
                    console.log("freeze 성공")

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }

    });
}

function heat(){
    console.log("heat")
    $.ajax({
                 url : target_url+"/status/UpTemp",
                 dataType : 'jsonp',
                 jsonp: "callback",
                 success : function(data){
                    console.log("heat 성공")

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
    });
}

function humid(){
    console.log("humid")
    $.ajax({
                 url : target_url+"/status/UpHumid",
                 dataType : 'jsonp',
                 jsonp: "callback",
                 success : function(data){
                    console.log("humid 성공")

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
    });
}

function dehum(){
    console.log("dehum")
    $.ajax({
                 url : target_url+"/status/DoHumid",
                 dataType : 'jsonp',
                 jsonp: "callback",
                 success : function(data){
                    console.log("dehum 성공")

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
    });
}

function door(){
    console.log("야이씨볼롬, door")
    $.ajax({
                 url : target_url+"/status/door",
                 dataType : 'jsonp',
                 jsonp: "callback",
                 success : function(data){
                    alert("성공");
                    console.log(data);

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
    });
}

function check(){
console.log("야이씨볼롬, check")
var value = $('#ConID').val();

    $.ajax({
                 url : "http://127.0.0.1:8000/main/check",
                 dataType : 'json',
                 data : {
                   data : value
                 },
                 type : "POST",
                 success : function(){

                    setTimeout(function(){
                    location.reload();
                    },1000); // 3000밀리초 = 3초
                 }
    });

}












/*
function control(){

    var value = $('#ConID').val();

    var form = document.createElement('form');
	form.setAttribute('method', 'post');
	form.setAttribute('action', 'http://127.0.0.1:8000/control/test');
	document.charset = "utf-8";
	var hiddenField = document.createElement('input');
	hiddenField.setAttribute('type', 'hidden');
	hiddenField.setAttribute('name', 'ConID');
	hiddenField.setAttribute('value', value);
	form.appendChild(hiddenField);

	document.body.appendChild(form);
	form.submit();
}*/