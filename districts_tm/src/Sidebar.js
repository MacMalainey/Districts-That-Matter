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
    
    const show = () => {
        return <button style={{background :'red', borderRadius: 10, color: 'red'}} onClick={ () => sendid(11)}>One</button>,
            <button style={{background:'blue', borderRadius: 10, color:'blue'}} onClick={() => sendid(12)}>One</button>,
            <button style={{background:'yellow', borderRadius: 10, color:'yellow'}} onClick={() => sendid(13)}>One</button>,
            <button style={{background:'green', borderRadius:10, color:'green'}} onClick={() => sendid(14)}>One</button> ,
            <button style={{background:'brown', borderRadius:10, color:'brown'}} onClick={() => sendid(14)}>One</button>, <br></br>,
            <button style={{background:'lightgreen', borderRadius:10, color:'lightgreen'}} onClick={() => sendid(14)}>One</button>, 
            <button style={{background:'#ffa500', borderRadius:10, color:'#ffa500'}} onClick={() => sendid(14)}>One</button>, 
            <button style={{background:'purple', borderRadius:10, color:'purple'}} onClick={() => sendid(14)}>One</button> ,
            <button style={{background:'#008080', borderRadius:10, color:'#008080'}} onClick={() => sendid(14)}>One</button>, 
            <button style={{background:'#133337', borderRadius:10, color:'#133337'}} onClick={() => sendid(14)}>One</button>, <br></br>
    }
  return (
    
        <div className = 'sidebar'>
            {/* <input type='text' placeholder='Update District Number'/> <br/>
            <button type='submit' onClick={submit}>submit</button> <br></br>
            <button type = 'submit' onClick={colordata}>Run Analysis</button> */}



            {<FaPaintBrush className="paint-brush" style={{fontSize:'30px'}} onClick={handlepaint}/>} 
            
            <FaRegHandPaper className="hand-cursor"  onClick={handlecursor}/>
            
            <BsEraser className='eraser' onClick={handleeraser} /> 
            <button style={{marginLeft:'20px', marginBottom:'10px'}}>Save</button> <br></br>
            {colorpalette && (
                <>
            <button style={{background:'#ff1a1a', borderRadius: 10,height:'35px', color:'#ff1a1a'}} onClick={() => sendid(11)}>One</button>
            <button style={{background:'#ff8080', borderRadius: 10, height:'35px', color:'#ff8080'}} onClick={() => sendid(12)}>One</button>
            <button style={{background:'#ffb3b3', borderRadius:10,height:'35px', color:'#ffb3b3'}} onClick={() => sendid(13)}>One</button> 
            <button style={{background:'#ffe6e6', borderRadius:10, height:'35px', color:'#ffe6e6'}} onClick={() => sendid(14)}>One</button>
            <button style={{background :'#ff0000', borderRadius: 10, height:'35px', color: '#ff0000'}} onClick={ () => sendid(15)}>One</button>
            <button style={{background:'#b30000', borderRadius:10, height:'35px', color:'#b30000'}} onClick={() => sendid(16)}>One</button> 
            <button style={{background:'#4d0000', borderRadius:10, height:'35px', color:'#4d0000'}} onClick={() => sendid(17)}>One</button> 
            <button style={{background:'#ff8000', borderRadius:10, height:'35px', color:'#ff8000'}} onClick={() => sendid(18)}>One</button> 
            <button style={{background:'#ffbf00', borderRadius:10, height:'35px', color:'#ffbf00'}} onClick={() => sendid(19)}>One</button> 
            <button style={{background:'#ffff00', borderRadius:10, height:'35px', color:'#ffff00'}} onClick={() => sendid(20)}>One</button> <br></br>
            <button style={{background :'#bfff00', borderRadius: 10, height:'35px', color: '#bfff00'}} onClick={ () => sendid(21)}>One</button>
            <button style={{background:'#80ff00', borderRadius: 10, height:'35px', color:'#80ff00'}} onClick={() => sendid(22)}>One</button>
            <button style={{background:'#40ff00', borderRadius: 10, height:'35px', color:'#40ff00'}} onClick={() => sendid(23)}>One</button>
            <button style={{background:'#00ff00', borderRadius:10, height:'35px', color:'#00ff00'}} onClick={() => sendid(24)}>One</button> 
            <button style={{background:'#00ff40', borderRadius:10, height:'35px', color:'#00ff40'}} onClick={() => sendid(25)}>One</button>
            <button style={{background:'#00ff80	', borderRadius:10, height:'35px', color:'#00ff80	'}} onClick={() => sendid(26)}>One</button> 
            <button style={{background:'#00ffbf', borderRadius:10, height:'35px', color:'#00ffbf'}} onClick={() => sendid(27)}>One</button> 
            <button style={{background:'#00ffff', borderRadius:10, height:'35px', color:'#00ffff'}} onClick={() => sendid(28)}>One</button> 
            <button style={{background:'#00bfff', borderRadius:10, height:'35px', color:'#00bfff'}} onClick={() => sendid(29)}>One</button> 
            <button style={{background:'#0080ff', borderRadius:10, height:'35px', color:'#0080ff'}} onClick={() => sendid(30)}>One</button> <br></br>
            <button style={{background :'#0040ff', borderRadius: 10, height:'35px', color: '#0040ff'}} onClick={ () => sendid(31)}>One</button>
            <button style={{background:'#0000ff', borderRadius: 10, height:'35px', color:'#0000ff'}} onClick={() => sendid(32)}>One</button>
            <button style={{background:'#4000ff', borderRadius: 10, height:'35px', color:'#4000ff'}} onClick={() => sendid(33)}>One</button>
            <button style={{background:'#8000ff', borderRadius:10, height:'35px', color:'#8000ff'}} onClick={() => sendid(34)}>One</button> 
            <button style={{background:'#bf00ff', borderRadius:10, height:'35px', color:'#bf00ff'}} onClick={() => sendid(35)}>One</button> 
            <button style={{background:'#ff00ff', borderRadius:10, height:'35px', color:'#ff00ff'}} onClick={() => sendid(36)}>One</button> 
            <button style={{background:'#ff00bf', borderRadius:10, height:'35px', color:'#ff00bf'}} onClick={() => sendid(37)}>One</button> 
            <button style={{background:'#ff0080', borderRadius:10, height:'35px', color:'#ff0080'}} onClick={() => sendid(38)}>One</button> 
            <button style={{background:'#ff0040', borderRadius:10, height:'35px', color:'#ff0040'}} onClick={() => sendid(39)}>One</button> 
            <button style={{background:'#996680', borderRadius:10, height:'35px', color:'#996680'}} onClick={() => sendid(40)}>One</button> <br></br>
            <button style={{background :'#80c4b7', borderRadius: 10, height:'35px', color: '#80c4b7'}} onClick={ () => sendid(41)}>One</button>
            <button style={{background:'#eeeeee', borderRadius: 10, height:'35px', color:'#eeeeee'}} onClick={() => sendid(42)}>One</button>
            <button style={{background:'#feffba', borderRadius: 10, height:'35px', color:'#feffba'}} onClick={() => sendid(43)}>One</button>
            <button style={{background:'#c90076', borderRadius:10, height:'35px', color:'#c90076'}} onClick={() => sendid(44)}>One</button> 
            <button style={{background:'#073763', borderRadius:10, height:'35px', color:'#073763'}} onClick={() => sendid(45)}>One</button> 
            <button style={{background:'#669999', borderRadius:10, height:'35px', color:'#669999'}} onClick={() => sendid(46)}>One</button> 
            <button style={{background:'#ffa500', borderRadius:10, height:'35px', color:'#ffa500'}} onClick={() => sendid(47)}>One</button> 
            <button style={{background:'#476b6b', borderRadius:10, height:'35px', color:'#476b6b'}} onClick={() => sendid(48)}>One</button> 
            <button style={{background:'#854442', borderRadius:10, height:'35px', color:'#854442'}} onClick={() => sendid(49)}>One</button> 
            <button style={{background:'#f24e70', borderRadius:10, height:'35px', color:'#f24e70'}} onClick={() => sendid(50)}>One</button> <br></br>

                </>
          
            )}
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
