import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';
let mapdemoarray = []
function Inspect() {

    const [mapiddemo, setmapiddemo] = useState(null)
    const[demodata, setdemodata] = useState(null)
    const[charact, setcharact] = useState('')
    const[id,setid] = useState(null)

    

    useEffect(()=>{
        const DemoData = async () => {
            setid(localStorage.getItem('mapid'))
            try {
              const response = await axios.get('http://127.0.0.1:5000/api/units/' + id + '/demographics');
              const Alldata = response.data // storing the response data in a var which can be utilized. wrapper requirement.
            //   setdemodata(Alldata)
              console.log('http://127.0.0.1:5000/api/units/' + id + '/demographics')
                    for (const k in Alldata){
                        mapdemoarray.push([id, k, Alldata[k]])
                        console.log("this is map data for an id", mapdemoarray)
                    }
                    
                    
                    
              
              
           
            }
            catch {
              console.log('Response data not appropriately handled:');
            }
          }
         DemoData();
         mapdemoarray = []

    })

        const handlemapdemo = () => {
            const filteredmaparray = mapdemoarray.filter((val) => val[1].startsWith(charact) && val[2]!==0)
            return <p>
                    {charact && <ul>
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


  return (
    <div>
      
      
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
      
      
    
    </div>
  )
}

export default Inspect
