const gulp = require("gulp");

gulp.task("hello", function (cb) {
  console.log("Hello, Gulp!");
  cb(); // Вызываем функцию обратного вызова, чтобы сигнализировать о завершении задачи
});
