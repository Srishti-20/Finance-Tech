import React from 'react';
import Analysis from '../components/Analysis'

const DataAnalysis = () => {
  return (
    <div className="analysis">
      <h1>Data Analysis & Charts</h1>
      <p>Analyze the financial data and visualize it using various charts.</p>
      <div className="container">
      <h3>Financial Data Dashboard</h3>
      <Analysis />
    </div>
    </div>
  );
};

export default DataAnalysis;
