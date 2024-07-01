const fs = require("fs");
const path = require("path");

// const inputPath = path.join(__dirname, "test.txt");
const inputPath = "/dev/stdin";

const input: string[] = fs.readFileSync(inputPath).toString().trim().split("\n");

// N: 현재 낚시터 수, K: 거리확보할 최소 낚시터 수
const [N, K] = input[0].split(" ").map((e: string) => Number(e));
let maxLengthAry: number[] = [];

// 1번째 인덱스부터 첫 줄은 꼭짓점 수, 두번째 줄은 각 점의 좌표 구조
for (let i = 1; i < 2 * N; i += 2) {
  const verticeNum = Number(input[i]);
  const dotAry = input[i + 1].split(" ").map((e: string) => Number(e));
  let maxLength = 0;

  // 0번째 인덱스부터 2개씩 묶어서 x, y 좌표 구조
  for (let j = 0; j < 2 * verticeNum; j += 2) {
    // 피타고라스 정리 활용해서 가장 먼 점까지 거리제곱 구하기
    let length = dotAry[j] * dotAry[j] + dotAry[j + 1] * dotAry[j + 1];
    if (maxLength < length) {
      maxLength = length;
    }
  }
  maxLengthAry.push(maxLength);
}

// 모든 낚시터에 대해, 낚시터를 모두 포용하려면 필요한 거리제곱 값을 오름차순으로 정렬
maxLengthAry.sort((a, b) => a - b);
// K개의 낚시터까지 닿는 낚시줄의 최소 길이 제곱을 소수 둘째자리까지 출력
console.log(maxLengthAry[K - 1].toFixed(2));

export {};
