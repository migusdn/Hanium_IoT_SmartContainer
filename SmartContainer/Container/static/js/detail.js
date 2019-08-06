$(document).ready(function detailpull(){
var value = $('#ConID').val();

      $.ajax({
                 url : "http://127.0.0.1:8000/api/Detail/?format=json",
                 dataType : 'json',
                 async: false,
                 success : function(data){
                        var my_json = JSON.stringify(data)
                        var filtered_json = find_in_object(JSON.parse(my_json), {ContainerID: value });

                        if (filtered_json.length==0){
                            document.write("상세정보가 없음")
                        }else{
                            $('#TemperY').val(filtered_json[0].Temper)
                            $('#HumidY').val(filtered_json[0].Humid)
                            $('#SetTemperY').val(filtered_json[0].SetTemper)
                            $('#SetHumidY').val(filtered_json[0].SetHumid)

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
                        }
                 }
      });

});


function find_in_object(my_object, my_criteria){

  return my_object.filter(function(obj) {
    return Object.keys(my_criteria).every(function(c) {
      return obj[c] == my_criteria[c];
    });
  });

}

function freeze(){
    console.log("야이씨볼롬, freeze");
    $.ajax({
                 url : "http://192.168.0.4:8000/status/freeze",
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

function heat(){
    console.log("야이씨볼롬, heat")
    $.ajax({
                 url : "http://192.168.0.4:8000/status/heat",
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

function humid(){
    console.log("야이씨볼롬, humid")
    $.ajax({
                 url : "http://192.168.0.4:8000/status/humid",
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

function dehum(){
    console.log("야이씨볼롬, dehum")
    $.ajax({
                 url : "http://192.168.0.4:8000/status/dehum",
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

function door(){
    console.log("야이씨볼롬, door")
    $.ajax({
                 url : "http://192.168.0.4:8000/status/door",
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
