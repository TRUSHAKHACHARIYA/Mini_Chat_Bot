const form = document.getElementById("chat-form");
const input = document.getElementById("question");
const chatBox = document.getElementById("chat-box");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const userQuestion = input.value.trim();
  if (!userQuestion) return;

  addMessage("user", userQuestion);
  input.value = "";

  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question: userQuestion }),
    });

    const data = await response.json();

    if (!response.ok) {
      // Show backend error message in the chat box
      addMessage("bot", `⚠️ Error: ${data.detail}`);
    } else {
      addMessage("bot", data.answer);
    }
  } catch (error) {
    addMessage("bot", "⚠️ Network error. Is the backend running?");
  }
});

function addMessage(sender, message) {
  const msgDiv = document.createElement("div");
  msgDiv.className = sender === "user" ? "user-message" : "bot-message";
  msgDiv.innerText = message;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
