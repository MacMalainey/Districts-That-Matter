// this component allows user to inspect dempographic data for each map unit, allows user to see COI's on the map and to inspect COI's
// it fullfills FR 9, FR 11, FR 12, FR 14, FR 15 

import React, { useEffect, useState, createContext, useContext} from 'react'
import axios, { all } from 'axios';
import { COISelectContext } from './App';
let mapdemoarray = []


function Inspect() {

    const [mapiddemo, setmapiddemo] = useState(null)
    const[demodata, setdemodata] = useState(null)
    const[charact, setcharact] = useState('')
    const[id,setid] = useState(null)
    const[inspectmap, setinspectmap] = useState(false)
    const[inspectCOI,setinspectCOI]= useState(false)
    const[COIcharact, setCOIcharact] = useState(null)
    const {data: showcoionmap, callback:setshowcoionmap} = useContext(COISelectContext)
    const COIotherarray = JSON.parse(localStorage.getItem('COIotherarray'))
    const[newdata, setnewdata] = useState([])
    // const [showcoionmap, setshowcoionmap] = useState(false)
    const[newcoidata, setnewcoidata] = useState([])
    const currenttab = localStorage.getItem('currenttab')
   // continuously render for the selected map id and set it
    useEffect(()=>{
        setid(localStorage.getItem('mapid'))
    })

    // check if id is there and tab is inspect
    // run demodata with a get request. 
    // this function loads the demographic data for the selected map unit (id to capture required data)

    useEffect(()=>{
        

        const DemoData = async () => {
            
            try {
              mapdemoarray = []
              const response = await axios.get('http://127.0.0.1:5000/api/units/' + id + '/demographics');
              const Alldata = response.data // storing the response data in a var which can be utilized. wrapper requirement.
            //   setdemodata(Alldata)
              
    
                    for (const k in Alldata){
                        mapdemoarray.push([id, k, Alldata[k]])
                        console.log("this is map data for an id", mapdemoarray)
                    }
    
                    console.log("array has changed too", id, mapdemoarray)
                    setnewdata(mapdemoarray)
            }
        
    
            catch {
              console.log('Response data not appropriately handled:');
            }
          }
          if(id && currenttab==1 && inspectmap==true){
            DemoData()
          }

    }, [id])
        
            
   
        
         
         

   
// once I have the demographic data available for the selected map unit, I am displaying it in a table 
        const handlemapdemo = () => {
            const filteredmaparray = newdata.filter((val) => val[1].startsWith(charact) && val[2]!==0)
            return <p >
                    {newdata && <ul >

                        {filteredmaparray.map((charact,indexvalue)=>(<li  key={indexvalue}>
            <table >
                <thead>
                <tr>
                    {charact[1]} has value {charact[2]}
                </tr>
                
                </thead>
            
            </table>
            
            </li>))}
                        
                        </ul>}
            </p>
            
        }
// this function shows a list of categories which user can select to inspect demographic data for
        const showdataformap = () => {
            return <p> 
                    <label>Select a Characteristic : </label>
      <select id='age' value={charact} onChange={(e)=>setcharact(e.target.value)}>
            <option value='Placeholder'>---</option>
        <option value='age'>Age</option>
            <option value='birthplace'>Birthplace</option>
            <option value='income'>Income</option>
            <option value='density'>Density</option>
            <option value='generation'>Generation</option>
            <option value='household'>Houshold</option>
            <option value='immigrated'>Imigrated</option>
            <option value = 'visible_minority'>Visible_Minority</option>
            <option value = 'population'>Population</option>
            <option value = 'landarea'>Landarea</option>
            <option value = 'marital_status'>Marital_Status</option>
            <option value = 'rc'> RC </option>
      </select>


            {charact && handlemapdemo()}
            </p>
        }

        useEffect(()=>{
            setnewcoidata(COIotherarray)
        })

// this function handles the COI demograpmic data and showing values for each category in a table
        const handlecoidemo = () => {
            
            const filteredmaparray = newcoidata.filter((par) => par[0].startsWith(COIcharact) && !par[0].includes('ratio') && par[1]!==0)
            return <p>
                    {newcoidata && <ul>
                        {filteredmaparray.map((charact,indexvalue)=>(<li key={indexvalue}>
            <table>
                <thead>
                <tr>
                    {charact[0]} has value {charact[1]}
                </tr>
                
                </thead>
            
            </table>
            
            </li>))}
                        
                        </ul>}
            </p>
            
        }

// this is a list of characteristics user can select to inspect COIs 
        const showdataforCOI = () => {
            return <p> 
                    <label>Select a COI Characteristic : </label>
      <select id='age' value={COIcharact} onChange={(e)=>setCOIcharact(e.target.value)}>
            <option value='Placeholder'>---</option>
        <option value='age'>Age</option>
            <option value='birthplace'>Birthplace</option>
            <option value='income'>Income</option>
            <option value='density'>Density</option>
            <option value='generation'>Generation</option>
            <option value='household'>Houshold</option>
            <option value='immigrated'>Imigrated</option>
            <option value = 'visible_minority'>Visible_Minority</option>
            <option value = 'population'>Population</option>
            <option value = 'landarea'>Landarea</option>
            <option value = 'marital_status'>Marital_Status</option>
            <option value = 'rc'> RC </option>
      </select>

            {COIcharact && handlecoidemo()}
            </p>
        }

  // return will allow user to select what category to inspect for a selected COI
// it will allow user to select what category to inspect for a map unit
// allow the user to click on showcoionmap to have COIs reflectd on the map
  return (
    <div>
    <h3><em>Demographic Data </em></h3>
      <label>Map Units</label>
      <input type='checkbox' value={inspectmap} onChange={()=>setinspectmap(!inspectmap)}></input>

      <label>Show COI on Map</label>
      <input type='checkbox' value={showcoionmap} onChange={()=>setshowcoionmap(!showcoionmap)}></input>
      
      
      {/* {showcoionmap && localStorage.setItem('showcoionmap', 1)}
      {!showcoionmap && localStorage.setItem('showcoionmap', 0)} */}
      {showcoionmap&& <p>
        <label> COI District</label>
      <input type='checkbox' value={inspectCOI} onChange={()=>setinspectCOI(!inspectCOI)}></input>
        </p>}
      
      {inspectmap && showdataformap()}
      

      
    {inspectCOI && showdataforCOI()}
    
      
    
    </div>
  )
}

export default Inspect
