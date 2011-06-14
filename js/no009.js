<script type="text/javascript">
/* There exists exactly one Pythagorean triplet for which
// a + b + c = 1000. Find the product abc. */

function first_triplet(total) {
  var c;
  for(var a = 1; a < total - 1; a++) {
    for(var b = 1; b < total - a; b++) {
      c = total - a - b;
      if(a*a + b*b == c*c) {
        return [a, b, c];
      }
    }
  }
}

function main() {
  var triplet = first_triplet(1000),
      result = triplet.reduce(function (a, b) { return a*b; }, 1);
  alert("The answer to Euler Project, question 9 is: " + triplet);
}

main();
</script>