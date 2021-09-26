// function createQuiz(){
//     var quizName = document.getElementById('quizName').value;
//     console.log(quizName);
//     var btn = document.getElementById('questionModal').click();
// }
const BASE_URL = window.location.origin;

document.getElementById("quizForm").addEventListener("submit", (e) => {
  var formData = new FormData(e.target);
  let body = { name: formData.get("quizName") };
  let csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  document.getElementById("questionModal").click();
  const xhr = new XMLHttpRequest();
  xhr.open("post", `${BASE_URL}/api/quiz/`, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("X-CSRFToken", csrf);
  xhr.onload = () => {
    console.log("in onload");
    if (xhr.status == 201) {
      localStorage.setItem("id", JSON.parse(xhr.responseText).id);
      document.getElementById("questionModal").click();
    } else {
      console.log(JSON.parse(xhr.responseText));
      console.log(xhr.responseText);
    }
  };
  xhr.send(JSON.stringify(body));
});

document.getElementById("addOption").addEventListener("click", () => {
  var optionNum = document.getElementsByName("option").length + 1;

  var newOption = `<div class="col-sm-6 col-md-8 my-1"><input type="text" id="option${optionNum}" name="option" placeholder="enter option here" required
    class="form-control" aria-describedby="passwordHelpBlock"></div>
<div class="col-6 col-md-4"><div class="form-check">
    <input class="form-check-input" type="radio" name="radio" checked id="optionRadio${optionNum}">
    <label class="form-check-label" for="flexRadioDefault1">
        is correct
    </label>`;
  // document.getElementById('optionsList').innerHTML += newOption;
  var list = document.getElementById("optionsList");
  var e = document.createElement("div");
  e.className = "optionsContainer";
  e.innerHTML = newOption;
  list.appendChild(e);
});

document.getElementById("deleteOption").addEventListener("click", () => {
  let optionNum = document.getElementsByName("option").length;
  let optionsList = document.getElementById("optionsList");
  optionsList.removeChild(optionsList.childNodes[optionNum]);
});

document.getElementById("questionForm").addEventListener("submit", (e) => {
  let formData = new FormData(e.target);
  //   console.log(formData.get("question"));
  let body = {};
  body["text"] = formData.get("question");
  body["options"] = [];
  let options = document.getElementsByName("option");
  let radios = document.getElementsByName("radio");
  for (i = 0; i < options.length; i++) {
    body["options"].push({
      text: options[i].value,
      is_correct: radios[i].checked,
    });
  }
  let quiz_id = localStorage.getItem("id");

  let csrf = document.getElementsByName("csrfmiddlewaretoken")[1].value;

  const xhr = new XMLHttpRequest();
  xhr.open("post", `${BASE_URL}/api/quiz/${quiz_id}/question/`, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("X-CSRFToken", csrf);
  xhr.onload = () => {
    if (xhr.status == 201) {
      document.getElementById("questionForm").reset();
    } else {
      let errMsg = "";
      let data = JSON.parse(xhr.responseText).options;
      for (i = 0; i < data.length; i++) {
        errMsg += data[i] + "\n";
      }
      alert(errMsg);
      // alert()
    }
  };
  xhr.send(JSON.stringify(body));
});

function copyQuizLink(uuid){
  navigator.clipboard.writeText(window.location.href.replace('#','') + uuid + '/');
  document.getElementById(`button${uuid}`).innerText = 'Copied !'
  setInterval(()=>{
    document.getElementById(`button${uuid}`).innerText = 'Copy link'
  },3000);
}

document.getElementById('AddQuestionsModal').addEventListener('hidden.bs.modal',()=>{
  window.location.reload()
})