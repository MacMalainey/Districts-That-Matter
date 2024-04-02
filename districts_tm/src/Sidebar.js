import {React, useEffect, useState} from 'react'
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
import axios, { all } from 'axios';

function Sidebar() {
    
    // const [selectpaint, setselectpaint] = useState(false)
    // const [selectcursor, setselectcursor] = useState(false)
    const [selecttab, setselecttab] = useState(null)
    const [colorpalette, setcolorpalette] = useState(false)
    const [cursor, setcursor] = useState(false)
    const [eraser, seteraser] = useState(false)
    const[id,setid] = useState(null)
    const [district, setdistrict] = useState(null)
    const[demodata, setdemodata] = useState(null)
    const temp = localStorage.getItem('mapid')
    const[districtnum, setdistrictnum] = useState(null)
    const [totalpop, settotalpop] = useState(false)
    const[lower, setlower] = useState(null)
    const[upper, setupper] = useState(null)
    // const testdistrict = localStorage.getItem('defineddistricts');
    const submit = () => {
        
        // localStorage.setItem('TotalDistricts', districtnum)
        const num = Math.floor(totalpop/districtnum)
       setlower(Math.floor(num - num * 0.25))
       setupper(Math.floor(num + num * 0.25))
    }
    const colordata = () =>{
        alert('data sent')
    }
    const handletab = (tab) => {
        setselecttab(tab)
        // setid(idvalue)
       
        
      }

    const handlepaint = () =>{
        setcolorpalette(true)
        localStorage.setItem('coloractive', 1)
        localStorage.setItem('cursor', 0)
        localStorage.setItem('eraser', 0)
    }
    const handlecursor = () => {
        setcolorpalette(false)
        setcursor(true)
        localStorage.setItem('coloractive', 0)
        localStorage.setItem('cursor', 1)
        localStorage.setItem('eraser', 0)
    }
    const handleeraser = () => {
        seteraser(true)
        setcolorpalette(false)
        setcursor(false)
        localStorage.setItem('coloractive', 0)
        localStorage.setItem('eraser', 1)
    }
    const sendid = (colorid) => {
        
        localStorage.setItem('colorid', colorid)
    }
    
    // this function will get demographic data for a defined dguid of a map unit
    
    
    // this function is saving the map units for a district
    
          useEffect(()=>{
            setdistrict(localStorage.getItem('defineddistricts'))
            
          },[district])
    const DefinedDistrict = async () => {

        
        
            
            const testar = JSON.parse(localStorage.getItem('defineddistricts'))
            let array = []
            for (let item in testar) {
                array.push([item, testar[item]])
            }
            
            const testing = [["2021S051235191288",40],["2021S051235191287",40],["2021S051235191290",40],["2021S051235191038",40],["2021S051235191104",40],["2021S051235191290",null],["2021S051235190747",47],["2021S051235190433",47]]
            console.log("testing returned array", testar)
            await axios.post('http://127.0.0.1:5000/api/districts/update', array).catch(error =>{console.log(error)});
        
        
            
           
           
          }
            
    useEffect(()=>{
            const handlepopulation = async () =>{
              const response = await axios.get('http://127.0.0.1:5000/api/units/totals')
              const population = response.data.total_population 
              settotalpop(population)
        
            }
            handlepopulation();
          }, [])
   
  return (
    
        <div className = 'sidebar'>

            <input type='text' placeholder='Update District Number' value={districtnum} onChange={(e)=>setdistrictnum(e.target.value)}/> 
            <button type='submit' onClick={submit}>submit</button> 
            <button type='submit' onClick={DefinedDistrict}>Save</button> <br></br>
           
           
            {totalpop && <p>
               
                <label style={{marginRight:'3px'}}><strong> Total Population is: </strong> <em> 5032425 </em></label> 
                <br></br>
              
                <label> <strong> District range is between: </strong> <em> {lower} </em>and <em> {upper} </em> </label> 
                
                
                
            </p> } 
            {<FaPaintBrush className="paint-brush" style={{fontSize:'30px'}} onClick={handlepaint}/>} 
            
            <FaRegHandPaper className="hand-cursor"  onClick={handlecursor}/>
            
            <BsEraser className='eraser' onClick={() => sendid(100)} /> 
             <br></br>
            {colorpalette && (
                <>
            <button style={{background:'#ff1a1a', width:'35px', borderRadius: 10,height:'35px', color:'black'}} onClick={() => sendid(11)}>11</button>
            <button style={{background:'#ff8080', width:'35px', borderRadius: 10, height:'35px', color:'black'}} onClick={() => sendid(12)}>12</button>
            <button style={{background:'#ffb3b3',width:'35px', borderRadius:10,height:'35px', color:'black'}} onClick={() => sendid(13)}>13</button> 
            <button style={{background:'#ffe6e6',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(14)}>14</button>
            <button style={{background :'#ff0000',width:'35px', borderRadius: 10, height:'35px', color: 'black'}} onClick={ () => sendid(15)}>15</button>
            <button style={{background:'#b30000', width:'35px',borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(16)}>16</button> 
            <button style={{background:'#4d0000',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(17)}>17</button> 
            <button style={{background:'#ff8000',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(18)}>18</button> 
            <button style={{background:'#ffbf00',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(19)}>19</button> 
            <button style={{background:'#ffff00',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(20)}>20</button> <br></br>
            <button style={{background :'#bfff00',width:'35px', borderRadius: 10, height:'35px', color: 'black'}} onClick={ () => sendid(21)}>21</button>
            <button style={{background:'#80ff00',width:'35px', borderRadius: 10, height:'35px', color:'black'}} onClick={() => sendid(22)}>22</button>
            <button style={{background:'#40ff00',width:'35px', borderRadius: 10, height:'35px', color:'black'}} onClick={() => sendid(23)}>23</button>
            <button style={{background:'#00ff00',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(24)}>24</button> 
            <button style={{background:'#00ff40',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(25)}>25</button>
            <button style={{background:'#00ff80',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(26)}>26</button> 
            <button style={{background:'#00ffbf',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(27)}>27</button> 
            <button style={{background:'#00ffff',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(28)}>28</button> 
            <button style={{background:'#00bfff',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(29)}>29</button> 
            <button style={{background:'#0080ff',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(30)}>30</button> <br></br>
            <button style={{background :'#0040ff',width:'35px', borderRadius: 10, height:'35px', color: 'black'}} onClick={ () => sendid(31)}>31</button>
            <button style={{background:'#0000ff',width:'35px', borderRadius: 10, height:'35px', color:'black'}} onClick={() => sendid(32)}>32</button>
            <button style={{background:'#4000ff',width:'35px', borderRadius: 10, height:'35px', color:'black'}} onClick={() => sendid(33)}>33</button>
            <button style={{background:'#8000ff',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(34)}>34</button> 
            <button style={{background:'#bf00ff',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(35)}>35</button> 
            <button style={{background:'#ff00ff',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(36)}>36</button> 
            <button style={{background:'#ff00bf',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(37)}>37</button> 
            <button style={{background:'#ff0080',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(38)}>38</button> 
            <button style={{background:'#ff0040',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(39)}>39</button> 
            <button style={{background:'#996680',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(40)}>40</button> <br></br>
            <button style={{background :'#80c4b7',width:'35px', borderRadius: 10, height:'35px', color: 'black'}} onClick={ () => sendid(41)}>41</button>
            <button style={{background:'#eeeeee', width:'35px',borderRadius: 10, height:'35px', color:'black'}} onClick={() => sendid(42)}>42</button>
            <button style={{background:'#feffba',width:'35px', borderRadius: 10, height:'35px', color:'black'}} onClick={() => sendid(43)}>43</button>
            <button style={{background:'#c90076',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(44)}>44</button> 
            <button style={{background:'#073763',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(45)}>45</button> 
            <button style={{background:'#669999',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(46)}>46</button> 
            <button style={{background:'#ffa500',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(47)}>47</button> 
            <button style={{background:'#476b6b',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(48)}>48</button> 
            <button style={{background:'#854442',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(49)}>49</button> 
            <button style={{background:'#f24e70',width:'35px', borderRadius:10, height:'35px', color:'black'}} onClick={() => sendid(50)}>50</button> <br></br>

                </>
          
            )}
            {cursor && colorpalette}
            {eraser && colorpalette && cursor}
            
            {/* <SketchPicker/> */}
            
            <button onClick={() => handletab('Inspect')} style={{fontSize:'20px', padding:'10px', width:'150px'}}>Inspect</button>
            <button onClick={() => handletab('DataLayer')} style={{fontSize: '20px', padding: '10px', width:'150px'}}>Data Layer</button>
            <button onClick={() => handletab('Evaluation')} style={{fontSize: '20px', padding: '10px', width:'150px'}}>Evaluation</button>
            {selecttab === 'Inspect' && <Inspect MUid = {id}/>}
            {selecttab === 'DataLayer' && <DataLayer/>}
            {selecttab === 'Evaluation' && <Evaluation/>}
            {/* {console.log("Sidebar",DGUID)} */}
 
        </div>
       
  )
}

export default Sidebar
