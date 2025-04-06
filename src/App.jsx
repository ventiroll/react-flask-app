import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios"; 
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import ReactTabs from './ReactTabs';
import Home from './Home';

function App() {
  const [count, setCount] = useState(0);
  const [array, setArray] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/users");
    setArray (response.data.use)
  }

  useEffect (() => {
    fetchAPI()
  }, [1])

  return (
    <BrowserRouter>
    <div className="App">
      <header className="App-header">
        <h1>Little Chef</h1>
      </header>

      <header className="App-body"> 
        <h2>don't just survive, thrive!</h2>
      </header>

      <header className="App-header">
      <h2><Link to="/Home">Home</Link> | <Link to="/ReactTabs">Get Started</Link></h2>
      </header>
      
      <Routes>
        <Route path="/Home" element={<Home />} />
        <Route path="/ReactTabs/*" element={<ReactTabs />} />
        
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
