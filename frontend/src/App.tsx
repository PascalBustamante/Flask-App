import ListGroup from "./components/ListGroup";
import { Routes, Route } from "react-router-dom";

const App = () =>  {
  return(
  <>
  <nav>
    <ul>
      <li></li>
    </ul>
  </nav>
  <Routes>
    <Route path="/" element={<h1>HI</h1>} />
    <Route />
  </Routes>
  </>
  )
}
export default App;