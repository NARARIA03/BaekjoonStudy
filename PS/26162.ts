const fs = require("fs");
const path = require("path");

// const inputPath = "/dev/stdin";
const inputPath = path.join(__dirname, "test.txt");

const input: number[] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((e: string) => Number(e));

const isPrime = (num: number): boolean => {
  if (num === 1) {
    return false;
  } else if (num === 2) {
    return true;
  } else {
    let flag: boolean = true;
    for (let i = 2; i < num; i++) {
      if (num % i === 0) {
        flag = false;
        break;
      }
    }
    return flag;
  }
};

const testCase = input[0];

for (let i = 1; i <= testCase; i++) {
  let num: number = input[i];
  let flag: boolean = false;
  for (let j = 1; j < num; j++) {
    let a: number = j;
    let b: number = num - a;
    if (isPrime(a) && isPrime(b)) {
      console.log("Yes");
      flag = true;
      break;
    }
  }
  if (!flag) {
    console.log("No");
  }
}

export {};
