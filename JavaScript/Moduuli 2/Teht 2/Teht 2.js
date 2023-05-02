const participants = +prompt("Anna osallistujien lukumäärä:")
let partNames = []

for (let i = 0; i<participants; i++){
  let nimi = prompt(`Anna ${i+1}. osallistujan nimi:`)
  partNames.push(nimi)
}
partNames.sort()

for (let i = 0; i < partNames.length; i++){
    let nimi = document.createElement("li")
    nimi.innerText = partNames[i]
    document.querySelector("#target").appendChild(nimi)
}