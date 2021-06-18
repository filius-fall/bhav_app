console.log("FOUND js")

function incFunc(){
    k =parseInt(document.getElementById("val").value);

    document.getElementById("val").value = k+1;

    console.log(typeof k)
    
}

function decFunc(){
    k = parseInt(document.getElementById("val").value);
    if(k > 0){
        document.getElementById("val").value = k-1;
    }
    
}

function startFunc(){
    return data = 0;
}

function lastFunc(){
    return data = -1;
}
