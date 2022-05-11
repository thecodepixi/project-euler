function fibTotal(max) {
  let a = 0
  let b = 1
  let total = 0

  while( a < max ) {
    if( a % 2 == 0 ) {
      total += a
    }
    let hold = a
    a = b
    b = hold + b
  }
  return total
}

console.log( fibTotal(4_000_000) )