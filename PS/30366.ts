const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N: number = Number(input[0].split(" ")[0]);
const M: number = Number(input[0].split(" ")[1]);
const groupList: number[] = input[1].split(" ").map((e: string): number => {
  return Number(e);
});

const solution = (N: number, M: number, groupList: number[]): void => {
  let cnt: number = 0;
  let seq = 0;
  groupList.forEach((e) => {
    if (e + cnt <= M) {
      console.log(seq);
      cnt += e;
    } else {
      cnt = e;
      seq += 1;
      console.log(seq);
    }
  });
};

solution(N, M, groupList);

export {};
