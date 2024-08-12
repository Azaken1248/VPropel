import { useState } from "react";
import { Light as SyntaxHighlighter } from "react-syntax-highlighter";
import { atomOneDarkReasonable as darkStyle } from "react-syntax-highlighter/dist/esm/styles/hljs";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "../styles/Question.css";

interface QuestionProps {
  question: string;
  question_content: string;
  solution: string;
  explanation: string;
}

const Question = ({
  question,
  question_content,
  solution,
  explanation,
}: QuestionProps) => {
  const [copied, setCopied] = useState<boolean>(false);

  const handleCopyCode = () => {
    navigator.clipboard
      .writeText(solution)
      .then(() => {
        setCopied(true);
        setTimeout(() => setCopied(false), 1000);
      })
      .catch((err) => {
        console.error("Failed to copy code: ", err);
      });
  };

  return (
    <div className="discord-embed">
      <h3>{question}</h3>
      <div>
        <p>{question_content}</p>
      </div>
      <h3>Solution</h3>
      <div className="code-container">
        <button onClick={handleCopyCode} className="run-button">
          <i className={copied ? "fas fa-check" : "fas fa-copy"}></i>
        </button>
        <div className="code-content">
          <SyntaxHighlighter language="python" style={darkStyle}>
            {solution}
          </SyntaxHighlighter>
        </div>
      </div>
      <h3>Explanation</h3>
      <div>
        <p>
          <i>{explanation}</i>
        </p>
      </div>
    </div>
  );
};

export default Question;
