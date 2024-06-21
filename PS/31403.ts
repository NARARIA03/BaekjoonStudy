const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const thinkNumber = (input: string[]): void => {
  const A: number = Number(input[0]);
  const B: number = Number(input[1]);
  const C: number = Number(input[2]);

  console.log(A + B - C);
  return;
};

const thinkString = (input: string[]): void => {
  const A: string = input[0];
  const B: string = input[1];
  const C: number = Number(input[2]);
  const AB: number = Number(A + B);
  console.log(AB - C);
  return;
};

thinkNumber(input);
thinkString(input);

export {};
