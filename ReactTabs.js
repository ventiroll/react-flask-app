import React from 'react';
import './App.css';

import { Routes, Route, Link } from 'react-router-dom';
import Demo from './Demo';

function ReactTabs() { 
    return (
        <div className="App">
            <header className="App-header">
            <h1>What would you like to learn today?</h1>
            </header>

            <header className="App-body">
                <h2><Link to="Demo">Cooking Demonstrations</Link></h2>
                <h2>Food Safety</h2>
                <h2>Equipment</h2>
                <h2>Cleaning</h2>
                <h2>Picking Groceries</h2>

            </header>
        <Routes>
        <Route path="/Demo/*" element={<Demo />} />
        </Routes>
        </div>
    );
}

export default ReactTabs;
