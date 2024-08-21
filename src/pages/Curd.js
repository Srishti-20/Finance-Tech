import React,{ useState, useEffect } from 'react';
import axios from 'axios';

const CRUDOperations = () => {
    const [data, setData] = useState([]);
    const [newData, setNewData] = useState({});
    const [updateKey, setUpdateKey] = useState('');
    const [updateData, setUpdateData] = useState({});
    const [deleteKey, setDeleteKey] = useState('');

    const API_URL = 'http://localhost:5000/data'; // Update if your API URL is different

    useEffect(() => {
        fetchData();
      }, []);
    
      const fetchData = async () => {
        try {
          const response = await axios.get(API_URL);
          setData(response.data.data);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
    
      const handleAdd = async () => {
        try {
          await axios.post(API_URL, newData);
          fetchData(); // Refresh the data
        } catch (error) {
          console.error('Error adding data:', error);
        }
      };
    
      const handleUpdate = async () => {
        try {
          await axios.put(`${API_URL}/${updateKey}`, updateData);
          fetchData(); // Refresh the data
        } catch (error) {
          console.error('Error updating data:', error);
        }
      };
    
      const handleDelete = async () => {
        try {
          await axios.delete(`${API_URL}/${deleteKey}`);
          fetchData(); // Refresh the data
        } catch (error) {
          console.error('Error deleting data:', error);
        }
      };

  return (
    <div className="crud">
      <h1>CRUD Operations</h1>
      <p>Here, you can create, read, update, and delete financial data entries.</p>
      <div>
        <h2>Fetch Data</h2>
        <button onClick={fetchData}>Fetch Data</button>
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </div>
      
      <div>
        <h2>Add New Data</h2>
        <input
          type="text"
          placeholder="Key"
          onChange={(e) => setNewData({ ...newData, key: e.target.value })}
        />
        <input
          type="text"
          placeholder="Value"
          onChange={(e) => setNewData({ ...newData, value: e.target.value })}
        />
        <button onClick={handleAdd}>Add Data</button>
      </div>

      <div>
        <h2>Update Data</h2>
        <input
          type="text"
          placeholder="Key to Update"
          onChange={(e) => setUpdateKey(e.target.value)}
        />
        <input
          type="text"
          placeholder="New Value"
          onChange={(e) => setUpdateData({ value: e.target.value })}
        />
        <button onClick={handleUpdate}>Update Data</button>
      </div>
      
      <div>
        <h2>Delete Data</h2>
        <input
          type="text"
          placeholder="Key to Delete"
          onChange={(e) => setDeleteKey(e.target.value)}
        />
        <button onClick={handleDelete}>Delete Data</button>
      </div>
    </div>
  );
};

export default CRUDOperations;
