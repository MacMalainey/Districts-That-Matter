import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';
localStorage.setItem('showonmap', '')
function DataLayer() {
  const[showVO, setshowVO] = useState(false)
  const explanation = JSON.parse(localStorage.getItem('COIexp'))
  const [VOcharact, setVOcharact] = useState(null)
  const [showonmap, setshowonmap] = useState(false)

 //total population: 5032425
 
    
  return (
    <div>
      

      <h2>Demographic Review</h2>
      <label>View Visual Overlay</label>
      <input type='checkbox' value={showVO} onChange={()=>setshowVO(!showVO)}></input> 
      
      {showVO && <p><label>Select a Characteristic</label><select value={VOcharact} onChange={(e) => setVOcharact(e.target.value)}>
        <option value='--'>--</option>
        <option value='age_0_to_4'>age_0_to_4</option>
        
        
      </select>
      {VOcharact && <input type='checkbox' value={showonmap} onChange={() =>setshowonmap(!showonmap) }></input>}
      {console.log(showonmap)}
      {showonmap && localStorage.setItem('showonmap', 1) }
      {!showonmap && localStorage.setItem('showonmap', 0) }
      {console.log(showonmap, localStorage.getItem('showonmap'))}
      
      </p>}
      
      
      
    

   
    
    <p>
      <h4>Explanation</h4>
      <ul>
        {explanation.map((charact,indexvalue)=>(<li key={indexvalue}>
          <p><strong>{charact[0]}</strong> : <em> {charact[1]}</em></p>
        </li>))}
      
      </ul>
      
    </p>
    
      
      
    </div>
  )
}

export default DataLayer
