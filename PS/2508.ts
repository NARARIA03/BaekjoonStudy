const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: string[] = fs.readFileSync(inputPath).toString().trim().split("\n");

let i = 0;

while (i < input.length) {
  if (input[i] !== "") {
    i++;
    continue;
  } else {
    i++;
    let [height, width] = input[i].split(" ").map((e: string) => Number(e));
    let board: string[][] = [];
    let candyCnt = 0;
    for (let j = 0; j < height; j++) {
      i++;
      let widthList = input[i].split("");
      board.push(widthList);
    }

    for (let j = 0; j < height; j++) {
      for (let k = 0; k < width; k++) {
        if (k + 2 < width && board[j][k] === ">" && board[j][k + 1] === "o" && board[j][k + 2] === "<") {
          candyCnt++;
        } else if (j + 2 < height && board[j][k] === "v" && board[j + 1][k] === "o" && board[j + 2][k] === "^") {
          candyCnt++;
        } else {
          continue;
        }
      }
    }
    console.log(candyCnt);
    continue;
  }
}

export {};
