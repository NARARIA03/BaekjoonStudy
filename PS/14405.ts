const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: string[] = fs.readFileSync(inputPath).toString().trim().split("");

let i = 0;
let isAble = true;

while (i < input.length) {
  if (i + 1 < input.length && input[i] === "p" && input[i + 1] === "i") {
    i += 2;
    continue;
  } else if (i + 1 < input.length && input[i] === "k" && input[i + 1] === "a") {
    i += 2;
    continue;
  } else if (i + 2 < input.length && input[i] === "c" && input[i + 1] === "h" && input[i + 2] === "u") {
    i += 3;
    continue;
  } else {
    console.log("NO");
    isAble = false;
    break;
  }
}

if (isAble) {
  console.log("YES");
}

export {};
