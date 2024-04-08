import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';
import { click } from '@testing-library/user-event/dist/click';
import './Evaluation.css';
// let inspectpop = []

function Evaluation() {
  // implemented FR 6 and FR7 
  // district number is taken as user input and we recalculate population range per district
  const [totalpop, settotalpop] = useState(null)
  const [districtdemo, setdistrictdemo] = useState(null)
  const totaldistrict = localStorage.getItem('TotalDistricts')
  const [selectTP, setselectTP] = useState(false)
  const [selectDD, setselectDD] = useState(false)
  const [selectpop, setselectpop] = useState(false)
  const [selectcharact, setselectcharact] = useState(null)
  const [secondcharact, setsecondcharact] = useState(null)
  const [population, setpopulation] = useState(null)
 const[disdemo, setdisdemo] = useState(null)
  //test2

  useEffect(()=>{
    const handledistrictdemo = async () =>{
     
      let inspectpop = []
      let inspectdemo = []
      let idk = []
    
      const response = await axios.get('http://127.0.0.1:5000/api/districts/demographics')
      const inspectDD = response.data
      console.log("Raw data", inspectDD)
        for (let k in inspectDD){
          console.log(k)
          idk.push(k)
          console.log("ids", idk)
          // inspectpop.push([k,"population", inspectDD[k].population]) 
        }

        idk.forEach(value =>{
          console.log(value, inspectDD[value].population)
          inspectpop.push([value, "population", inspectDD[value].population])
          setpopulation(inspectpop)
          for(let j in inspectDD[value]){
            console.log(value, j, inspectDD[value][j])

            inspectdemo.push([value, j , inspectDD[value][j]])
            setdisdemo(inspectdemo)
          }
          
        })


       
    }
    
    handledistrictdemo();

 
   
  }, [])
  
 

  const handleinspectChar = () => {
    const filteredinspectcharact = disdemo.filter((arr)=>arr[1]===selectcharact)
    // const filsecondcharact = inspectdata.filter((arr2)=>arr2[1]===secondcharact)
    const addcolor = filteredinspectcharact.map((chek)=> {
      console.log(chek[0])
      if(chek[0]==11){
        return [...chek,'#ff1a1a']
      }
      else if(chek[0]==12){
        return [...chek,'#ff8080']
      }
      else if(chek[0]==13){
        return [...chek,'#ffb3b3']
      }
      else if(chek[0]==14){
        return [...chek,'#ffe6e6']
      }
      else if(chek[0]==15){
        return [...chek,'#ff0000']
      }
      else if(chek[0]==16){
        return [...chek,'#b30000']
      }
      else if(chek[0]==17){
        return [...chek,'#4d0000']
      }
      else if(chek[0]==18){
        return [...chek,'#ff8000']
      }
      else if(chek[0]==19){
        return [...chek,'#ffbf00']
      }
      else if(chek[0]==20){
        return [...chek,'#ffff00']
      }
      else if(chek[0]==21){
        return [...chek,'#bfff00']
      }
      else if(chek[0]==22){
        return [...chek,'#80ff00']
      }
      else if(chek[0]==23){
        return [...chek,'#40ff00']
      }
      else if(chek[0]==24){
        return [...chek,'#00ff00']
      }
      else if(chek[0]==25){
        return [...chek,'#00ff40']
      }
      else if(chek[0]==26){
        return [...chek,'#00ff80']
      }
      else if(chek[0]==27){
        return [...chek,'#00ffbf']
      }
      else if(chek[0]==28){
        return [...chek,'#00ffff']
      }
      else if(chek[0]==29){
        return [...chek,'#00bfff']
      }
      else if(chek[0]==30){
        return [...chek,'#0080ff']
      }
      else if(chek[0]==31){
        return [...chek,'#0040ff']
      }
      else if(chek[0]==32){
        return [...chek,'#0000ff']
      }
      else if(chek[0]==33){
        return [...chek,'#4000ff']
      }
      else if(chek[0]==34){
        return [...chek,'#8000ff']
      }
      else if(chek[0]==35){
        return [...chek,'#bf00ff']
      }
      else if(chek[0]==36){
        return [...chek,'#ff00ff']
      }
      else if(chek[0]==37){
        return [...chek,'#ff00bf']
      }
      else if(chek[0]==38){
        return [...chek,'#ff0080']
      }
      else if(chek[0]==39){
        return [...chek,'#ff0040']
      }
      else if(chek[0]==40){
        return [...chek,'#996680']
      }
      else if(chek[0]==41){
        return [...chek,'#80c4b7']
      }
      else if(chek[0]==42){
        return [...chek,'#eeeeee']
      }
      else if(chek[0]==43){
        return [...chek,'#feffba']
      }
      else if(chek[0]==44){
        return [...chek,'#c90076']
      }
      else if(chek[0]==45){
        return [...chek,'#073763']
      }
      else if(chek[0]==46){
        return [...chek,'#669999']
      }
      else if(chek[0]==47){
        return [...chek,'#ffa500']
      }
      else if(chek[0]==48){
        return [...chek,'#476b6b']
      }
      else if(chek[0]==49){
        return [...chek,'#854442']
      }
      else if(chek[0]==50){
        return [...chek,'#f24e70']
      }
    })
    
    return <p> Compare a Characteristic:  
      <select value={selectcharact} onChange={(e)=>setselectcharact(e.target.value)}>
    <option style={{fontStyle:'italic'}}> select...</option>
  
    {disdemo.map((charact,indexvalue) =>(
      <option key={indexvalue} value={charact[1]}>{charact[1]}</option>
    ))}

    
    </select>
     {/* <p> with </p> 
    <select value={secondcharact} onChange={(e)=>setsecondcharact(e.target.value)}>
    <option style={{fontStyle:'italic'}}> select...</option>
  
    {inspectdata.map((charact,indexvalue) =>(
      <option key={indexvalue} value={charact[1]}>{charact[1]}</option>
    ))} */}

    
    {/* </select> */}
       
       {selectcharact  && <p>
        <table> 
        <tr>
              <th> DN  </th> 
              <th></th>
              <th></th>
              <th>
                {selectcharact}
              </th>
              <th></th>
              <th></th>
              <th>{secondcharact}</th>

              

            </tr >

       
        
        {addcolor.map((charact,indexvalue)=>(

              <tr key={indexvalue}>
                <td style={{background: charact[3],width:'35px', borderRadius:10, height:'15px', color:'black', paddingLeft:'20px'}}> {charact[0]} </td>
                <td></td>
                <td></td>
                <td>{charact[2]}</td>
                <td></td>
                <td></td>
                <td></td>

              </tr>

        ))}
        

        {/* {filsecondcharact.map((charact,indexvalue)=>(
          
          <tr   key={indexvalue}>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>{charact[2]}</td>
            
          </tr>

))} */}
       </table>
      </p>}
    </p>
    
  }


  const handlepopulation = () => {
    const filteredinspectcharact = population.filter((arr)=>arr[1]==='population')
    const addcolor = filteredinspectcharact.map((chek)=> {
      console.log(chek[0])
      if(chek[0]==11){
        return [...chek,'#ff1a1a']
      }
      else if(chek[0]==12){
        return [...chek,'#ff8080']
      }
      else if(chek[0]==13){
        return [...chek,'#ffb3b3']
      }
      else if(chek[0]==14){
        return [...chek,'#ffe6e6']
      }
      else if(chek[0]==15){
        return [...chek,'#ff0000']
      }
      else if(chek[0]==16){
        return [...chek,'#b30000']
      }
      else if(chek[0]==17){
        return [...chek,'#4d0000']
      }
      else if(chek[0]==18){
        return [...chek,'#ff8000']
      }
      else if(chek[0]==19){
        return [...chek,'#ffbf00']
      }
      else if(chek[0]==20){
        return [...chek,'#ffff00']
      }
      else if(chek[0]==21){
        return [...chek,'#bfff00']
      }
      else if(chek[0]==22){
        return [...chek,'#80ff00']
      }
      else if(chek[0]==23){
        return [...chek,'#40ff00']
      }
      else if(chek[0]==24){
        return [...chek,'#00ff00']
      }
      else if(chek[0]==25){
        return [...chek,'#00ff40']
      }
      else if(chek[0]==26){
        return [...chek,'#00ff80']
      }
      else if(chek[0]==27){
        return [...chek,'#00ffbf']
      }
      else if(chek[0]==28){
        return [...chek,'#00ffff']
      }
      else if(chek[0]==29){
        return [...chek,'#00bfff']
      }
      else if(chek[0]==30){
        return [...chek,'#0080ff']
      }
      else if(chek[0]==31){
        return [...chek,'#0040ff']
      }
      else if(chek[0]==32){
        return [...chek,'#0000ff']
      }
      else if(chek[0]==33){
        return [...chek,'#4000ff']
      }
      else if(chek[0]==34){
        return [...chek,'#8000ff']
      }
      else if(chek[0]==35){
        return [...chek,'#bf00ff']
      }
      else if(chek[0]==36){
        return [...chek,'#ff00ff']
      }
      else if(chek[0]==37){
        return [...chek,'#ff00bf']
      }
      else if(chek[0]==38){
        return [...chek,'#ff0080']
      }
      else if(chek[0]==39){
        return [...chek,'#ff0040']
      }
      else if(chek[0]==40){
        return [...chek,'#996680']
      }
      else if(chek[0]==41){
        return [...chek,'#80c4b7']
      }
      else if(chek[0]==42){
        return [...chek,'#eeeeee']
      }
      else if(chek[0]==43){
        return [...chek,'#feffba']
      }
      else if(chek[0]==44){
        return [...chek,'#c90076']
      }
      else if(chek[0]==45){
        return [...chek,'#073763']
      }
      else if(chek[0]==46){
        return [...chek,'#669999']
      }
      else if(chek[0]==47){
        return [...chek,'#ffa500']
      }
      else if(chek[0]==48){
        return [...chek,'#476b6b']
      }
      else if(chek[0]==49){
        return [...chek,'#854442']
      }
      else if(chek[0]==50){
        return [...chek,'#f24e70']
      }
    })
    

    return <p>
      
      <button style={{ marginTop:'10px', border:' 3px solid green' , width:'30px', borderRadius: 4,height:'15px', fontSize:'10px'}}></button>
      <label style={{fontSize:'12px'}}> "Population between Min Pop and Max Pop   </label> 
      <button style={{ marginLeft:'5px', border:' 3px solid red' , width:'30px', borderRadius: 4,height:'15px', fontSize:'10px'}}></button>
      <label style={{fontSize:'12px'}}> " Otherwise </label>
      
      
     
       
       {<p>
        <table style={{ marginRight:'3px', boxShadow: '10px 20px 9px darkgrey'}}> 
        <tr>
              <th> DN  </th> 
              <th></th>
              <th></th>
              <th>
                Population
              </th>
              <th></th>
              <th></th>
              <th>{secondcharact}</th>
              <th>Analysis</th>
              <th></th>
              <th> Min % req</th>
              <th> Max % req </th>
            </tr >

       
        
        {addcolor.map((charact,indexvalue)=>(
            
              <tr  key={indexvalue}>
                <td style={{background: charact[3],width:'35px', borderRadius:10, height:'15px', color:'black', paddingLeft:'20px'}}> {charact[0]} </td>
                <td></td>
                <td></td>
                <td>{charact[2]}</td>
                <td></td>
                <td></td>
                <td></td>
                <td>
                
                <div className='set' style={{position:'relative', width:'160px', height:'10px', background:'lightgrey'}}>
                    <div className='vertical' style={{position:'absolute', width:'1px', height:'100%', background:'black', left:'96px', top:'0px'}}>

                    </div>
                </div>

                <progress className='progress' style={{'--progress':`${charact[2] / localStorage.getItem('upper')} %`,  height:'25px', border:  charact[2] > localStorage.getItem('upper')? '2px solid red':(charact[2] < localStorage.getItem('lower') ? '2px solid red' :'2px solid green')}}   max={localStorage.getItem('upper')} value={charact[2]} >  </progress>
                <span> {Math.floor(charact[2] / localStorage.getItem('upper') * 100)}%</span>
                  
                </td>
                <td></td>
                <td> {Math.floor(localStorage.getItem('lower') / localStorage.getItem('upper') * 100)}% </td>
               <td> 100 % </td>
              </tr>

        ))}
        

        
       </table>
      </p>}
    </p>
    
  }
  
  

  return (
    <div className='eval'>
      
      
      <label>Show Total Population</label>
      <input type='checkbox' value={selectTP} onChange={() =>setselectTP(!selectTP)}></input>
      <label>Compare District's</label>
      <input type='checkbox' value={selectDD} onChange={() =>setselectDD(!selectDD)}></input>
      {/* <p> {localStorage.getItem('population')}</p> */}
      {selectTP && handlepopulation()}
      
      {selectDD && <br></br> && handleinspectChar()}
      
    </div>
  )
}

export default Evaluation
