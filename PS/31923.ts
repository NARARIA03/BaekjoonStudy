const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");
const input: string[] = fs.readFileSync(inputPath).toString().trim().split("\n");

const stick: number = parseInt(input[0].split(" ")[0]);
const ddalgi: number = parseInt(input[0].split(" ")[1]);
const shain: number = parseInt(input[0].split(" ")[2]);

const ddalgiStick: number[] = input[1].split(" ").map((v: string) => parseInt(v));
const shainStick: number[] = input[2].split(" ").map((v: string) => parseInt(v));

let stickPointer: number = 0;
let result: string = "YES";
let resultValue: number[] = [];

while (stickPointer < stick) {
  let flag: boolean = false;
  let insertCnt: number = 0;

  while (insertCnt * ddalgi < 10000 && insertCnt * shain < 10000) {
    if (ddalgiStick[stickPointer] + insertCnt * ddalgi === shainStick[stickPointer] + insertCnt * shain) {
      flag = true;
      break;
    }
    insertCnt++;
  }
  if (!flag) {
    result = "NO";
    break;
  } else {
    resultValue.push(insertCnt);
  }
  stickPointer++;
}

if (result === "YES") {
  console.log("YES");
  console.log(resultValue.join(" "));
} else {
  console.log("NO");
}
export {};
