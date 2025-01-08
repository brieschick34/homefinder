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
  const principalVal = document
    .querySelector('#principal').value;

  const extraPaymentVal = document
    .querySelector('#extraPayment').value;
      
  const mortgageAmountVal = document
    .querySelector('#mortgageAmount').value;

  const interestRateVal = document
    .querySelector('#interestRate').value;
      
  console.log("Sending GET Request");

  const path = `/generateAmortizationReport?principal=${principalVal}&extraPayment=${extraPaymentVal}&mortgageAmount=${mortgageAmountVal}&interestRate=${interestRateVal}`

  const response = fetch(path, {
    method: 'GET',
    headers: {
      // Authorization: 'Bearer abcdxyz',
      'Content-Type': 'application/json',
    }
  })

  // console.log(response.json)

  // const myHeaders = new Headers();
  // myHeaders.append("Content-Type", "application/json");
  // myHeaders.append("Access-Control-Allow-Origin", "localhost");
  
  // const raw = JSON.stringify({
  //   "principal": principalVal,
  //   "extraPayment": extraPaymentVal,
  //   "mortgageAmount": mortgageAmountVal,
  //   "interestRate": interestRateVal
  // });
  
  // const requestOptions = {
  //   method: "POST",
  //   mode: "cors",
  //   headers: myHeaders,
  //   body: raw,
  //   redirect: "follow"
  // };
  
  // try {
  //   const response = await fetch("http://localhost:5000/api/v1/generateAmortizationReport", requestOptions);
  //   const result = await response.text();
  //   console.log(result)
  // } catch (error) {
  //   console.error(error);
  // };

  // OLD
  // const myHeaders = new Headers();
  // myHeaders.append("Content-Type", "application/json");
  
  // const raw = JSON.stringify({
  //   "principal": principalVal,
  //   "extraPayment": extraPaymentVal,
  //   "mortgageAmount": mortgageAmountVal,
  //   "interestRate": interestRateVal
  // });
  
  // const requestOptions = {
  //   method: "POST",
  //   headers: myHeaders,
  //   body: raw,
  //   redirect: "follow"
  // };
  
  // fetch("http://localhost:5000/api/v1/generateAmortizationReport", requestOptions)
  //   .then((response) => response.text())
  //   .then((result) => console.log(result))
  //   .catch((error) => console.error(error));

  // fetch('http://localhost:5000/api/v1/generateAmortizationReport', {
  //   method: 'POST',
  //   mode: "no-cors",
  //   headers: {
  //       'Content-Type': 'application/x-www-form-urlencoded'
  //   },
  //   body: JSON.stringify({
  //     "principal": principalVal,
  //     "extraPayment": extraPaymentVal,
  //     "mortgageAmount": mortgageAmountVal,
  //     "interestRate": interestRateVal
  //   }),
  // })
  // .then(r => r.text().then(console.log));
  // .then((res) => {
  //   return res.json();
  // })
  // .then(res => console.log(res))
}
