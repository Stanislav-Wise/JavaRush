const students = [
{ name: 'Alice', grade: 85 },
{ name: 'Bob', grade: 92 },
{ name: 'Charlie', grade: 78 }
];
// .map() - преобразование массива
const studentNames = students.map(student => student.name);
console.log(studentNames); // ['Alice', 'Bob', 'Charlie’]
// .filter() - фильтрация элементов
const excellentStudents = students.filter(student => student.grade >= 90);
console.log(excellentStudents); // [{name: 'Bob', grade: 92}]
// .reduce() - агрегация данных
const totalGrade = students.reduce((sum, student) => sum + student.grade, 0);
console.log(totalGrade); // 255