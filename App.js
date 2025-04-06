
import './App.css';

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import ReactTabs from './ReactTabs';
import Home from './Home';

function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <header className="App-header">
        <h1>name</h1>
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
