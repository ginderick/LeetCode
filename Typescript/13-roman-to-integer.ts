function romanToInt(s: string): number {
  const romanNumeralsDict = new Map();

  romanNumeralsDict.set("M", 1000);
  romanNumeralsDict.set("D", 500);
  romanNumeralsDict.set("C", 100);
  romanNumeralsDict.set("L", 50);
  romanNumeralsDict.set("X", 10);
  romanNumeralsDict.set("V", 5);
  romanNumeralsDict.set("I", 1);

  let number = 0;

  for (let i = 0; i < s.length - 1; i++) {
    if (romanNumeralsDict.get(s[i]) < romanNumeralsDict.get(s[i + 1])) {
      number -= romanNumeralsDict.get(s[i]);
    } else {
      number += romanNumeralsDict.get(s[i]);
    }
  }

  return number + romanNumeralsDict.get(s[s.length - 1]);
}

const answer = romanToInt("III");
