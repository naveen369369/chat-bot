import axios from "axios";

const API = axios.create({
  baseURL: "https://chat-bot-2-xdyo.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export const sendMessage = async (message) => {
  const response = await API.post("/chat", { message });
  return response.data;
};
