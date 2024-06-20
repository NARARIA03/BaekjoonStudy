const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const ISP = [
  { call: 30, data: 40 },
  { call: 35, data: 30 },
  { call: 40, data: 20 },
];

const solution = (input: string[]): void => {
  input.forEach((e) => {
    let minCost = Number.MAX_VALUE;
    let [call, data] = e.split(" ");
    let callInt = Number(call);
    let dataInt = Number(data);

    if (callInt === 0 && dataInt === 0) {
      return;
    }

    ISP.forEach((e) => {
      let cost = callInt * e.call + dataInt * e.data;
      if (cost < minCost) {
        minCost = cost;
      }
    });
    console.log(minCost);
  });
};

solution(input);

export {};
