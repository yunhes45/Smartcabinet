window.onload = function(){
    document.getElementById("cool").onclick = function(){
        alert("확인을 누르시면 15초 동안 냉장고 잠금이 해제됩니다");
        location.replace("/");
    }

    document.getElementById("warm").onclick = function(){
        alert("확인을 누르시면 15초 동안 온장고 잠금이 해제됩니다");
        location.replace("/");
    }
    document.getElementById("cooltext").onclick = function(){
        alert("확인을 누르시면 15초 동안 냉장고 잠금이 해제됩니다");
        location.replace("/");
    }

    document.getElementById("warmtext").onclick = function(){
        alert("확인을 누르시면 15초 동안 온장고 잠금이 해제됩니다");
        location.replace("/");
    }
}