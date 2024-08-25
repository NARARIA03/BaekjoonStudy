const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");
const input: string[] = fs.readFileSync(inputPath).toString().trim().split("");

let i: number = 0;
let result: string = "";

while (i < input.length) {
  result += input[i];
  if (input[i] === "a" || input[i] === "e" || input[i] === "i" || input[i] === "o" || input[i] === "u") {
    i += 2;
  }
  i += 1;
}

console.log(result);

export {};
