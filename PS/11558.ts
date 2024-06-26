const fs = require("fs");
const path = require("path");

// const inputPath = path.join(__dirname, "test.txt");
const inputPath = "/dev/stdin";

const input: number[] = fs
  .readFileSync(inputPath)
  .toString()
  .trim()
  .split("\n")
  .map((e: string) => Number(e));

let pointer: number = 1;

for (let i = 0; i < input[0]; i++) {
  let N: number = input[pointer];
  if (N === 1) {
    console.log(1);
    continue;
  }
  let peopleNumber: number = 1;
  let gameBoard: { people: number; next: number }[] = [];

  for (let j = pointer + 1; j < pointer + N + 1; j++) {
    gameBoard.push({ people: peopleNumber, next: input[j] });
    peopleNumber++;
  }

  // make visited ary
  let visited = new Array(N + 1).fill(0);
  let isImpossible: boolean = false;
  let curPeople = 1;
  let cnt = 1;

  while (!isImpossible) {
    visited[curPeople] = 1;
    let people = gameBoard.find((value) => value.people === curPeople);

    if (people) {
      let next = people.next;
      if (visited[next] === 1) {
        isImpossible = true;
      } else if (next === N) {
        console.log(cnt);
        break;
      } else {
        curPeople = next;
        cnt++;
      }
    }
  }
  if (isImpossible) {
    console.log(0);
  }
  pointer += N + 1;
}

export {};
