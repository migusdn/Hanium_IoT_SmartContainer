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
                            document.write(filtered_json)
                            document.write("오브젝트 나오면 성공")
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