const path = require("path");
const fs = require("fs");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: string[] = fs.readFileSync(inputPath).toString().trim().split("\n");

const N: number = parseInt(input[0]);

let cnt: number = 1;

for (let i: number = 1; i < 2 * N + 1; i += 2) {
  const aMap: { [key: string]: number } = {};
  const bMap: { [key: string]: number } = {};
  const a: string[] = input[i].split("");
  const b: string[] = input[i + 1].split("");

  a.forEach((char: string) => {
    if (!aMap[char]) {
      aMap[char] = 1;
    } else {
      aMap[char]++;
    }
  });

  b.forEach((char: string) => {
    if (!bMap[char]) {
      bMap[char] = 1;
    } else {
      bMap[char]++;
    }
  });

  let result: number = 0;

  Object.keys(aMap).forEach((key: string) => {
    if (!Object.keys(bMap).includes(key)) {
      result += aMap[key];
    } else {
      let diff: number = aMap[key] - bMap[key];

      if (diff >= 0) {
        result += diff;
      } else {
        result -= diff;
      }
    }
  });

  Object.keys(bMap).forEach((key: string) => {
    if (!Object.keys(aMap).includes(key)) {
      result += bMap[key];
    }
  });

  console.log(`Case #${cnt}: ${result}`);
  cnt++;
}
export {};
