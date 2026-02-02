import React, { useState } from "react";
import { sendMessage } from "./api";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;

    setLoading(true);
    try {
      const data = await sendMessage(message);
      setReply(data.Message);
    } catch (err) {
      console.error("Frontend error:", err);
      setReply("Error connecting to backend");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h2>Smart Chat</h2>

      <textarea
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={handleSend}>
        {loading ? "Thinking..." : "Send"}
      </button>

      {reply && (
        <div className="response">
          <strong>Response:</strong>
          <p>{reply}</p>
        </div>
      )}
    </div>
  );
}

export default App;