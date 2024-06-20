const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N: number = Number(input[0]);

const solution = (N: number): void => {
  const printUpper = (N: number): void => {
    let cnt = N - 1;

    for (let i = 1; i <= N; i++) {
      for (let k = 0; k < cnt; k++) {
        process.stdout.write(" ");
      }
      cnt -= 1;
      for (let j = 0; j < i * 2 - 1; j++) {
        process.stdout.write("*");
      }
      console.log();
    }
  };

  const printLower = (N: number): void => {
    let cnt = 1;
    for (let k = N; k > 0; k--) {
      for (let j = 0; j < cnt; j++) {
        process.stdout.write(" ");
      }
      cnt += 1;
      for (let i = 0; i < k * 2 - 1; i++) {
        process.stdout.write("*");
      }
      console.log();
    }
  };

  printUpper(N);
  printLower(N - 1);
};

solution(N);

export {};
