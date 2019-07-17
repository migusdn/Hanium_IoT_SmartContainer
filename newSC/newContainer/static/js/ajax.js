
function pullajax(){
    $.ajax({
            url : "http://127.0.0.1:8000/api/Container/?format=json",
            dataType: 'json',
            success : function (data) {
                var my_json = JSON.stringify(data)
                var filtered_json = find_in_object(JSON.parse(my_json), {ContainerID: "Container1" });
                document.write(my_json);
                var a = Object.getOwnPropertyNames(filtered_json[0]);
                document.write("<br><br>"+a+"<br><br>");
                document.write("<table id='contable' border='1'>");
                //for(var i; i<=요소개수까지; i++){}
                document.write("<tr>");
                for (var j = 1; j<=(a.length - 1); j++){
                document.write("<th>");
                document.write(a[j]);
                document.write("</th>");
                }
                document.write("</tr>");
                document.write("<tbody></tbody></table>")
                document.write("<br>");
        }
    });
}

function pullajax2(){
    $.ajax({
            url : "http://127.0.0.1:8000/main/containerdetail",
            dataType: 'json',
            success : function (data) {
                var my_json = JSON.stringify(data)
                var filtered_json = find_in_object(JSON.parse(my_json), {ContainerID: "Container1" });
                document.write(my_json);
                document.write("<br>");
                var a = Object.getOwnPropertyNames(filtered_json[0]);
                document.write(a);
        }
    });
}

function pushajax(){

    // var obj = new Array();
    ContainerID =$('#ContainerID').val();
    PortID = $('#PortID').val();
    PortName = $('#PortName').val();
    PortExportDate = $('#PortExportDate').val();

 /*   PortEntryYear = $('#PortEntryYear').val();
    PortEntryCount = $('#PortEntryCount').val();
    PortEntryDate = $('#PortEntryDate').val();
    ShipKoName = $('#ShipKoName').val();
    ShipEngName = $('#ShipEngName').val();
    ShipTypeCode = $('#ShipTypeCode').val();
    ShipTypeName = $('#ShipTypeName').val();
*/
    console.log(ContainerID);
    console.log(PortID);
    console.log("test");

    $.ajax({
		type : 'POST',
		url : 'http://127.0.0.1:8000/main/container_input',
		data : {
                'ContainerID':ContainerID,
                'PortID':PortID,
                'PortName':PortName,
                'PortExportDate':PortExportDate,
 /*               'PortEntryYear': PortEntryYear,
                'PortEntryCount': PortEntryCount,
                'PortImportDate': PortImportDate,
                'ShipKoName': ShipKoName,
                'ShipEngName': ShipEngName,
                'ShipTypeCode': ShipTypeCode,
                'ShipTypeName': ShipTypeName,
                'CheckInOut': null,
                'CheckInOutName': null,
                'LaidupCode': null,
                'LaidupSubCode': null,
                'LaidupPlace': null,
                'CheckDoor': null,
                'TemInfo': null,
                'WetInfo': null,
                'LocaInfo': null,
                'ContainerInfo': null,
                'ContainerloadInfo': null,
                'VibInfo': null,
                'BatteryInfo': null,
                'SecInfo': null,*/
		},
		dataType:'json',
		success: function(){
			alert("SUCESS");
		}
	});
}

function find_in_object(my_object, my_criteria){

  return my_object.filter(function(obj) {
    return Object.keys(my_criteria).every(function(c) {
      return obj[c] == my_criteria[c];
    });
  });
}


/*                console.log("sort전 :"+ my_json);
                  my_json.sort(function(a,b) {
	            return parseFloat(a.ContainerID) - parseFloat(b.ContainerID);
                });
                console.log("sort후"+ my_json);*/