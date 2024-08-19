const path = require("path");
const fs = require("fs");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: number[] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split(":")
  .map((v: string) => parseInt(v));

const numPath: { [key: string]: NumPath } = {
  "1": { x: 1, y: 4 },
  "2": { x: 2, y: 4 },
  "3": { x: 3, y: 4 },
  "4": { x: 1, y: 3 },
  "5": { x: 2, y: 3 },
  "6": { x: 3, y: 3 },
  "7": { x: 1, y: 2 },
  "8": { x: 2, y: 2 },
  "9": { x: 3, y: 2 },
  "0": { x: 2, y: 1 },
};

type NumPath = { x: number; y: number };

const getEffort = (a: NumPath, b: NumPath) => {
  return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
};

let minDist = 100000000;
let minA = 100000000;
let minB = 100000000;
let minC = 100000000;
let minD = 100000000;

for (let h: number = input[0]; h < 100; h += 24) {
  for (let m: number = input[1]; m < 100; m += 60) {
    let effort0: number, effort1: number, effort2: number;
    let a = Math.floor(h / 10);
    let b = Math.floor(h % 10);
    let c = Math.floor(m / 10);
    let d = Math.floor(m % 10);

    effort0 = getEffort(numPath[a.toString()], numPath[b.toString()]);
    effort1 = getEffort(numPath[b.toString()], numPath[c.toString()]);
    effort2 = getEffort(numPath[c.toString()], numPath[d.toString()]);

    if (effort0 + effort1 + effort2 < minDist) {
      minDist = effort0 + effort1 + effort2;
      minA = a;
      minB = b;
      minC = c;
      minD = d;
    }
  }
}

console.log(`${minA.toString()}${minB.toString()}:${minC.toString()}${minD.toString()}`);

export {};
