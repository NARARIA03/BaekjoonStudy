const fs = require("fs");
const path = require("path");

// const inputPath = path.join(__dirname, "test.txt");
const inputPath = "/dev/stdin";

const input = fs.readFileSync(inputPath).toString().trim().split("\n");

// n: 트럭 수, w: 다리길이, l: 다리최대하중
const [n, w, l]: number[] = input[0].split(" ").map((e: string): number => Number(e));
// 각 트럭들의 하중
const truckList: number[] = input[1].split(" ").map((e: string): number => Number(e));

class Node {
  public data: number;
  public next: Node | null;
  constructor(data: number) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  public front: Node | null;
  public rear: Node | null;
  public size: number;
  constructor() {
    this.front = null;
    this.rear = null;
    this.size = 0;
  }

  push(data: number) {
    if (this.size === 0) {
      this.front = new Node(data);
      this.rear = this.front;
      this.size++;
    } else {
      if (this.rear) {
        this.rear.next = new Node(data);
        this.rear = this.rear.next;
        this.size++;
      }
    }
  }

  pop() {
    if (this.size === 0) {
      return undefined;
    } else {
      if (this.front) {
        let v: number = this.front.data;
        this.front = this.front.next;
        this.size--;
        return v;
      }
    }
  }

  frontNode() {
    if (this.size === 0) {
      return undefined;
    } else {
      if (this.front) {
        return this.front.data;
      }
    }
  }
}

let queue = new Queue();
truckList.forEach((e) => {
  queue.push(e);
});

let totalWeight: number = 0;
let timeCount: number = 0;
let weightControlAry: { weight: number; time: number }[] = [];
let exitFlag: boolean = false;

// 큐도 비어있고, exitFlag도 true여야만 종료되는 반복문
while (queue.size > 0 || !exitFlag) {
  timeCount++;
  // time이 1 증가했으니, 트럭들을 한 칸씩 옮긴다 (time--)
  weightControlAry.forEach((e) => {
    if (e.time > 0) {
      e.time--;
    }
  });
  // weight의 time이 0인 경우, 다리를 빠져나온 것
  // 다리의 현재 weight에서 빠져나온 트럭의 weight를 빼준 뒤, 다음부터는 빼지 않도록 time을 -1로 변경!
  weightControlAry.forEach((e) => {
    if (e.time === 0) {
      totalWeight -= e.weight;
      e.time = -1;
    }
  });

  // front를 사용해 deque 하면 나올 트럭이 있는지 체크하고
  // 있으면, 이 트럭이 다리에 올라가도 totalWeight가 괜찮은지 확인,
  // 이 트럭이 올라가도 괜찮다면 weightControlAry에 해당 트럭 정보를 등록하고 queue에서 실제로 deque 수행
  let front: number | undefined = queue.frontNode();
  if (front) {
    if (totalWeight + front <= l) {
      totalWeight += front;
      weightControlAry.push({
        weight: front,
        time: w,
      });
      queue.pop();
    }
  }

  // 모든 트럭이 다리를 빠져나왔는지 확인하기 위한 구간
  // weightControlAry의 각 요소들의 time이 -1이라면, 트럭이 빠져나간 것임
  // time이 -1인 요소의 숫자와 weightControlAry의 길이가 같다면 모든 트럭이 빠져나갔다고 간주하고 flag를 true로 변경
  let cnt: number = 0;
  weightControlAry.forEach((e) => {
    if (e.time === -1) {
      cnt++;
    }
  });
  if (cnt === weightControlAry.length) {
    exitFlag = true;
  }
}
console.log(timeCount);

export {};
