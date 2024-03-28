import React from 'react'

function DataLayer() {
  
  const explanation = JSON.parse(localStorage.getItem('COIexp'))
 
    
  return (
    <div>
      <h2>Painted Districts</h2>
      <input type='checkbox'></input>
      <label>Show Painted Districts</label>
      <input type='checkbox'></input>
      <label>Show Demographic Integration</label> <br></br>

      <h2>Boundary Information</h2>
      <input type='checkbox'></input>
      <label>Show County Boundaries</label> <br></br>
      
    

    <select>
    <option value="age">Age</option>
    <option value="income">Income</option>
    </select>
    
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
