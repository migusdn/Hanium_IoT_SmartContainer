$(document).ready(function mappull(){


    $.ajax({
                 url : "http://127.0.0.1:8000/api/Container/?format=json",
                 dataType : 'json',
                 async: false,
                 success : function(data){
                    console.log(data);
                    for(i=0; i<data.length; i++){
                        if(data[i].Section=="0"){
                            console.log("0");
                            var strn =""
                            strn = strn + data[i].ContainerID
                            $("#select-bar0").append(strn);
                        }else if(data[i].Section=="A"){
                            var strn =""
                            strn = strn + data[i].ContainerID
                            console.log("A");
                            $("#select-barA").append(strn);
                        }else{
                            console.log("B");
                            var strn =""
                            strn = strn + data[i].ContainerID
                            $("#select-barB").append(strn);
                        }
                    }
                 }

    });

});

function fun0(){
    console.log("0이 위로");
    document.getElementById('select-barA').style.zindex = -1;
    document.getElementById('select-barB').style.zindex = -1;
    document.getElementById('select-bar0').style.zindex = 1;
}

function funA(){
    console.log("A이 위로");
    document.getElementById('select-bar0').style.zindex = -1;
    document.getElementById('select-barB').style.zindex = -1;
    document.getElementById('select-barA').style.zindex = 1;
}

function funB(){
    console.log("B이 위로");
    document.getElementById('select-bar0').style.zindex = -1;
    document.getElementById('select-barA').style.zindex = -1;
    document.getElementById('select-barB').style.zindex = 1;
}