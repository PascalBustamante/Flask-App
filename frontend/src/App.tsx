import ListGroup from "./components/ListGroup";
import { Routes, Route } from "react-router-dom";

function App() {
  return <Routes>
    <Route path="/" element={<h1>HI</h1>} />
    <Route />
  </Routes>
}
export default App;