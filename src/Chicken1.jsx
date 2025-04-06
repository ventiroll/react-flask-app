import React from 'react';
import './App.css';
import { Routes, Route, Link } from 'react-router-dom';
import Chicken2 from './Chicken2';
import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios"; 

function Chicken1() {
  const [count, setCount] = useState(0);
  const [array, setArray] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/users");
    console.log(response.data.users); 
    setArray(response.data.users);
  };

  useEffect (() => {
    fetchAPI();
  }, [1]);

    return (
        <div className="App">
      <header className="App-header">
        <h1>- Demonstration -</h1>
      </header>

      <header className="App-body">
        <h2>Cooking Chicken</h2>
        <h2>Step 1: </h2>
        <h2><Link to="Chicken2">-</Link></h2>
        <p>
        {
          array.map((user, index) => (
            <span key={index}>{user}</span> 
          ))
        }
        </p>
      </header>
      <Routes>
                    <Route path="/Chicken2/*" element={<Chicken2 />} />
                    </Routes>
    </div>
    );
}

export default Chicken1;