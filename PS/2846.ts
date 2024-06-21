const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input: string[] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const length: number = Number(input[0]);
const ary: number[] = input[1].split(" ").map((e: string) => {
  return Number(e);
});

const solution = (length: number, ary: number[]): void => {
  let height: number = 0;
  for (let i = 0; i < length; i++) {
    let start: number = ary[i];
    let end: number = ary[i + 1];
    for (let j = i + 1; j < length; j++) {
      let cur: number = ary[j - 1];
      if (cur >= ary[j]) {
        end = ary[j - 1];
        break;
      }
      end = ary[j];
    }
    if (height < end - start) {
      height = end - start;
    }
  }
  console.log(height);
};

solution(length, ary);

export {};
