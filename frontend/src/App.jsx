import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [context, setContext] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    setContext("");

    try {
      const res = await axios.post("/ask", { question });



      setAnswer(res.data.answer);
      setContext(res.data.context);
    } catch (err) {
      console.error(err);
      setAnswer("Error fetching answer. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>RAG Assistant</h1>
      <div>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me something..."
        />
        <button onClick={handleAsk} disabled={loading}>
          {loading ? "Loading..." : "Ask"}
        </button>
      </div>

      {answer && (
        <div className="response">
          <h3>Answer:</h3>
          <p>{answer}</p>
          <h4>Context:</h4>
          <pre>{context}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
