import React from 'react'

function DataLayer() {
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
      
      
    </div>
  )
}

export default DataLayer
