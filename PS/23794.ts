const path = require("path");
const fs = require("fs");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: number = parseInt(fs.readFileSync(inputPath).toString().trim());

const n = input + 2;

for (let i: number = 0; i < n; i++) {
  if (i === 0 || i === n - 1) {
    for (let j: number = 0; j < n; j++) {
      process.stdout.write("@");
    }
  } else {
    for (let j: number = 0; j < n; j++) {
      if (j === 0 || j === n - 1) {
        process.stdout.write("@");
      } else {
        process.stdout.write(" ");
      }
    }
  }
  process.stdout.write("\n");
}

export {};
