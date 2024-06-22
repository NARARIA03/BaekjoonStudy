const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "test.txt");

const input: string[] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

class Node {
  public data: string;
  public next: Node | null;
  constructor(data: string) {
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

  push(data: string) {
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
      return "-1";
    } else {
      if (this.front) {
        const v: string = this.front.data;
        this.front = this.front.next;
        this.size--;
        if (this.isEmpty()) this.rear = null;
        return v;
      }
    }
  }

  isEmpty() {
    return this.size === 0 ? 1 : 0;
  }

  frontNode() {
    if (this.size === 0) {
      return "-1";
    } else {
      if (this.front) {
        return this.front.data;
      }
    }
  }

  rearNode() {
    if (this.size === 0) {
      return "-1";
    } else {
      if (this.rear) {
        return this.rear.data;
      }
    }
  }
}

let queue = new Queue();
let result: (string | number | undefined)[] = [];
const N: number = Number(input[0]);

for (let i: number = 1; i <= N; i++) {
  let cmd: string[] = input[i].split(" ");
  if (cmd.length === 2) {
    if (cmd[0] === "push") {
      queue.push(cmd[1]);
    }
  } else {
    if (cmd[0] === "pop") {
      result.push(queue.pop());
    } else if (cmd[0] === "size") {
      result.push(queue.size);
    } else if (cmd[0] === "empty") {
      result.push(queue.isEmpty());
    } else if (cmd[0] === "front") {
      result.push(queue.frontNode());
    } else if (cmd[0] === "back") {
      result.push(queue.rearNode());
    }
  }
}

console.log(result.join("\n"));

export {};
