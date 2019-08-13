function send(){

var form = $("form")[0];
var formData = new FormData(form);

console.log(formData);
console.log("오잉");
$.ajax({
    cache: false,
    url: "http://127.0.0.1:8000/main/container_input",
    processData:false,
    contentType:false,
    type:'POST',
    data : formData,
    success: function(data){
        console.log("success");
    },
    error: function(xhr, status){
        alert(xhr + ":" +status);
    }
});



}