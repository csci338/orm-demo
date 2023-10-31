import { React } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

function main() {
    const root = createRoot(document.getElementById("app"));
    root.render(<App />);
}

// Invoke the function that kicks off React!
main();
