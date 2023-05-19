function toggleDiv(radio) {
    var textInput = document.getElementById('textInput');
    if (radio.checked && radio.value==="pay_method_1") {
        textInput.style.display = 'block';
        textInput.classList.add('fade-in');
    } else {
        textInput.classList.remove('fade-in');
        textInput.style.display = 'none';
    }
  }