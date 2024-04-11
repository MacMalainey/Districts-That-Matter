//This component is showing user the gradient overlay for selected categories
//It includes population, income, birthplace, age, visible_minority
//User selecting which category to see gradient overlay for and it gets reflected on the map

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


  // this function handles the category list on the datalayer
  // its part of FR 10
  useEffect(()=>{
    
    const handlegradientstore = async () =>{
      gradientstore = []
      const response = await axios.get('http://127.0.0.1:5000/api/schema')
      const inspectDD = response.data
      if(gradientstore.length != 105) {
        for (const k in inspectDD){

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
 
//return is allowing user to select a category they want the visual overlay for 
// and once the user selects an overlayer, user selects show on map and that gets reflected on the map 
  return (
    <div>
      
      

      <h2>Demographic Review</h2>
      

      


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
      
    

      
      
      </p>}
      
      
    </div>
  )
}

export default DataLayer
