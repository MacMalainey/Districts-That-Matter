import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';
import { click } from '@testing-library/user-event/dist/click';
import { Chart } from 'chart.js';
let inspectdata = []
function Evaluation() {
  // implemented FR 6 and FR7 
  // district number is taken as user input and we recalculate population range per district
  const [totalpop, settotalpop] = useState(null)
  const [districtdemo, setdistrictdemo] = useState(null)
  const totaldistrict = localStorage.getItem('TotalDistricts')
  const [selectTP, setselectTP] = useState(false)
  const [selectDD, setselectDD] = useState(false)
  const [selectpop, setselectpop] = useState(false)
  
  useEffect(()=>{
    const handlepopulation = async () =>{
      const response = await axios.get('http://127.0.0.1:5000/api/units/totals')
      const population = response.data.total_population 
      settotalpop(population)

    }
    handlepopulation();
  }, [totalpop])
  

  useEffect(()=>{
    const handledistrictdemo = async () =>{
      const response = await axios.get('http://127.0.0.1:5000/api/districts/demographics')
      const inspectDD = response.data
      for (const k in inspectDD){
        
        for (const j in inspectDD[k]){
          inspectdata.push([k,j,inspectDD[k][j]])
        }
          // console.log(j, inspectDD[k][j])
          // const val = inspectDD[k]
          // inspectdata.push([k,val])
        
          
          

        
       
        
      }
      
      console.log(inspectdata)
    }
    handledistrictdemo();
   
  }, [])
  
  const handleinspectDD = (pop) => {
    const filteredinspect = inspectdata.filter((arr)=>arr[1]===pop)
    console.log(filteredinspect)
    return <p>Population 
       <input type='checkbox' value={selectpop} onChange={() => setselectpop(!selectpop)}></input>
       {selectpop && <ul>
        
        {filteredinspect.map((charact,indexvalue)=>(<li key={indexvalue}>
          <table>
            <thead>
              <tr>
                District {charact[0]} : {charact[1]} is {charact[2]}
              </tr>
              
            </thead>
          
          </table>
          
        </li>))}
      
      </ul>}
    </p>
    
  }
  
  return (
    <div>
      <label>Show Total Population</label>
      <input type='checkbox' value={selectTP} onChange={() =>setselectTP(!selectTP)}></input>
      {/* <p> {localStorage.getItem('population')}</p> */}
      {selectTP && <p>total population is {totalpop} <br></br>
      updated total population per district is: {Math.floor(totalpop/totaldistrict)}
      </p>}
      <label>Compare District's</label>
      <input type='checkbox' value={selectDD} onChange={() =>setselectDD(!selectDD)}></input>
      {selectDD && <br></br> && handleinspectDD('population')}
      
    </div>
  )
}

export default Evaluation
