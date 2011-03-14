<script type="text/javascript">
/* Find the difference between the sum of the squares of the
// first one hundred natural numbers and the square of the sum */

function main() {
  var sum_first_100 = 100*(100 + 1)/2,
      sum_first_100_squares = 100*(100 + 1)*(2*100 + 1)/6,
      result = Math.abs(sum_first_100*sum_first_100 - sum_first_100_squares);
  alert("The answer to Euler Project, question 6 is: " + result);
}

main();
</script>