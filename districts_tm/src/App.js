import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import DrawMap from './Map';
import Sidebar from './Sidebar';
import './App.css';
// import DataLayer from './DataLayer';
// import Inspect from './Inspect';
function App() {
    const [id, setid] = useState(0)
  
    const handleid = (newid) => {
       setid(newid)

    }
  return (
      
    <div className='container'>
        <DrawMap/>
        <Sidebar /> 
        
    </div>
    
   
  );
}

export default App;
