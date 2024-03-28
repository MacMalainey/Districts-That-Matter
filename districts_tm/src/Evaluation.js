import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';
import { click } from '@testing-library/user-event/dist/click';

function Evaluation() {
  // implemented FR 6 and FR7 
  // district number is taken as user input and we recalculate population range per district
  const [totalpop, settotalpop] = useState(null)
  const totaldistrict = localStorage.getItem('TotalDistricts')
  const [selectTP, setselectTP] = useState(false)
  useEffect(()=>{
    const handlepopulation = async () =>{
      const response = await axios.get('http://127.0.0.1:5000/api/units/totals')
      const population = response.data.total_population 
      settotalpop(population)

    }
    handlepopulation();
  }, [totalpop])
  
  
 
  
  return (
    <div>
      <label>Show Total Population</label>
      <input type='checkbox' value={selectTP} onChange={() =>setselectTP(!selectTP)}></input>
      {/* <p> {localStorage.getItem('population')}</p> */}
      {selectTP && <p>total population is {totalpop} <br></br>
      updated total population per district is: {Math.floor(totalpop/totaldistrict)}
      </p>}
      
      
    </div>
  )
}

export default Evaluation
