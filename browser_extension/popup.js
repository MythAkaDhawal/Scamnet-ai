document.addEventListener('DOMContentLoaded', () => {
  const scanButton = document.getElementById('scanButton');
  const messageInput = document.getElementById('messageInput');
  const resultCard = document.getElementById('resultCard');
  const resultTitle = document.getElementById('resultTitle');
  const resultDesc = document.getElementById('resultDesc');
  const riskScoreValue = document.getElementById('riskScoreValue');
  const riskCircle = document.getElementById('riskCircle');
  const btnText = document.querySelector('.btn-text');
  const loader = document.querySelector('.loader');
  const errorMessage = document.getElementById('errorMessage');

  scanButton.addEventListener('click', async () => {
    const text = messageInput.value.trim();
    if (!text) {
      showError("Please enter a message to scan.");
      return;
    }

    // Reset UI
    errorMessage.classList.add('hidden');
    resultCard.classList.add('hidden');
    resultCard.classList.remove('risk-low', 'risk-medium', 'risk-high');
    riskCircle.setAttribute('stroke-dasharray', '0, 100');

    // Set loading state
    scanButton.disabled = true;
    btnText.textContent = "Scanning...";
    loader.classList.remove('hidden');

    try {
      const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: text })
      });

      if (!response.ok) {
        throw new Error('Server unreachable or returned an error.');
      }

      const data = await response.json();

      // Update UI with response
      updateResultCard(data.scam_probability, data.prediction);
    } catch (error) {
      console.error(error);
      showError("Could not connect to the backend server. Is it running?");
    } finally {
      // Restore button
      scanButton.disabled = false;
      btnText.textContent = "Analyze Risk";
      loader.classList.add('hidden');
    }
  });

  function updateResultCard(probability, prediction) {
    resultCard.classList.remove('hidden');

    // Handle floating point weirdness
    const score = Math.round(probability);
    riskScoreValue.textContent = `${score}%`;

    // Animate SVG ring using stroke-dasharray (score, 100)
    setTimeout(() => {
      riskCircle.setAttribute('stroke-dasharray', `${score}, 100`);
    }, 50);

    // Apply color and logic based on risk score
    if (score < 30) {
      resultCard.classList.add('risk-low');
      resultTitle.textContent = "✅ Safe Message";
      resultDesc.textContent = "This message seems legitimate and low risk 🥰.";
    } else if (score < 70) {
      resultCard.classList.add('risk-medium');
      resultTitle.textContent = "⚠️ Suspicious";
      resultDesc.textContent = "Proceed with caution. 🥷🏻 This could be spam.";
    } else {
      resultCard.classList.add('risk-high');
      resultTitle.textContent = "🚨 Scam Detected";
      resultDesc.textContent = "High probability of being a scam or phishing attempt! 😱 Do not click this links!!!";
    }
  }

  function showError(msg) {
    errorMessage.textContent = msg;
    errorMessage.classList.remove('hidden');
    resultCard.classList.add('hidden');
  }
});
