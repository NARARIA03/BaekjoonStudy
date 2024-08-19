const path = require("path");
const fs = require("fs");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: string = fs.readFileSync(inputPath).toString().trim();

const FAN = ":fan:";
const HONGJUN = `:${input}:`;

console.log(`${FAN}${FAN}${FAN}`);
console.log(`${FAN}${HONGJUN}${FAN}`);
console.log(`${FAN}${FAN}${FAN}`);

export {};
