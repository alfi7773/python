const array = [1, 4, 6, 7, 8, 9, 15, 2, 3, 5]
let count = 0
function linearSearch(array, item) {
    for (let i = 0; i < array.length; i++) {
        count += 1
        if (array[i] === item) {
            return i;
        }
    }
    return null
}

console.log(linearSearch(array, 5))
console.log('count:', count)

