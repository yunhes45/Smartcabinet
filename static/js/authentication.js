window.addEventListener("DOMContentLoaded", function() {
    document.getElementById("btn").addEventListener("click", function(evt) {

        var name = document.getElementById("name");
        var pass = document.getElementById("pass");

        if (name.value== "" || name.value.length==0) {
            evt.preventDefault();
            alert("이름을 입력해주세요.");
        }
        else if (pass.value == "" || pass.value.length == 0) {
            evt.preventDefault();
            alert('비밀번호를 입력해주세요.');
        }
        else {

        }

        /*			
         if(name.value != exname){
         evt.preventDefault();
         alert("이름. 탈락!");
         }
        
         if(number.value != exnumber){
         evt.preventDefault();
         alert("번호. 탈락!");
         }
        
         if(number.value == "" || number.value.length == 0) {
         evt.preventDefault();
         alert('휴대폰번호를 입력해주세요.');
         } else {
        
         }
         */
    });
})