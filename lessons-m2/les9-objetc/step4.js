const nowTime = new Date();
console.log(nowTime);

const date1 = new Date(2023, 11, 28);
console.log(date1);

const date2 = new Date('December 28, 2023 10:00:00');
console.log(date2);
console.log(typeof date2);

// const date2 = new Date('Decembr 28, 2023 11:00:00');
// console.log(date2);

console.log(nowTime.getFullYear())

console.log(nowTime.getMonth())

let month = nowTime.getMonth() + 1;
console.log(month)
console.log(typeof month)

console.log(nowTime.getSeconds())

nowTime.setFullYear(2027);
console.log(nowTime);


console.log(nowTime.toDateString())
console.log(nowTime.toTimeString())