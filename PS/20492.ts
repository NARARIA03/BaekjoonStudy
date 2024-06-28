const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: number = Number(fs.readFileSync(inputPath).toString().trim());

console.log(input - input * (22 / 100), input - input * (20 / 100) * (22 / 100));

export {};
