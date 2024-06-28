const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: string[] = fs.readFileSync(inputPath).toString().trim().split("\n");

const money: number = Number(input[0]);
const N: number = Number(input[1]);

// 0: 파란색, 1: 빨간색, 2: 초록색
let bridgeAry: number[] = new Array(100).fill(0);

for (let i = 2; i <= N + 1; i++) {
  let cnt: number = Number(input[i].split(" ")[0]);
  let direct: string = input[i].split(" ")[1];

  if (direct === "L") {
    // cnt가 50이고 L이라면, 인덱스 기준으로는 49에 서있고 48부터 0까지 색이 바뀌는 것
    for (let j = cnt - 2; j >= 0; j--) {
      bridgeAry[j] += 1;
    }
  } else if (direct === "R") {
    // cnt가 50이고 R이라면, 인덱스 기준으로는 49에 서있고 50부터 끝까지 색이 바뀌는 것
    for (let j = cnt; j < bridgeAry.length; j++) {
      bridgeAry[j] += 1;
    }
  }
}

let jooinCnt = 0; // blue
let jipyoCnt = 0; // red
let chungsoCnt = 0; // green

bridgeAry.forEach((e: number) => {
  if (e % 3 === 0) {
    // blue
    jooinCnt++;
  } else if (e % 3 === 1) {
    // red
    jipyoCnt++;
  } else if (e % 3 === 2) {
    // green
    chungsoCnt++;
  }
});

console.log((money * (jooinCnt / 100)).toFixed(2));
console.log((money * (jipyoCnt / 100)).toFixed(2));
console.log((money * (chungsoCnt / 100)).toFixed(2));

export {};
