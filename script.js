document.getElementById("predict-form").addEventListener("submit", async (event) => {
  event.preventDefault(); // prevent page reload

  const data = {
    supplier_id: document.getElementById("supplier_id").value,
    transport_mode: document.getElementById("transport_mode").value,
    place: document.getElementById("place").value,
    schedule_date: document.getElementById("schedule_date").value,
  };

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Prediction failed. Try again.");
    }

    const result = await response.json();
    document.getElementById("result").textContent = `Prediction: ${result.prediction} (${result.risk}) — ${result.message}`;
  } catch (error) {
    document.getElementById("result").textContent = "❌ " + error.message;
  }
});
