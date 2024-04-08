import React, { useContext, useEffect, useState } from 'react'
import axios, { all } from 'axios';
import './DataLayer.css';
import { GradientSelectContext } from './App';

localStorage.setItem('showonmap', '')
localStorage.setItem('showcoionmap', '')
localStorage.setItem('gradientstore', '')
let gradientstore = []
function DataLayer() {
  const[showVO, setshowVO] = useState(false)
  const [VOcharact, setVOcharact] = useState(null)
  const [showonmap, setshowonmap] = useState(false)
  const {data: gradientSelect, callback: setGradientSelect} = useContext(GradientSelectContext)


 //total population: 5032425
   
  //  for (const k in GS){
  //   gradientstore.push(['charact', GS])
  //  }
  useEffect(()=>{
    
    const handlegradientstore = async () =>{
      gradientstore = []
      const response = await axios.get('http://127.0.0.1:5000/api/schema')
      // const response = await axios.get('http://127.0.0.1:5000/api/districts/demographics')
      const inspectDD = response.data
      // console.log("Hi from DL, ", inspectDD)
      if(gradientstore.length != 105) {
        for (const k in inspectDD){
          // console.log(k != "marital_status")
          if(k == "marital_status" || k == "household" || k == "immigrated" ||  k == "generation"){
            
          }
          else {
            for(const j in inspectDD[k]) {
              gradientstore.push([inspectDD[k][j]])
            }
          }
        
        }

      }
      console.log("store", gradientstore)
      
    
      
    }
    handlegradientstore();
    
  }, [gradientstore])
 

  return (
    <div>
      
      

      <h2>Demographic Review</h2>
      

      
      {/* <label>Show COI </label>
      <input type='checkbox' value={showcoionmap} onChange={()=>setshowcoionmap(!showcoionmap)}></input>
      {showcoionmap && localStorage.setItem('showcoionmap', 1)}
      {!showcoionmap && localStorage.setItem('showcoionmap', 0)} */}


      <label>View Visual Overlay</label>
      <input type='checkbox' value={showVO} onChange={()=>setshowVO(!showVO)}></input> 
      
      {showVO && <p><label>Select a Characteristic: </label><select value={VOcharact} onChange={(e) => setVOcharact(e.target.value)}>
      <option value='--'>--</option>
          {gradientstore.map((charact, index) => 
          <option key={index}>{charact[0]}</option>
          )}

      </select>
      {/* {localStorage.setItem('selectedage', VOcharact)} */}
      {VOcharact && <input type='checkbox' value={showonmap} onChange={() => {
        let toShow = VOcharact;
        if (showonmap == true)
          toShow = null;
        setshowonmap(!showonmap)
        setGradientSelect(toShow) }}>
        </input>
        }
      
      {/* {showonmap && localStorage.setItem('showonmap', 1) }
      {!showonmap && localStorage.setItem('showonmap', 0) } */}
      
      
      </p>}
      
      
    </div>
  )
}

export default DataLayer
