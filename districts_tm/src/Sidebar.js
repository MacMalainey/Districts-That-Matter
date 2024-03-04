import React from 'react'
import './Sidebar.css'; // Import your CSS file

function Sidebar() {
    const submit = () => {
        
        window.location.reload();
    }

  return (
    
        <div className = 'sidebar'>
            <input type='text' placeholder='Update District Number'/> <br/>
            <button type='submit' onClick={submit}>submit</button>
        </div>
       
    
  )
}

export default Sidebar
