// this component allows user to set number of districts and get a population range for each district
// allows user to toggle between paint, erase and back to cursor
// allows user to save districts once they are drawn 
//fullfills FR 6. FR 7, FR 16, FR 17, FR 18, FR 19, FR 20


import {React, useContext, useEffect, useState} from 'react'
import './Sidebar.css'; // Import your CSS file
import {SketchPicker} from 'react-color'
import { FaPaintBrush } from "react-icons/fa";
import { FaRegHandPaper } from "react-icons/fa";
import { BsEraser } from "react-icons/bs";
import Button from '@mui/material/Button'
// import { FaPaintBrush } from "react-icons/fa";
// import { FaHandPaper } from "react-icons/fa";
import Inspect from './Inspect';
import DataLayer from './DataLayer';
import Evaluation from './Evaluation';
import axios from 'axios';
import { DistrictsContext, MapModeContext } from './App';
import { MAP_MODE_ERASE, MAP_MODE_HAND, MAP_MODE_PAINT } from './config';

localStorage.setItem('currenttab',0)
function Sidebar() {
    const {data: mapMode, callback: setMapMode} = useContext(MapModeContext)
    const {data: districtData, callback: _} = useContext(DistrictsContext)
    const [selecttab, setselecttab] = useState(null)
    const[id,setid] = useState(null)
    const[districtnum, setdistrictnum] = useState(null)
    const [totalpop, settotalpop] = useState(false)
    const[lower, setlower] = useState(null)
    const[upper, setupper] = useState(null)

    const submit = () => {
        const num = Math.floor(totalpop/districtnum)
       setlower(Math.floor(num - num * 0.25))
       setupper(Math.floor(num + num * 0.25))
    }
    const handletab = (tab) => {
        if(tab === 'DataLayer') {
            localStorage.setItem('currenttab', 2)
        }
        else if (tab ==='Inspect') {
            localStorage.setItem('currenttab', 1)
        }
        else{
            localStorage.setItem('currenttab', 3)
        }
        

        setselecttab(tab)
    }

    const handlepaint = () =>{
        setMapMode(MAP_MODE_PAINT)
    }
    const handlecursor = () => {
        setMapMode(MAP_MODE_HAND)
    }
    const handleeraser = () => {
        setMapMode(MAP_MODE_ERASE)
    }
    const sendid = (colorid) => {
        localStorage.setItem('colorid', colorid)
    }
    
    // this function is saving the map units for a district
    //fullfills FR 19

    const DefinedDistrict = async () => {
            const testar = districtData
            let array = []
            for (let item in testar) {
                array.push([item, testar[item]])
            }
            await axios.post('http://127.0.0.1:5000/api/districts/update', array).catch(error =>{console.log(error)});
          }
            //Fullfills FR 6
    useEffect(()=>{
            const handlepopulation = async () =>{
              const response = await axios.get('http://127.0.0.1:5000/api/units/totals')
              const population = response.data.total_population 
              settotalpop(population)
        
            }
            handlepopulation();
          }, [])
   //return is handling user input for number of districts 
   // it allows user to toggle between paint, erase, cursor
   // it allows user to save drawn districts with a POST request
   // it draws color pallete with district numbers on it
   // it allows user to toggler between inspect tab, data layer tab and evaluation tab
  return (
    
        <div className = 'sidebar' style={{marginTop:'2px', marginRight:'2px'}}>
            <div style={{paddingTop: '4px', border: '1px solid black',  boxShadow: '10px 10px 5px #D8BFD8'}}>
            <input style={{border: '1px solid #D8BFD8', fontSize: '14px',borderRadius:'10px'}} type='text' placeholder='Update District Number' value={districtnum} onChange={(e)=>setdistrictnum(e.target.value)}/> 
            <Button style={{marginLeft: '5px'}} className= 'submit' type='submit' onClick={submit}>Update</Button> 
            <Button style={{marginLeft:'5px'}} type='submit' onClick={DefinedDistrict}>Save </Button> <br></br>

           
           
            {totalpop && <p>
               
                <label style={{marginRight:'3px'}}><strong> Total Population is: </strong> <em style={{background:'darkgrey'}}> 5032425 </em></label> 
                <br style={{marginBottom:'10px'}}></br> 
              
                <label> <strong> District range is between: </strong>  <input style={{width:'75px', borderRadius:'10px'}} value={lower}></input> and <input style={{width:'75px', borderRadius:'10px'}} value={upper}></input> </label> 
                
                {localStorage.setItem('lower', lower)}
                {localStorage.setItem('upper',upper)}
                
            </p> } 

            </div>
            
            {<FaPaintBrush className="paint-brush" style={{fontSize:'30px'}} onClick={handlepaint}/>} 
            
            <FaRegHandPaper className="hand-cursor"  onClick={handlecursor}/>
            
            <BsEraser className='eraser' onClick={handleeraser} /> 
             <br></br>
            {(mapMode == MAP_MODE_PAINT || mapMode == MAP_MODE_ERASE) && (
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
            
            {/* <SketchPicker/> */}
            
            <button onClick={() => handletab('Inspect')} style={{fontSize:'20px', padding:'10px', width:'145px'}}>Inspect</button>
            <button onClick={() => handletab('DataLayer')} style={{fontSize: '20px', padding: '10px', width:'145px'}}>Data Layer</button>
            <button onClick={() => handletab('Evaluation')} style={{fontSize: '20px', padding: '10px', width:'145px'}}>Evaluation</button>
            {selecttab === 'Inspect' && <Inspect className = 'inspect' MUid = {id}/>}
            {selecttab === 'DataLayer' && <DataLayer className = 'dl'/>}
            {selecttab === 'Evaluation' && <Evaluation className = 'eval'/>}
 
        </div>
       
  )
}

export default Sidebar
