const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");
// const inputPath = "/dev/stdin";

const input = fs.readFileSync(inputPath).toString().trim().split("\n");

// c는 상행선 수, h는 하행선 수
const [c, h]: number[] = input[0].split(" ").map(Number);

let cList: number[] = [];
let hList: number[] = [];

// 하루는 86400초
let timetable: number[] = new Array(86400).fill(1);

for (let i = 1; i <= c; i++) {
  let [h, m, s]: number[] = input[i].split(":").map(Number);
  cList.push(h * 3600 + m * 60 + s);
}

for (let i = c + 1; i <= c + h; i++) {
  let [h, m, s]: number[] = input[i].split(":").map(Number);
  hList.push(h * 3600 + m * 60 + s);
}

// 하루를 초로 쪼개둔 배열에서 상행선 지나간 동안은 0으로 변경시킴
cList.forEach((e: number) => {
  for (let i = e; i < e + 40; i++) {
    timetable[i] = 0;
  }
});

// 하루를 초로 쪼개둔 배열에서 하행선 지나간 동안은 0으로 변경시킴
hList.forEach((e: number) => {
  for (let i = e; i < e + 40; i++) {
    timetable[i] = 0;
  }
});

// 하루를 초로 쪼개둔 배열의 수를 모두 더함 -> 차단기 올라가 있던 시간 초
let sum = timetable.reduce((sum: number, e: number) => sum + e);
console.log(sum);

export {};
