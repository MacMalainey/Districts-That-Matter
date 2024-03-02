import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import DrawMap from './Map';
import Sidebar from './Sidebar';
import './App.css';
function App() {
  
  const center = [43.6532, -79.3832];
  // const [coord, setcoord] = useState([])
  // useEffect(() => {
  //   const geoJ = JSON.parse()
  // })
  // const [coord, setCoord] = useState([]);

  //   useEffect(() => {
      
  //     console.log(data);

  //   }, []);


  // ;
  return (
      
    <div className='container'>
        <DrawMap/>
        {/* <Sidebar/> */}
    </div>
    
   
  );
}

export default App;
