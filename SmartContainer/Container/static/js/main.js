
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
                        var strn = strn + data[i].PortID;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].PortName;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].PortExportDate;
                        var strn = strn + "</td>";
                        var strn = strn + "<td>";
                        var strn = strn + data[i].PortCheck;
                        var strn = strn + "</td>";
                        var strn = strn + "</tr>";
                    }
                    var strn = strn + "</tbody>"

                    $("#sourcetable").append(strn);
                 }
      });

});

var pickedup;

$(document).ready(function() {
    $( "#sourcetable tbody tr" ).on( "click", function( event ) {

          $("#fillname").val($(this).find("td").eq(0).html());
          var ConID = $("#fillname").val()
          pickedup = $( this );

    var ConID = $("#fillname").val()

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
