function createQuiz(){
    var quizName = document.getElementById('quizName').value;
    console.log(quizName);
    var btn = document.getElementById('questionModal').click();
}


document.getElementById('addOption').addEventListener('click' , ()=>{
    var optionNum = document.getElementsByName('option').length + 1;
    console.log(optionNum)
    var newOption = `<div class="col-sm-6 col-md-8 my-1"><input type="text" id="option${optionNum}" name="option" placeholder="enter option here" required
    class="form-control" aria-describedby="passwordHelpBlock"></div>
<div class="col-6 col-md-4"><div class="form-check">
    <input class="form-check-input" type="radio" name="radio" id="optionRadio${optionNum}">
    <label class="form-check-label" for="flexRadioDefault1">
        is correct
    </label>`
    // document.getElementById('optionsList').innerHTML += newOption;
    var list = document.getElementById('optionsList')
    var e = document.createElement('div');
    e.className = 'optionsContainer';
    e.innerHTML = newOption;  
    list.appendChild(e);
})


document.getElementById('deleteOption').addEventListener('click' , ()=>{
    let optionNum = document.getElementsByName('option').length - 1 || 0;
    let optionsList = document.getElementById('optionsList');
    optionsList.removeChild(optionsList.childNodes[optionNum]);
    
})

