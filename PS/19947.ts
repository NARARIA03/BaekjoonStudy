const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");
const input: number[] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split(" ")
  .map((v: string) => parseInt(v));

const year: number = input[1];
let money: number = input[0];

let list: number[] = [money];

list.push(Math.floor((list[0] * 105) / 100));
list.push(Math.floor((list[1] * 105) / 100));
list.push(Math.max(Math.floor((list[2] * 105) / 100), Math.floor((list[0] * 120) / 100)));
list.push(Math.max(Math.floor((list[3] * 105) / 100), Math.floor((list[1] * 120) / 100)));

while (list.length <= year) {
  list.push(
    Math.max(
      Math.floor((list[list.length - 1] * 105) / 100),
      Math.floor((list[list.length - 3] * 120) / 100),
      Math.floor((list[list.length - 5] * 135) / 100)
    )
  );
}

console.log(list[year]);

export {};
