import Card from "./components/Card";
import ListGroup from "./components/ListGroup";
import { Routes, Route } from "react-router-dom";
import './App.css'
import RegistrationComponent from "./components/Registration";
import Register from "./containers/Register";

const App = () =>  {
  return (
    <div className="App">
      <Register />
    </div>
  );
}
export default App;