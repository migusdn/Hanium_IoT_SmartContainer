
$(document).ready(function mappull(){


    $.ajax({
                 url : "http://127.0.0.1:8000/api/Container/?format=json",
                 dataType : 'json',
                 async: false,
                 success : function(data){
                    console.log(data);
                            var strn ="";
                            var strn = strn+"<tbody>";
                        for(i=0; i<data.length; i++){
                          if(data[i].Section=="0"){
                            console.log("0");
                            var strn0 = strn0 + "<tr>";
                            var strn0 = strn0 + "<td>";
                            var strn0 = strn0 + data[i].ContainerID
                            var strn0 = strn0 + "</td>";
                            var strn0 = strn0 + "<td>";
                            var strn0 = strn0 + data[i].Section;
                            var strn0 = strn0 + "</td>";
                            var strn0 = strn0 + "<td>";
                            if(data[i].Check=='0'){
                            strn0 = strn0 + "했음";
                            }else {
                            strn0 = strn0 + "해야함";
                            }
                            var strn0 = strn0 + "</td>";
                            var strn0 = strn0 + "</tr>";
//                            $("#0table").append(strn);

                        }else if(data[i].Section=="A"){
                            console.log("A");
                            var strnA = strnA + "<tr>";
                            var strnA = strnA + "<td>";
                            var strnA = strnA + data[i].ContainerID
                            var strnA = strnA + "</td>";
                            var strnA = strnA + "<td>";
                            var strnA = strnA + data[i].Section;
                            var strnA = strnA + "</td>";
                            var strnA = strnA + "<td>";
                            if(data[i].Check=='0'){
                            strnA = strnA + "했음";
                            }else {
                            strnA = strnA + "해야함";
                            }
                            var strnA = strnA + "</td>";
                            var strnA = strnA + "</tr>";

                        }else{
                            console.log("B");
                            var strnB = strnB + "<tr>";
                            var strnB = strnB + "<td>";
                            var strnB = strnB + data[i].ContainerID
                            var strnB = strnB + "</td>";
                            var strnB = strnB + "<td>";
                            var strnB = strnB + data[i].Section;
                            var strnB = strnB + "</td>";
                            var strnB = strnB + "<td>";
                            if(data[i].Check=='0'){
                             strnB = strnB + "했음";
                            }else {
                            strnB = strnB + "해야함";
                            }
                            var strn = strn + "</td>";
                            var strn = strn + "</tr>";

                        }
                    }
                        $("#0table").append(strn0);
                        $("#Atable").append(strnA);
                        $("#Btable").append(strnB);
                        var strn = strn + "</tbody>"
                        $(".placetable").append(strn);
                 }

    });
     $(".placetable").tablesorter({
    widthFixed : true,
    showProcessing: true,
    headerTemplate : '{content} {icon}',
    widgets: [ 'uitheme', 'zebra', 'filter', 'scroller' ],
    widgetOptions : {
      scroller_height : 300,
      scroller_barWidth : 18,
      scroller_upAfterSort: true,
      scroller_jumpToHeader: true,
      scroller_idPrefix : 's_'
    }
  });
});

function fun0(){
    console.log("0이 위로");
    document.getElementById('select-barA').style.zIndex = 2;
    document.getElementById('select-barB').style.zIndex = 1;
    document.getElementById('select-bar0').style.zIndex = 3;
}

function funA(){
    console.log("A이 위로");
    document.getElementById('select-bar0').style.zIndex = 2;
    document.getElementById('select-barB').style.zIndex = 1;
    document.getElementById('select-barA').style.zIndex = 3;
}

function funB(){
    console.log("B이 위로");
    document.getElementById('select-bar0').style.zIndex = 2;
    document.getElementById('select-barA').style.zIndex = 1;
    document.getElementById('select-barB').style.zIndex = 3;
}