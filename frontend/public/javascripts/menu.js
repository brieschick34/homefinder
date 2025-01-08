function menuToggle(state) {
  var ele = document.getElementById('menu');
  switch(state) {
    case 'show':
      ele.style.opacity=1;
      ele.style.color='rgb(96, 96, 96)';
      ele.style.visibility='visible';
      ele.style.transition='visibility 0s, opacity 0.3s';
      break;
    case 'hide':
      ele.style.opacity=0;
      ele.style.color='black';
      ele.style.visibility='hidden';
      ele.style.transition='visibility 0.3s, opacity 0.3s'; 
      break;
  }
}

function generateAmortizationReport() {
  console.log("Setting Parameters");
  const principal = document
    .querySelector('#principal').value;

  const extraPayment = document
    .querySelector('#extraPayment').value;
      
  const mortgageAmount = document
    .querySelector('#mortgageAmount').value;

  const interestRate = document
    .querySelector('#interestRate').value;
      
  console.log("Sending POST Request");

  fetch('http://localhost:5000/api/v1/generateAmortizationReport', {
    method: 'POST',
    // mode: "cors",
    headers: {
      'Content-Type': 'text/plain',
    },
    body: JSON.stringify({
      "principal":principal,
      "extraPayment":extraPayment,
      "mortgageAmount":mortgageAmount,
      "interestRate":interestRate
    }),
  })
  .then(r => r.text().then(console.log));
  // .then((res) => {
  //   return res.json();
  // })
  // .then(res => console.log(res))
}
