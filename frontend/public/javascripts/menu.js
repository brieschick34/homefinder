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

async function generateAmortizationReport() {
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

  const path = `generateAmortizationReport?principal=${principalVal}&extraPayment=${extraPaymentVal}&mortgageAmount=${mortgageAmountVal}&interestRate=${interestRateVal}`

  console.log("STARTING FETCH")
  response = await fetch(path, {
    method: 'GET',
    // headers: {
    //   // Authorization: 'Bearer abcdxyz',
    //   'Content-Type': 'application/json',
    // }
  })
  .then(res => {                        
    if (!res.ok) {                    
        throw new Error(res.status); 
    }    
    return res.json();                            
  })
  .then(response => {
    const networkData = response.networks;
    this.setState({
      loanData: networkData
    });
  })
  .catch(error => {
    console.log('Error:', error);
  })

  console.log("FETCH ENDED")

  responseJson = await response.json()
  console.log("JSON")
  console.log(responseJson)

  result = await response.text();
  console.log("RESPONSE:");
  console.log(result);
}
