import React from 'react';
import ReactDOM from 'react-dom/client';
//import 'bootstrap/dist/css/bootstrap.css';
import App from './App';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Login from './containers/Login';
import Register from './containers/Register';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route index element={<App/>}/>
        <Route path='login' element={<Login/>} />
        <Route path='register' element={<Register/>} />
      </Routes>
    </Router>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
