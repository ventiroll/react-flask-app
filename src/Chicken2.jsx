import React from 'react';
import './App.css';

import { Routes, Route, Link } from 'react-router-dom';
import Chicken3 from './Chicken3';

function Chicken2() {
    return (
        <div className="App">
      <header className="App-header">
        <h1>- Demonstration -</h1>
      </header>

      <header className="App-body">
        <h2>Cooking Chicken</h2>
        <h2>Step 2: -</h2>
        <h2><Link to="Chicken3">-</Link></h2>
        <h2>contents</h2>
      </header>
      <Routes>
                          <Route path="Chicken3" element={<Chicken3 />} />
                          </Routes>
    </div>
    );
}

export default Chicken2;