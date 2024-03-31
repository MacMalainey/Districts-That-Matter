import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';
import { click } from '@testing-library/user-event/dist/click';
import { Chart } from 'chart.js';
import './Evaluation.css';
let inspectdata = []
let TTT= []
function Evaluation() {
  // implemented FR 6 and FR7 
  // district number is taken as user input and we recalculate population range per district
  const [totalpop, settotalpop] = useState(null)
  const [districtdemo, setdistrictdemo] = useState(null)
  const totaldistrict = localStorage.getItem('TotalDistricts')
  const [selectTP, setselectTP] = useState(false)
  const [selectDD, setselectDD] = useState(false)
  const [selectpop, setselectpop] = useState(false)
  const [selectcharact, setselectcharact] = useState(null)

  useEffect(()=>{
    const handletest = async () =>{
      try{
        const response = await axios.get('http://127.0.0.1:5000/api/units/all?include=ages')
        const testage = response.data.features
      
          for (const t in testage){
            const num = testage[t].properties['ages_0_to_4']
            const tot = testage[t].properties['rc_ages']
            const newval = (num/tot) * 100
             console.log(testage[t].id, 'ages_0_to_4',newval)
             TTT.push([testage[t].id, 'ages_0_to_4',newval])
            const newTTT = TTT.filter(chk => chk[2] >= 5)
            console.log("filter", newTTT)
            //  testage.push([testage[t].id, testage[t].properties['age_0_to_4'][0]])
          }
        
        
        // for (const temp in testage[0]){
        //   console.log(testage[0][temp])
        // }
      }
      catch{
        console.log("Error in Data retrival process....")
      }
      
      // console.log(testage)
      // testage.push([testage])
      // settotalpop("this is just a test, Harsh:", testage)
      // console.log("test Harsh", testage)

    }
    handletest();
  }, [])
  
  // useEffect(()=>{
  //   const handlepopulation = async () =>{
  //     const response = await axios.get('http://127.0.0.1:5000/api/units/totals')
  //     const population = response.data.total_population 
  //     settotalpop(population)

  //   }
  //   handlepopulation();
  // }, [totalpop])
  

  useEffect(()=>{
    const handledistrictdemo = async () =>{
      const response = await axios.get('http://127.0.0.1:5000/api/districts/demographics')
      const inspectDD = response.data
      for (const k in inspectDD){
        const temp = inspectDD[k]
        for (const j in temp){
          inspectdata.push([k,j,temp[j]])
          
          
        }
          // console.log(j, inspectDD[k][j])
          // const val = inspectDD[k]
          // inspectdata.push([k,val])

      }
      
      console.log(inspectdata)
    }
    handledistrictdemo();
   inspectdata = []
  }, [])
  
 

  const handleinspectChar = () => {
    const filteredinspectcharact = inspectdata.filter((arr)=>arr[1]===selectcharact)
    return <p> Inspect Characteristics:  
      <select value={selectcharact} onChange={(e)=>setselectcharact(e.target.value)}>
    <option style={{fontStyle:'italic'}}> select...</option>
  
    {inspectdata.map((charact,indexvalue) =>(
      <option key={indexvalue} value={charact[1]}>{charact[1]}</option>
    ))}

    
    </select>
       
       {selectcharact && <ul>
        
        {filteredinspectcharact.map((charact,indexvalue)=>(<li key={indexvalue}>
          <table>
            <thead>
              <tr>
                District {charact[0]} : {charact[1]} has value {charact[2]}
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
      {selectTP && <p>total population is  <br></br>
      
      </p>}
      <label>Compare District's</label>
      <input type='checkbox' value={selectDD} onChange={() =>setselectDD(!selectDD)}></input>
      {selectDD && <br></br> && handleinspectChar()}
      
    </div>
  )
}

export default Evaluation
