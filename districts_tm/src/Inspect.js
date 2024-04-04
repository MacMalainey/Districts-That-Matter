import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';
let mapdemoarray = []
function Inspect() {

    const [mapiddemo, setmapiddemo] = useState(null)
    const[demodata, setdemodata] = useState(null)
    const[charact, setcharact] = useState('')
    const[id,setid] = useState(null)
    const[inspectmap, setinspectmap] = useState(false)
    const[inspectCOI,setinspectCOI]= useState(false)
    const[COIcharact, setCOIcharact] = useState(null)
    const COIotherarray = JSON.parse(localStorage.getItem('COIotherarray'))

    const[newdata, setnewdata] = useState([])
    const [showcoionmap, setshowcoionmap] = useState(false)
    const[newcoidata, setnewcoidata] = useState([])
    const currenttab = localStorage.getItem('currenttab')
   
    useEffect(()=>{
        setid(localStorage.getItem('mapid'))
    })

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
        
            
   
        
         
         

   

        const handlemapdemo = () => {
            const filteredmaparray = newdata.filter((val) => val[1].startsWith(charact) && val[2]!==0)
            return <p>
                    {newdata && <ul>

                        {filteredmaparray.map((charact,indexvalue)=>(<li key={indexvalue}>
            <table>
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

  return (
    <div>
    <h3><em>Demographic Data </em></h3>
      <label>Map Units</label>
      <input type='checkbox' value={inspectmap} onChange={()=>setinspectmap(!inspectmap)}></input>

      <label>Show COI on Map</label>
      <input type='checkbox' value={showcoionmap} onChange={()=>setshowcoionmap(!showcoionmap)}></input>
      {showcoionmap && localStorage.setItem('showcoionmap', 1)}
      {!showcoionmap && localStorage.setItem('showcoionmap', 0)}
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
