const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input: string[] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const haveCardLen: number = Number(input[0]);
const haveCard: number[] = input[1].split(" ").map((e: string) => Number(e));
const questionCard: number[] = input[3].split(" ").map((e: string) => Number(e));

let sortedHaveCard: number[] = haveCard.sort((a: number, b: number): number => a - b);

const binarySearch = (haveCard: number[], question: number, haveCardLen: number): number => {
  let l = 0,
    r = haveCardLen - 1;

  while (l <= r) {
    let m = Math.floor((l + r) / 2);

    if (haveCard[m] < question) {
      l = m + 1;
    } else if (haveCard[m] > question) {
      r = m - 1;
    } else if (haveCard[m] === question) {
      return 1;
    }
  }
  return 0;
};

const solution = (haveCard: number[], questionCard: number[], haveCardLen: number): void => {
  let ansList: number[] = [];

  questionCard.forEach((e) => {
    let ans: number = binarySearch(haveCard, e, haveCardLen);
    ansList.push(ans);
  });
  console.log(ansList.join(" "));
};

solution(sortedHaveCard, questionCard, haveCardLen);

export {};
