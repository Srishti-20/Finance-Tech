import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

const Analysis = () => {
  const [analysis, setAnalysis] = useState({});
  const [charts, setCharts] = useState({});

  const [selectedChart, setSelectedChart] = useState('');
  const [chartImage, setChartImage] = useState('');

  const fetchChart = async (chartType) => {
    try {
      const response = await axios.get(`http://localhost:5000/data/_analysis/chart?type=${chartType}`);
      setChartImage(response.data.chart);
      setSelectedChart(chartType);
    } catch (error) {
      console.error('Error fetching chart:', error);
    }
  }

  useEffect(() => {
    const fetchAnalysis = async () => {
      try {
        const response = await axios.get('http://localhost:5000/data/_analysis');
        setAnalysis(response.data.analysis);
        setCharts(response.data.charts);
      } catch (error) {
        console.error('Error fetching analysis:', error);
      }
    };
    fetchAnalysis();
  }, []);

  const chartData = {
    labels: Object.keys(analysis.avg_amount_by_category || {}),
    datasets: [
      {
        label: 'Average Amount',
        data: Object.values(analysis.avg_amount_by_category || {}),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }
    ]
  };

  return (
    <div>
      <h2>Data Analysis</h2>

<div>
  <h3>Select Analysis Criterion:</h3>
  <ul>
    <li>
      <button onClick={() => fetchChart('fraud_age_gender')}>Fraud Count by Age and Gender</button>
    </li>
    <li>
      <button onClick={() => fetchChart('fraud_age_gender_mpl')}>Fraud Count by Age and Gender</button>
    </li>
    <li>
      <button onClick={() => fetchChart('age_distribution')}>Age Distribution</button>
    </li>
    <li>
      <button onClick={() => fetchChart('age_distribution_mpl')}>Age Distribution</button>
    </li>
    <li>
      <button onClick={() => fetchChart('avg_amount_by_category')}>Average Amount by Category</button>
    </li>
    <li>
      <button onClick={() => fetchChart('avg_amount_by_category_mpl')}>Average Amount by Category</button>
    </li>
    <li>
      <button onClick={() => fetchChart('fraud_by_merchant')}>Fraud by Merchant</button>
    </li>
    <li>
      <button onClick={() => fetchChart('fraud_by_merchant_mpl')}>Fraud by Merchant</button>
    </li>
  </ul>
</div>

<div>
  {selectedChart && (
    <div>
      <h3>Selected Chart: {selectedChart.replace('_', ' ').toUpperCase()}</h3>
      {chartImage && <img src={`data:image/png;base64,${chartImage}`} alt={`${selectedChart} Chart`} />}
    </div>
  )}
</div>
      <div>
        {charts.fraud_age_gender && (
          <img src={`data:image/png;base64,${charts.fraud_age_gender}`} alt="Fraud Count by Age and Gender" />
        )}
      </div>

      <div>
        {charts.fraud_age_gender_mpl && (
          <img src={`data:image/png;base64,${charts.fraud_age_gender_mpl}`} alt="Fraud Count by Age and Gender" />
        )}
      </div>

      <div>
        {charts.age_distribution && (
          <img src={`data:image/png;base64,${charts.age_distribution}`} alt="Age Distribution" />
        )}
      </div>

      <div>
        {charts.age_distribution_mpl && (
          <img src={`data:image/png;base64,${charts.age_distribution_mpl}`} alt="Age Distribution" />
        )}
      </div>

      <div>
        {charts.avg_amount_by_category && (
          <img src={`data:image/png;base64,${charts.avg_amount_by_category}`} alt="Average Amount by Category" />
        )}
      </div>

      <div>
        {charts.avg_amount_by_category_mpl && (
          <img src={`data:image/png;base64,${charts.avg_amount_by_category_mpl}`} alt="Average Amount by Category" />
        )}
      </div>

      <div>
        {charts.fraud_by_merchant && (
          <img src={`data:image/png;base64,${charts.fraud_by_merchant}`} alt="Fraud by Merchant" />
        )}
      </div>

      <div>
        {charts.fraud_by_merchant_mpl && (
          <img src={`data:image/png;base64,${charts.fraud_by_merchant_mpl}`} alt="Fraud by Merchant" />
        )}
      </div>

      <div>
        <Bar data={chartData} />
      </div>
    </div>
  );
};

export default Analysis;
