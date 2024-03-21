import React from 'react'

function Evaluation() {
  return (
    <div>
      <p> This is the evaluation layer</p>
      <p> {localStorage.getItem('population')}</p>
    </div>
  )
}

export default Evaluation
