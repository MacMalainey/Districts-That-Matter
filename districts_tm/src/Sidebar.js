import {React, useState} from 'react'
import './Sidebar.css'; // Import your CSS file
import {SketchPicker} from 'react-color'
import { FaPaintBrush } from "react-icons/fa";
import { FaRegHandPaper } from "react-icons/fa";
import { BsEraser } from "react-icons/bs";

// import { FaPaintBrush } from "react-icons/fa";
// import { FaHandPaper } from "react-icons/fa";
import Inspect from './Inspect';
import DataLayer from './DataLayer';
import Evaluation from './Evaluation';

function Sidebar({DGUID}) {
    
    const [selectpaint, setselectpaint] = useState(false)
    const [selectcursor, setselectcursor] = useState(false)
    const [selecttab, setselecttab] = useState(null)
    const [colorpalette, setcolorpalette] = useState(false)
    const [cursor, setcursor] = useState(false)
    const [eraser, seteraser] = useState(false)
    const[id,setid] = useState(0)
    const submit = () => {
        
        window.location.reload();
    }

    const demodata = () => {
    
    }
    
    const colordata = () =>{
        alert('data sent')
    }
    const handletab = (tab) => {
        setselecttab(tab)
        
  
      }

    const handlepaint = () =>{
        setcolorpalette(true)
        localStorage.setItem('coloractive', 1)
    }
    const handlecursor = () => {
        setcolorpalette(false)
        setcursor(true)
        localStorage.setItem('coloractive', 0)
    }
    const handleeraser = () => {
        seteraser(true)
        setcolorpalette(false)
        setcursor(false)
        localStorage.setItem('coloractive', 0)
    }
    const sendid = (colorid) => {
        
        localStorage.setItem('colorid', colorid)
    }
    
  return (
    
        <div className = 'sidebar'>
            {/* <input type='text' placeholder='Update District Number'/> <br/>
            <button type='submit' onClick={submit}>submit</button> <br></br>
            <button type = 'submit' onClick={colordata}>Run Analysis</button> */}
            <button onClick={ () => sendid(11)}>Red</button>
            <button onClick={() => sendid(12)}>Blue</button>
            <button onClick={() => sendid(13)}>Yellow</button>
            <button onClick={() => sendid(14)}>Green</button>


            {<FaPaintBrush className="paint-brush" style={{fontSize:'30px'}} onClick={handlepaint}/>} 
            
            <FaRegHandPaper className="hand-cursor"  onClick={handlecursor}/> 
            
            <BsEraser className='eraser' onClick={handleeraser} /> <br></br>
            {colorpalette && <SketchPicker/> }
            {cursor && colorpalette}
            {eraser && colorpalette && cursor}
            
            {/* <SketchPicker/> */}
            <button onClick={() => handletab('Inspect')} style={{fontSize:'20px', padding:'10px', width:'167px'}}>Inspect</button>
            <button onClick={() => handletab('DataLayer')} style={{fontSize: '20px', padding: '10px', width:'167px'}}>Data Layer</button>
            <button onClick={() => handletab('Evaluation')} style={{fontSize: '20px', padding: '10px', width:'167px'}}>Evaluation</button>
            {selecttab === 'Inspect' && <Inspect/>}
            {selecttab === 'DataLayer' && <DataLayer/>}
            {selecttab === 'Evaluation' && <Evaluation/>}
            {/* {console.log("Sidebar",DGUID)} */}
            {<p>DGUID is {localStorage.getItem('mapid')}</p>}
            
          

          
        </div>
       
  )
}

export default Sidebar
