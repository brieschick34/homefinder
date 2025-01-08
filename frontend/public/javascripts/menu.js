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
  fetch('/generateAmortizationReport', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer abcdxyz',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      principal,
      extraPayment,
      mortgageAmount,
      interestRate
    }),
  })
  // .then((res) => {
  //   return res.json();
  // })
  // .then((data) => console.log(data));
}
