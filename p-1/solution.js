function multiples(start) {
    var sum = 0;
    for (var i = start - 1; i > 0; i--) {
        if (i % 3 === 0 || i % 5 === 0) {
            sum += i;
        }
    }
    return sum;
}
;
console.log(multiples(10), multiples(100), multiples(1000));
