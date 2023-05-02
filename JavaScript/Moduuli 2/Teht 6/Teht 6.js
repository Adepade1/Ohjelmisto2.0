function rollUntil6(){
    let is6 = false
    while(!is6){
        let newroll = Math.floor(1+ Math.random() * 6)
        console.log(newroll)
        if (newroll === 6){is6 = true}
        let newline = document.createElement("li")
        newline.innerText = newroll.toString()
        document.querySelector("#target").appendChild(newline)
    }
    console.log("Dice rolled.")
}

rollUntil6()