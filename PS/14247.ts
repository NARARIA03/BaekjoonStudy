const fs = require("fs");
const path = require("path");

// const inputPath = path.join(__dirname, "test.txt");
const inputPath = "/dev/stdin";

const input: string[] = fs.readFileSync(inputPath).toString().trim().split("\n");

const n = Number(input[0]);

const initTreeHeight: number[] = input[1].split(" ").map((e: string) => Number(e));

const growthTreeHeight: number[] = input[2].split(" ").map((e: string) => Number(e));

const treeData: { height: number; growth: number }[] = [];

for (let i = 0; i < n; i++) {
  treeData.push({
    height: initTreeHeight[i],
    growth: growthTreeHeight[i],
  });
}

let result: number = 0;

treeData.sort((a, b) => a.growth - b.growth);
// console.log(treeData);

for (let i = 0; i < n; i++) {
  result += treeData[i].height + i * treeData[i].growth;
}

console.log(result);

export {};
