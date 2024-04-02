import { Draw } from "leaflet"
import React, {useEffect, useState} from "react"
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Polyline, GeoJSON, LayersControl, Marker, Popup} from 'react-leaflet';
import TestPoly from "./TestGeo";
import L from 'leaflet';
import './Map.css';
import axios, { all } from 'axios';
import Sidebar from "./Sidebar";
import { eventWrapper } from "@testing-library/user-event/dist/utils";
import { BsBox } from "react-icons/bs";
import {colors} from './config';

// FR1: Map Render
// FR2: Map Fetch
// FR3: Map.Units.Render
// FR4: Map.Units.Fetch
// FR5: Map.Navigate
let changes = {};
let COIarray = [];
let Visualarray = [];
localStorage.setItem('coloractive', '')
localStorage.setItem('mapid','')
localStorage.setItem('colorid','')
localStorage.setItem('COIexp', '')
let COIotherarray = [];
function DrawMap(){
  
    const center = [ 43.65107, - 79.347015];
    const [selectedmapunit, setselectedmapunit] = useState(null);
    const [selectedmapunitid, setselectedmapunitid] = useState(null);
    const [allda, setallda] = useState(null)
    const [coida, setcoida] = useState(null)
    const[dguid, setdguid] = useState(15)
    const coloractiveid = localStorage.getItem('coloractive')
    const colid = localStorage.getItem('colorid')
    const cursorid = localStorage.getItem('cursor')
    const eraseractiveid = localStorage.getItem('eraser')
    // set onselect color and onselect again, deselect and change back to grey
    const[state, setstate] = useState(false);
    const[Dmapid, setDmapid] = useState()
    const[Dcolorid, setDcolorid] = useState()
    const[selectedCOI, setselectedCOI] = useState(null)
    const[selectedCOIdata, setselectedCOIdata] = useState(null)
    const [vsda, setvsda] = useState(null)
    const[gradient, setgradient] = useState(null)
    const [VOincome, setVOincome] = useState(null)
    const[VOvisibleM, setVOvisibleM] = useState(null) 
    const[VObirthplace, setVObirthplace] = useState(null)
    const[VOpop, setVOpop] = useState(null)
    const showonmap = localStorage.getItem('showonmap')
    const showCOIonmap = localStorage.getItem('showcoionmap')
    const colormapunit = (mapunit) => {
      const base = {
        fillOpacity: 0,
        weight: 0
      };
      const did = changes[mapunit.id];
      if (did != undefined || did != null) {
        base['fillOpacity'] = 0.6;
        base['fillColor'] = colors[did - 11]
      }
      return base
    };

    // gradient for ages

    useEffect(()=>{
      const handletest = async () =>{
        try{
          const response = await axios.get('http://127.0.0.1:5000/api/units/all?include=ages')
          setgradient(response.data)
          
          
          // for (const temp in testage[0]){
          //   console.log(testage[0][temp])
          // }
        }
        catch{
          console.log("Error in Data retrival process....")
        }
        
        // console.log(testage)
        // testage.push([testage])
        // settotalpop("this is just a test, Harsh:", testage)
        // console.log("test Harsh", testage)
  
      }
      handletest();
    }, [])

    //gradient for income
    useEffect(()=>{
      const handleincome = async () =>{
        try{
          const response = await axios.get('http://127.0.0.1:5000/api/units/all?include=income')
          setVOincome(response.data)
          
          
          // for (const temp in testage[0]){
          //   console.log(testage[0][temp])
          // }
        }
        catch{
          console.log("Error in Data retrival process....")
        }
        
        // console.log(testage)
        // testage.push([testage])
        // settotalpop("this is just a test, Harsh:", testage)
        // console.log("test Harsh", testage)
  
      }
      handleincome();
    }, [])

    // visible minority 
    useEffect(()=>{
      const handlevisibleM = async () =>{
        try{
          const response = await axios.get('http://127.0.0.1:5000/api/units/all?include=visible_minority')
          setVOvisibleM(response.data)
          
          
          // for (const temp in testage[0]){
          //   console.log(testage[0][temp])
          // }
        }
        catch{
          console.log("Error in Data retrival process....")
        }
        
        // console.log(testage)
        // testage.push([testage])
        // settotalpop("this is just a test, Harsh:", testage)
        // console.log("test Harsh", testage)
  
      }
      handlevisibleM();
    }, [])

    useEffect(()=>{
      const handlebirthplace = async () =>{
        try{
          const response = await axios.get('http://127.0.0.1:5000/api/units/all?include=birthplace')
          setVObirthplace(response.data)
          
          
          // for (const temp in testage[0]){
          //   console.log(testage[0][temp])
          // }
        }
        catch{
          console.log("Error in Data retrival process....")
        }
        
        // console.log(testage)
        // testage.push([testage])
        // settotalpop("this is just a test, Harsh:", testage)
        // console.log("test Harsh", testage)
  
      }
      handlebirthplace();
    }, [])

    // population 
    useEffect(()=>{
      const handleVOpop = async () =>{
        try{
          const response = await axios.get('http://127.0.0.1:5000/api/units/all')
          setVOpop(response.data)
          
          
          // for (const temp in testage[0]){
          //   console.log(testage[0][temp])
          // }
        }
        catch{
          console.log("Error in Data retrival process....")
        }
        
        // console.log(testage)
        // testage.push([testage])
        // settotalpop("this is just a test, Harsh:", testage)
        // console.log("test Harsh", testage)
  
      }
      handleVOpop();
    }, [])



    useEffect(()=>{

      const MapData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/units/all');
          const Alldata = response.data // storing the response data in a var which can be utilized. wrapped requirement.
          setallda(Alldata);
          
          // console.log("original mapda:", Alldata)
          // console.log(Alldata)
        }
        catch {
          console.log('Response data not appropriately handled:');
        }
      }

       MapData();
        
        
      }, [])
// COI data coordinate collection
// covers FR 13, FR 14, FR 15
      useEffect(()=>{

        const COIData = async () => {
          try {
            const response = await axios.get('http://127.0.0.1:5000/api/cois/all');
            const coidata = response.data // storing the response data in a var which can be utilized. wrapped requirement.
            // console.log("COI data, lets check",coidata)
            // for (const tes in coidata){
            //   console.log("testing COI info:", tes)
            // }
               setcoida(response.data);
              // console.log(response.data)
            

          }
          catch {
            console.log('Response data not appropriately handled:');
          }
        }
  
         COIData();
          
          
        }, [coida])
// handler explaination for each selected id, store in local storage
  

      // useEffect(()=>{
      //   const handleCOI = () => {
      //   try{
         
      //     for (const reason in selectedCOI){
      //       const ite = selectedCOI[reason]
      //       // console.log("interpretation of {} this item is", reason, ite.interpretation)
      //       COIarray.push([reason, ite.interpretation])
      //       localStorage.setItem('COIexp', JSON.stringify(COIarray))
            
      //     }
      //   }
      
      //   catch{
      //     console.log("Error with COI explanation parsing......")
      //   }
          
      //   COIarray=[] // clear array after storage, otherwise it will append to the existing array. 
      //   }
      //   //  console.log("selected COI explanation is:", selectedCOI.generation_first.interpretation)
      //   handleCOI();
        
        
      // }, [])
// handle COI data for selected COI, except explanation, which is handled separately. 
      useEffect(()=>{
        const handleCOIother = () => {
          COIotherarray=[]
        try{
          if(COIotherarray.length!=132){

          
          for (const tempdata in selectedCOIdata){
            // console.log(tempdata,selectedCOIdata)
            const tempval = selectedCOIdata[tempdata]
            // console.log("interpretation of {} this item is", reason, ite.interpretation)
            // COIotherarray.push([tempdata, tempval])
            COIotherarray.push([tempdata,tempval])
            console.log("COIotherarray:", COIotherarray)
            localStorage.setItem('COIotherarray', JSON.stringify(COIotherarray))
            // localStorage.setItem('COIexp', JSON.stringify(COIarray))
            
          }
        }
      }
        catch{
          console.log("Error with COI explanation parsing......")
        }
          
        COIarray=[] // clear array after storage, otherwise it will append to the existing array. 
        }
        //  console.log("selected COI explanation is:", selectedCOI.generation_first.interpretation)
        handleCOIother();
        
        
      }, [selectedCOIdata])
//  this gets the mapid only after its set
      useEffect(()=>{
        if (selectedmapunitid !=null){
        localStorage.setItem('mapid', selectedmapunitid)
        console.log("selected map unit is: ", selectedmapunitid)
        definedistrict(selectedmapunitid,colid)
        }
        
        
      }, [selectedmapunitid])

      // this function checks for dguids and color id, if the id is non 100, it sends both values otherwise it sends a null as in erase 
      
        const definedistrict= (val1, val2) =>{
          
          try { 


          
            if (val2==100){

                changes[val1] = null
              }
            else {
              changes[val1] = parseInt(val2)
            }
            
              
          }
            
          catch {
            console.log("Cant recieve id's on time")
          }
          
         }


  const gradientmapunit = (gradient) => {

    // console.log("Demag kharab", gradient)
    const getvalue = localStorage.getItem('selectedage')
    const testage = gradient.properties[getvalue]
    const  testrc = gradient.properties['rc_ages']
    const result = (testage / testrc) * 100
    console.log(result)
    if(result < 5){
        return {
                fillColor: '#CCCCCC',
                color: 'lightgrey'  ,
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
    }
    else if (result > 5.1 && result < 8.1){
      return {
        fillColor: '#999999',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else {
      return {
        fillColor: '#333333',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
           
            }
        
        const gradientincomemapunit = (VOincome) => {

              // console.log("Demag kharab part 2", VOincome)
              const getvalue = localStorage.getItem('selectedage')
              const testincome = VOincome.properties[getvalue]
              const  testrc = VOincome.properties['rc_income']
              const result = (testincome / testrc) * 100
              console.log(result)
              if(result < 2){
                  return {
                          fillColor: '#CCCCCC',
                          color: 'lightgrey'  ,
                          weight: 0.5, 
                          fillOpacity: 0.3,
                           
                        };
              }
              else if (result > 2.1 && result < 4.1){
                return {
                  fillColor: '#999999',
                  color: 'lightgrey',
                  weight: 0.5, 
                  fillOpacity: 0.3,
                   
                };
              }
              else {
                return {
                  fillColor: '#333333',
                  color: 'lightgrey',
                  weight: 0.5, 
                  fillOpacity: 0.3,
                   
                };
              }
                     
        }

        const gradientvisibleMmapunit = (VOvisibleM) => {

          // console.log("Demag kharab part 2", VOincome)
          const getvalue = localStorage.getItem('selectedage')
          const testvisibleM = VOvisibleM.properties[getvalue]
          const  testrc = VOvisibleM.properties['rc_visible_minority']
          const result = (testvisibleM / testrc) * 100
          console.log(result)
          if(result < 2){
              return {
                      fillColor: '#CCCCCC',
                      color: 'lightgrey'  ,
                      weight: 0.5, 
                      fillOpacity: 0.3,
                       
                    };
          }
          else if (result > 2.1 && result < 4.1){
            return {
              fillColor: '#999999',
              color: 'lightgrey',
              weight: 0.5, 
              fillOpacity: 0.3,
               
            };
          }
          else {
            return {
              fillColor: '#333333',
              color: 'lightgrey',
              weight: 0.5, 
              fillOpacity: 0.3,
               
            };
          }
                 
    }   


    const gradientbirthplacemapunit = (VObirthplace) => {

      // console.log("Demag kharab part 2", VOincome)
      const getvalue = localStorage.getItem('selectedage')
      const testbirthplace = VObirthplace.properties[getvalue]
      const  testrc = VObirthplace.properties['rc_birthplace']
      const result = (testbirthplace / testrc) * 100
      console.log(result)
      if(result < 40){
          return {
                  fillColor: '#CCCCCC',
                  color: 'lightgrey'  ,
                  weight: 0.5, 
                  fillOpacity: 0.3,
                   
                };
      }
      else if (result > 40.1 && result < 60){
        return {
          fillColor: '#999999',
          color: 'lightgrey',
          weight: 0.5, 
          fillOpacity: 0.3,
           
        };
      }
      else {
        return {
          fillColor: '#333333',
          color: 'lightgrey',
          weight: 0.5, 
          fillOpacity: 0.3,
           
        };
      }
             
}   


const gradientpopulationmapunit = (VOpop) => {

  // console.log("Demag kharab part 2", VOincome)
  const getvalue = localStorage.getItem('selectedage')
  const testpop = VOpop.properties[getvalue]
  // console.log("pop count", testpop)
  const  testrc_pop = 29669 
  const result = (testpop / testrc_pop) * 100
  // console.log(result)
  if(result < 30){
      return {
              fillColor: '#CCCCCC',
              color: 'lightgrey'  ,
              weight: 0.5, 
              fillOpacity: 0.3,
               
            };
  }
  else if (result > 30.1 && result < 60){
    return {
      fillColor: '#999999',
      color: 'lightgrey',
      weight: 0.5, 
      fillOpacity: 0.3,
       
    };
  }
  else if (result > 60.1 && result < 80){
    return {
      fillColor: '#666666',
      color: 'lightgrey',
      weight: 0.5, 
      fillOpacity: 0.3,
       
    };
  }
  else {
    return {
      fillColor: '#333333',
      color: 'lightgrey',
      weight: 0.5, 
      fillOpacity: 0.3,
       
    };
  }
         
}   
        

    return (
      
        <div className="map">  
          
            
                 
                  <MapContainer center={center} zoom={10} style={{ height: '1000px' }}>
                  <TileLayer
                    
                    url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
                    
                  />
                   <LayersControl postition='topright'>
                    <LayersControl.BaseLayer name='Baselayer' checked='Baselayer'>
                    {allda  &&  <GeoJSON data = {allda} style={{ fillColor: 'transparent', color: 'grey', weight: 0.5}} eventHandlers={{click: (e) =>{setselectedmapunitid(e.layer.feature.id)} }} />}

                    </LayersControl.BaseLayer>
                    <LayersControl.Overlay name = 'ColorLayer'>
                    
                    {allda && (coloractiveid == 1 || coloractiveid==0) && <GeoJSON data = {allda} style={colormapunit} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature);
                    {console.log(e.layer.feature.id)}
                    setselectedmapunitid(e.layer.feature.id);
                    
                    
                    
                  }}} />}
                    </LayersControl.Overlay>

                    
                    </LayersControl>                             
                  
                  
                  {/* {allda && <GeoJSON data = {allda} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature.properties.dguid)}}} />} */}
                  {/* {allda && eraseractiveid==1 && coloractiveid == 0 && <GeoJSON data = {allda} style={decolormapunit} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature)}}} />} */}
                  {coida && showCOIonmap==1 && <GeoJSON data = {coida} style={{fillColor: 'red',color:'black',weight: 2,fillOpacity: 0.6}} eventHandlers = {{click: (e) => 
                    {setselectedCOI(e.layer.feature.properties.explanation);
                      
                      
                      setselectedCOIdata(e.layer.feature.properties)
                      COIarray = []
                      for (const reason in selectedCOI){
                        const ite = selectedCOI[reason]
                        // console.log("interpretation of {} this item is", reason, ite.interpretation)
                        COIarray.push([reason, ite.interpretation])
                       
                        
                      }
                    //   console.log("COI data is: new test", e.layer.feature.properties)
                    // console.log("coi region selected", e.layer.feature.properties.explanation);
                   
                    
                  
                    }}} 
                    
                    >
                      <Popup>
                      <p> 
                        <h4>Explanation</h4>
                        <p> 
                          <ul>
                          {COIarray.map((charact,indexvalue) =>(
                           <li key={indexvalue} ><strong>{charact[0]}</strong> : {charact[1]}</li>
                        ))}

                          </ul>
                        
                        </p>
                        
                      </p>
                    </Popup>
                    </GeoJSON>}
                  
                  {gradient && showonmap ==1 && <GeoJSON data = {gradient} style={gradientmapunit}/>}
                  {VOincome && showonmap ==1 && <GeoJSON data = {VOincome} style={gradientincomemapunit}/>}
                  {VOvisibleM && showonmap ==1 && <GeoJSON data = {VOvisibleM} style={gradientvisibleMmapunit}/>}
                  {VObirthplace && showonmap ==1 && <GeoJSON data = {VObirthplace} style={gradientbirthplacemapunit}/>}
                  {VOpop && showonmap ==1 && <GeoJSON data = {VOpop} style={gradientpopulationmapunit}/>}
                  {localStorage.setItem('defineddistricts', JSON.stringify(changes))}
                
                </MapContainer>

        </div>
        
        
       
      );


}

export default DrawMap