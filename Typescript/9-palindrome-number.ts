function isPalindrome(x: number): boolean {
  if (x < 0 || (x > 0 && x % 10 === 0)) {
    return false;
  }

  return x == reverseUtil(x);
}

function reverseUtil(x: number): number {
  let result = 0;
  let input_number: number = x;

  while (input_number !== 0) {
    const digit = input_number % 10;
    result = result * 10 + digit;
    input_number = Math.floor(input_number / 10);
  }

  return result;
}
