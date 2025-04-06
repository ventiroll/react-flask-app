import React from 'react';
import './App.css';

import { Routes, Route, Link } from 'react-router-dom';
import Chicken1 from './Chicken1';

function Demo() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>- Demonstration -</h1>
      </header>

      <header className="App-body">
        <h2>What would you like to cook?</h2>
        <h2>Search</h2>
        <h2>Suggested:</h2>
        <h2><Link to="Chicken1">Chicken</Link></h2>
        <h2>Pasta</h2>
        <h2>Brownies</h2>
      </header>
      <Routes>
              <Route path="/Chicken1/*" element={<Chicken1 />} />
              </Routes>
    </div>
  );
}

export default Demo;