import {React, useState} from 'react'
import './Sidebar.css'; // Import your CSS file
import {SketchPicker} from 'react-color'

function Sidebar() {
    const [selectpaint, setselectpaint] = useState(false)
    const [selectcursor, setselectcursor] = useState(false)

    const submit = () => {
        
        window.location.reload();
    }

    const handlepaint = () =>{
        setselectpaint(true)
        console.log("paint is selected")
    }
    const handlecursor = ()=>{
        setselectpaint(false)
        setselectcursor(true)
    }
    const colordata = () =>{
        alert('data sent')
    }
  return (
    
        <div className = 'sidebar'>
            
            <FaPaintBrush onClick={handlepaint} color="grey"/>
            <FaHandPaper onClick={handlecursor} color = "grey"/> <br></br>
            <SketchPicker/>
            <input type='text' placeholder='Update District Number'/> <br/>
            <button type='submit' onClick={submit}>submit</button> <br></br>
            <button type = 'submit' onClick={colordata}>Run Analysis</button>

            <p>Data Layer</p>
            <input type='checkbox'></input>
            <label>Show painted region</label>
        </div>
       
  )
}

export default Sidebar
