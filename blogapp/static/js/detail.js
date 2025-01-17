// 하트 클릭 시 요청 보내기
// post id 보내기

document.querySelector("#like-section").addEventListener("click", () => {
  fetch(``)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
});
