
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
                        var strn = strn + data[i].Check;
                        var strn = strn + "</td>";
                    }
                    var strn = strn + "</tbody>"
                    $("#sourcetable").append(strn);
                 }
      });

});
$(document).ready(function() {

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

