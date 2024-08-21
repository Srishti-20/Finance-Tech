// src/components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Optional CSS for styling

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/crud">CRUD Operations</Link></li>
        <li><Link to="/analysis">Data Analysis</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
