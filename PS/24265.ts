const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: number = Number(fs.readFileSync(inputPath).toString().trim());

if (input === 1 || input === 2) {
  console.log(0);
  console.log(2);
} else if (input === 3) {
  console.log(1);
  console.log(2);
} else {
  let cnt = input - 1;
  let result = 0;
  while (cnt > 0) {
    result += cnt;
    cnt--;
  }
  console.log(result);
  console.log(2);
}

export {};
