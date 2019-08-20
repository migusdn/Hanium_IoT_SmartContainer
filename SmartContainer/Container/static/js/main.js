
$(document).ready(function realmainpull(){

     $.ajax({
                 url : "http://127.0.0.1:8000/api/Container/?format=json",
                 dataType : 'json',
                 async: false,
                 success : function(data){
                    var strn='';
                    var strn = strn+"<tbody>";
                    for(i=0; i<data.length; i++){
                        var strn = strn + "<tr>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].ContainerID;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].SizeType;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].TotalWeight;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].GoodsName;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].GoodsClassify;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].Section;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].LeavePlace;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].CarryingDate;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + "■";
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        if(data[i].Check=='0'){
                            strn = strn + "했음";
                        }else {
                            strn = strn + "해야함";
                        }
                        var strn = strn + "</td>";
                    }
                    var strn = strn + "</tbody>"
                    $("#sourcetable").append(strn);
                 }
      });

});
$(document).ready(function() {              //정렬기능
 $("#sourcetable").tablesorter({
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




var pickedup;

$(document).ready(function() {
    $( "#sourcetable tbody tr" ).on( "click", function( event ) {

          $("#fillname").val($(this).find("td").eq(0).html());
          var ConID = $("#fillname").val();
          pickedup = $( this );

    var ConID = $("#fillname").val();
    console.log(ConID);
    var form = document.createElement('form');
	form.setAttribute('method', 'post');
	form.setAttribute('action', 'http://127.0.0.1:8000/detail/test');
	document.charset = "utf-8";
	var hiddenField = document.createElement('input');
	hiddenField.setAttribute('type', 'hidden');
	hiddenField.setAttribute('name', 'ConID');
	hiddenField.setAttribute('value', ConID);
	form.appendChild(hiddenField);

	document.body.appendChild(form);
	form.submit();

    });
});

$(document).ready(function() {                  //검색기능
  jQuery.expr[':'].icontains = function(a, i, m) {
  return jQuery(a).text().toUpperCase()
      .indexOf(m[3].toUpperCase()) >= 0;
};
 $("#keyword").keyup(function() {
                var k = $(this).val();
                $("#sourcetable tbody tr").hide();
                var temp = $("#sourcetable tbody tr > td:nth-child(n):icontains('" + k + "')");
                $(temp).parent().show();
            })
});

$(document).ready(function() {
    var exTable = document.getElementById("sourcetable");   //table 복사
    var result = new Array();        //result 배열 생성
   if (exTable){            //복사테이블 존재할시
    for(var i=1; i<exTable.rows.length; i++ ){      //데이터행있는만큼 반복문
        if(exTable.rows[i].cells[7]){               //행이있다면
            console.log(exTable.rows[i].cells[7].innerText);    //연습으로콘솔
            result[i] = exTable.rows[i].cells[7].innerText;
            }   //result[1] 부터 배열 넣기
        }
    }

    for( var i=1; i<result.length;i++){
         console.log(result[i]);
    }

    //document.getElementById("result").innerHTML = result;   //id=result에 출력

    function dateDiff(_date1, _date2) { //날짜 계산해주는 함수
    var diffDate_1 = _date1 instanceof Date ? _date1 : new Date(_date1);
    var diffDate_2 = _date2 instanceof Date ? _date2 : new Date(_date2);

     diffDate_1 = new Date(diffDate_1.getFullYear(), diffDate_1.getMonth()+1, diffDate_1.getDate());
     diffDate_2 = new Date(diffDate_2.getFullYear(), diffDate_2.getMonth()+1, diffDate_2.getDate());

    var diff = diffDate_1.getTime() - diffDate_2.getTime();//절대값원하면 Math.abs(diffDate_2.getTime() - diffDate_1.getTime()) 로바꿔야함
      diff = Math.ceil(diff / (1000 * 3600 * 24));

    return diff;
    }

    var result2= new Array();    //result배열과 오늘날짜차이 저장하기위한배열
    for(var i=1; i<result.length;i++){
        result2[i] = dateDiff(result[i],new Date());    //계산해서 배열저장
        console.log("여여기여깅");
        console.log(result2[i]);
        if(result2[i]>=7){                  //차이값이 얼마이상이면
            exTable.rows[i].cells[8].style.backgroundColor='#aabbcc';
                                        //지정 배경색 칠하기
        }
        else if(result2[i]<=3){                  //3일이내면 빨간색
            exTable.rows[i].cells[8].style.backgroundColor='#ff0000';
        }

    }

});
