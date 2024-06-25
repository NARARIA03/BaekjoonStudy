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

  enque(data: number) {
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

  deque() {
    if (this.size === 0) {
      return undefined;
    } else if (this.front) {
      const data = this.front.data;
      this.front = this.front.next;
      this.size--;
      return data;
    }
  }
}

const fs = require("fs");
const path = require("path");

// const inputPath = path.join(__dirname, "test.txt");
const inputPath = "/dev/stdin";

const input = Number(fs.readFileSync(inputPath).toString().trim());

let queue = new Queue();
for (let i = 1; i <= input; i++) {
  queue.enque(i);
}

let tmp: number | undefined;
let t: number = 1;
while (queue.size > 1) {
  tmp = queue.deque();
  // 큐에서 하나가 deque된 뒤에 순환하는 구조로 코드를 짰기 때문에 finisher 계산 시 1 더해야 함
  if (tmp) {
    let finisher = (t * t * t) % (queue.size + 1);
    if (finisher === 0) {
      finisher = queue.size + 1;
    }
    for (let i = 1; i < finisher; i++) {
      queue.enque(tmp);
      let dequed = queue.deque();
      if (dequed) {
        tmp = dequed;
      }
    }
    t++;
  }
}
if (queue.front) {
  console.log(queue.front.data);
}

export {};
