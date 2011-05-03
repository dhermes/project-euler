<script type="text/javascript">
// What is the largest prime factor of the number 600851475143

function first_prime_divisor(n) {
  if (n === 1) {
    return [1, 1];
  }

  var divisor = 2;
  while (n % divisor != 0) {
    divisor += 1;
  }
  return [divisor, n/divisor];
}

function prime_factors(n) {
  if (n === 1) {
    return [];
  }

  var division = first_prime_divisor(n);
  var prime = division[0];
  var quotient = division[1];

  var remaining = quotient;
  while (remaining % prime == 0) {
    remaining = remaining/prime;
  }
  return [prime].concat(prime_factors(remaining));
}

function max_array(arr) {
  var result = arr[0];
  for(var i = 1, val; val = arr[i]; i++) {
    if (val > result) {
      result = val;
    }
  }
  return result;
}

function main() {
  var result = max_array(prime_factors(600851475143));
  alert("The answer to Euler Project, question 3 is: " + result);
}

main();
</script>