const fs = require("fs");
const path = require("path");
const inputPath = path.join(__dirname, "test.txt");

// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);
const list = input[1].split(" ");
const sizeList = list.map((e: string) => {
  return Number(e);
});
const [t, p] = input[2].split(" ");
const T = Number(t);
const P = Number(p);

const solution = (N: number, sizeList: number[], T: number, P: number) => {
  let requireT = 0;
  sizeList.forEach((e) => {
    let t = Math.floor(e / T);
    let r = e % T;

    if (r === 0) {
      requireT += t;
    } else {
      requireT += t + 1;
    }
  });
  const requireP = Math.floor(N / P);
  const remainderP = N % P;
  console.log(requireT);
  console.log(requireP, remainderP);
};

solution(N, sizeList, T, P);

export {};
