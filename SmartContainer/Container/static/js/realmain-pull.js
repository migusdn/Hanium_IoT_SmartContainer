$(document).ready(function realmainpull(){

     $.ajax({
                 url : "http://127.0.0.1:8000/api/Container/?format=json",
                 dataType : 'json',
                 success : function(data){
                    console.log(data)

                    console.log(data.length)


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
                        var strn = strn + "</tr>"
                        console.log("오우쒯")
                    }
                    var strn = strn + "</tbody>"
                    $("#Container-table").append(strn);
                    console.log(strn);
                 }
      });

});
