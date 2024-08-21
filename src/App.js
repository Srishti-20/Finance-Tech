// src/App.js
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import CRUDOperations from './pages/Curd';
import DataAnalysis from './pages/DataAnalysis';
import './App.css';

const App = () => {

  return (
    <div>
      <Router>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/crud" element={<CRUDOperations />} />
          <Route path="/analysis" element={<DataAnalysis />} />
        </Routes>
      </div>
    </Router>
      
    </div>
  );
};

export default App;
