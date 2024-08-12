import { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import "../styles/Popup.css"; // Ensure this CSS file exists and is correctly styled

declare global {
  interface Window {
    loadPyodide: () => Promise<any>;
  }
}

const Popup = ({ onClose }: { onClose: () => void }) => {
  const [output, setOutput] = useState<string>("");
  const [pyodide, setPyodide] = useState<any>(null); // Store Pyodide instance
  const [codeInput, setCodeInput] = useState<string>(""); // Start with an empty code input

  useEffect(() => {
    const initializePyodide = async () => {
      try {
        const pyodideInstance = await window.loadPyodide(); // Load Pyodide
        setPyodide(pyodideInstance); // Save Pyodide instance
      } catch (error) {
        console.error("Failed to load Pyodide", error);
      }
    };

    initializePyodide();
  }, []); // Empty dependency array ensures this runs once

  const handleRunCode = async () => {
    if (!pyodide) return; // Ensure Pyodide is loaded

    try {
      const result = await pyodide.runPythonAsync(codeInput); // Run the code
      setOutput(result); // Display the result
    } catch (error: unknown) {
      if (error instanceof Error) {
        setOutput(`Error: ${error.message}`); // Handle known errors
      } else {
        setOutput("An unknown error occurred"); // Handle unexpected error types
      }
    }
  };

  return ReactDOM.createPortal(
    <div className="popup-overlay">
      <div className="popup-content">
        <button className="close-button" onClick={onClose}>
          ×
        </button>
        <textarea
          value={codeInput}
          onChange={(e) => setCodeInput(e.target.value)} // Update code input
          placeholder="Enter your Python code here..."
          rows={10}
          cols={50}
        />
        <button onClick={handleRunCode} disabled={!pyodide}>
          Run Code
        </button>
        <pre>{output}</pre>
      </div>
    </div>,
    document.body
  );
};

export default Popup;
