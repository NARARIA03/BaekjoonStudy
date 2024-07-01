const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: number = Number(fs.readFileSync(inputPath).toString().trim());

let counter = 0;

for (let i = input - 1; i >= 1; i--) {
  counter++;
  if (input % i === 0) {
    break;
  }
}
console.log(counter);

export {};
