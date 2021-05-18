//1. 자바스크립트 타입
// var n1 = 10;
// var n2 = 10.5;
// var s1 = "문자열";
// var b1 = true;

// console.log(n1);
// console.log(n2);
// console.log(s1);
// console.log(b1);

//2. 자바스크립트 오브젝트 타입
// var borad = {
//   id:1,
//   title:"제목1",
//   content:"내용1"  
// };

// console.log(borad);
// console.log(borad.title);

// 3. 자바스크립트 함수
function add() {
    return 10;
}

var result = add();
console.log(result);

// 4. 익명함수
var m = function(){
    return 20;
}

console.log(m());

//5. 화살표 함수
var r =()=> 20;

console.log(r());

//6. 화살표 함수로 변경하기
var f1 = function hello(n1){
    return n1+5;
}

var f2 = (n1)=> n1+5;

var r1 = f2(5);
console.log(r1);

// 7.리스트(배열)
