import axios from "axios";

const API = axios.create({
  baseURL: "https://chat-bot-3-lf7p.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export const sendMessage = async (message) => {
  try {
    const response = await API.post("/chat", { message });
    return response.data;
  } catch (error) {
    console.error("API error:", error.response || error.message);
    throw error;
  }
};