const fs = require("fs");
const path = require("path");

const inputPath = "/dev/stdin";
// const inputPath = path.join(__dirname, "test.txt");

const input: number = Number(fs.readFileSync(inputPath).toString().trim());

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
    } else if (this.rear) {
      this.rear.next = new Node(data);
      this.rear = this.rear.next;
      this.size++;
    }
  }

  pop() {
    if (this.size === 0) {
      return -1;
    } else {
      if (this.front) {
        const v: number = this.front.data;
        this.front = this.front.next;
        this.size--;
        return v;
      }
    }
  }
}

const solution = (input: number): void => {
  let queue = new Queue();
  let resAry: number[] = [];

  for (let i = 1; i <= input; i++) {
    queue.push(i);
  }

  while (queue.size !== 0) {
    let card: number | undefined = queue.pop();
    if (card && card !== -1) {
      resAry.push(card);
    }
    card = queue.pop();
    if (card && card !== -1) {
      queue.push(card);
    }
  }
  console.log(resAry.join(" "));
};

solution(input);

export {};
