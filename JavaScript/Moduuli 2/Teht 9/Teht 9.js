function even(array){
    return array.filter(num => (num % 2 === 0))
}
function randomizer(){
    let array = []
    for (let i = 0; i<10; i++){
        let number = Math.floor(Math.random() * 10)
        array.push(number)
    }
    return array
}
function getEvenRandomArray(){
    const original = randomizer()
    const evened = even(original)
    const arrays = [original, evened]
    console.log(`Original array: ${arrays[0]}`)
    console.log(`Altered array: ${arrays[1]}`)
}
getEvenRandomArray()