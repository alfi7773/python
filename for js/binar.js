const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let count = 0

function binarySearch(array, item) {
    let start = 0;
    let end = array.length;
    let middle;
    let found = false;
    let position = -1
    while (found === false && start <= end) {
        middle = Math.floor((start + end) / 2);
        if (array[middle] === item) {
            found = true
            position = middle
            return position
        }
    }
}


console.log(binarySearch(array, 8));
console.log('count:', count)
