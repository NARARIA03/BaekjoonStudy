const path = require("path");
const fs = require("fs");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: string[] = fs.readFileSync(inputPath).toString().trim().split("\n");

let [N, M] = input[0].split(" ").map((v) => parseInt(v));

let s: string[] = [];
let testCase: string[] = [];

for (let i = 1; i <= N; i++) {
  s.push(input[i]);
}

for (let i = N + 1; i <= M + N; i++) {
  testCase.push(input[i]);
}

let sMap: { [key: string]: Set<string> } = {};

s.forEach((value) => {
  if (sMap[value[0]]) {
    sMap[value[0]].add(value);
  } else {
    sMap[value[0]] = new Set<string>();
    sMap[value[0]].add(value);
  }
});

let res = 0;

testCase.forEach((value) => {
  if (sMap[value[0]]) {
    if (sMap[value[0]].has(value)) {
      res++;
    }
  }
});

console.log(res);

export {};
