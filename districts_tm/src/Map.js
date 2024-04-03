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

// FR1: Map Render
// FR2: Map Fetch
// FR3: Map.Units.Render
// FR4: Map.Units.Fetch
// FR5: Map.Navigate
let array = [];
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
      // console.log(mapunit)
      if (coloractiveid == 1 && mapunit == selectedmapunit) {
        
        if (colid == 11) {
          return {
            fillColor: '#ff1a1a',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
          
        }
        else if (colid==12) {
          return {
            fillColor: '#ff8080',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==13) {
          return {
            fillColor: '#ffb3b3',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==14) {
          return {
            fillColor: '#ffe6e6', 
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==15) {
          return {
            fillColor: '#ff0000',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==16) {
          return {
            fillColor: '#b30000',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==17) {
          return {
            fillColor: '#4d0000',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==18) {
          return {
            fillColor: '#ff8000', 
            
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==19) {
          return {
            fillColor: '#ffbf00',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==20) {
          return {
            fillColor: '#ffff00',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==21) {
          return {
            fillColor: '#bfff00',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==22) {
          return {
            fillColor: '#bfff00',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==23) {
          return {
            fillColor: '#40ff00',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==24) {
          return {
            fillColor: '#00ff00',
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==25) {
          return {
            fillColor: '#00ff40',
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==26) {
          return {
            fillColor: '#00ff80',
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==27) {
          return {
            fillColor: '#00ffbf',
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==28) {
          return {
            fillColor: '#00ffff',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==29) {
          return {
            fillColor: '#00bfff', 
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==30) {
          return {
            fillColor: '#0080ff', 
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==31) {
          return {
            fillColor: '#0040ff',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==32) {
          return {
            fillColor: '#0000ff', 
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==33) {
          return {
            fillColor: '#4000ff',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==34) {
          return {
            fillColor: '#8000ff', 
            
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==35) {
          return {
            fillColor: '#bf00ff',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==36) {
          return {
            fillColor: '#ff00ff',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==37) {
          return {
            fillColor: '#ff00bf',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==38) {
          return {
            fillColor: '#ff0080', 
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==39) {
          return {
            fillColor: '#ff0040',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==40) {
          return {
            fillColor: '#996680',
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==41) {
          return {
            fillColor: '#80c4b7',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==42) {
          return {
            fillColor: '#eeeeee', 
            
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==43) {
          return {
            fillColor: '#feffba',  
            
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==44) {
          return {
            fillColor: '#c90076',  
            weight: 0.5, 
            
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==45) {
          return {
            fillColor: '#073763', 
            
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==46) {
          return {
            fillColor: '#669999',
              
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==47) {
          return {
            fillColor: '#ffa500',
             
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==48) {
          return {
            fillColor: '#476b6b', 
            
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==49) {
          return {
            fillColor: '#854442', 
            
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==50) {
          return {
            fillColor: '#f24e70',
            color: 'grey',  
            weight: 0.5, 
            fillOpacity: 0.6,
             
          };
        }
        else if (colid==100){
          return {
            fillColor: '#c2dcff',
            weight: 2, 
            fillOpacity: 0.6,
            
            
          }
        }
        
        
        
        
      }
 

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
          
          
        }, [])

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
                array.push(([val1, null]))
              }
            else {
              array.push(([val1, parseInt(val2)]))
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
    if(result < 14.9){
        return {
                fillColor: '#D3D3D3',
                color: 'lightgrey'  ,
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
    }
    else if (result > 15 && result < 29.9){
      return {
        fillColor: '#C0C0C0',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 30 && result < 44.9){
      return {
        fillColor: '#DCDCDC',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 45 && result < 59.9){
      return {
        fillColor: '#808080',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 60 && result < 74.9){
      return {
        fillColor: '#696969',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 75 && result < 89.9){
      return {
        fillColor: '#A9A9A9',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else {
      return {
        fillColor: '#444444',
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
              if(result < 14.9){
                return {
                        fillColor: '#D3D3D3',
                        color: 'lightgrey'  ,
                        weight: 0.5, 
                        fillOpacity: 0.3,
                         
                      };
            }
            else if (result > 15 && result < 29.9){
              return {
                fillColor: '#C0C0C0',
                color: 'lightgrey',
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
            }
            else if (result > 30 && result < 44.9){
              return {
                fillColor: '#DCDCDC',
                color: 'lightgrey',
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
            }
            else if (result > 45 && result < 59.9){
              return {
                fillColor: '#808080',
                color: 'lightgrey',
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
            }
            else if (result > 60 && result < 74.9){
              return {
                fillColor: '#696969',
                color: 'lightgrey',
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
            }
            else if (result > 75 && result < 89.9){
              return {
                fillColor: '#A9A9A9',
                color: 'lightgrey',
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
            }
            else {
              return {
                fillColor: '#444444',
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
          if(result < 14.9){
            return {
                    fillColor: '#D3D3D3',
                    color: 'lightgrey'  ,
                    weight: 0.5, 
                    fillOpacity: 0.3,
                     
                  };
        }
        else if (result > 15 && result < 29.9){
          return {
            fillColor: '#C0C0C0',
            color: 'lightgrey',
            weight: 0.5, 
            fillOpacity: 0.3,
             
          };
        }
        else if (result > 30 && result < 44.9){
          return {
            fillColor: '#DCDCDC',
            color: 'lightgrey',
            weight: 0.5, 
            fillOpacity: 0.3,
             
          };
        }
        else if (result > 45 && result < 59.9){
          return {
            fillColor: '#808080',
            color: 'lightgrey',
            weight: 0.5, 
            fillOpacity: 0.3,
             
          };
        }
        else if (result > 60 && result < 74.9){
          return {
            fillColor: '#696969',
            color: 'lightgrey',
            weight: 0.5, 
            fillOpacity: 0.3,
             
          };
        }
        else if (result > 75 && result < 89.9){
          return {
            fillColor: '#A9A9A9',
            color: 'lightgrey',
            weight: 0.5, 
            fillOpacity: 0.3,
             
          };
        }
        else {
          return {
            fillColor: '#444444',
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
      if(result < 14.9){
        return {
                fillColor: '#D3D3D3',
                color: 'lightgrey'  ,
                weight: 0.5, 
                fillOpacity: 0.3,
                 
              };
    }
    else if (result > 15 && result < 29.9){
      return {
        fillColor: '#C0C0C0',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 30 && result < 44.9){
      return {
        fillColor: '#DCDCDC',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 45 && result < 59.9){
      return {
        fillColor: '#808080',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 60 && result < 74.9){
      return {
        fillColor: '#696969',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else if (result > 75 && result < 89.9){
      return {
        fillColor: '#A9A9A9',
        color: 'lightgrey',
        weight: 0.5, 
        fillOpacity: 0.3,
         
      };
    }
    else {
      return {
        fillColor: '#444444',
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
  if(result < 14.9){
    return {
            fillColor: '#D3D3D3',
            color: 'lightgrey'  ,
            weight: 0.5, 
            fillOpacity: 0.3,
             
          };
}
else if (result > 15 && result < 29.9){
  return {
    fillColor: '#C0C0C0',
    color: 'lightgrey',
    weight: 0.5, 
    fillOpacity: 0.3,
     
  };
}
else if (result > 30 && result < 44.9){
  return {
    fillColor: '#DCDCDC',
    color: 'lightgrey',
    weight: 0.5, 
    fillOpacity: 0.3,
     
  };
}
else if (result > 45 && result < 59.9){
  return {
    fillColor: '#808080',
    color: 'lightgrey',
    weight: 0.5, 
    fillOpacity: 0.3,
     
  };
}
else if (result > 60 && result < 74.9){
  return {
    fillColor: '#696969',
    color: 'lightgrey',
    weight: 0.5, 
    fillOpacity: 0.3,
     
  };
}
else if (result > 75 && result < 89.9){
  return {
    fillColor: '#A9A9A9',
    color: 'lightgrey',
    weight: 0.5, 
    fillOpacity: 0.3,
     
  };
}
else {
  return {
    fillColor: '#444444',
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
                    {allda && coloractiveid == 1 && <GeoJSON data = {allda} style={colormapunit} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature);
                    {console.log(e.layer.feature.id)}
                    setselectedmapunitid(e.layer.feature.id);
                    
                    
                    
                  }}} />}
                  {gradient && showonmap ==1 && <GeoJSON data = {gradient} style={gradientmapunit}/>}
                  {VOincome && showonmap ==1 && <GeoJSON data = {VOincome} style={gradientincomemapunit}/>}
                  {VOvisibleM && showonmap ==1 && <GeoJSON data = {VOvisibleM} style={gradientvisibleMmapunit}/>}
                  {VObirthplace && showonmap ==1 && <GeoJSON data = {VObirthplace} style={gradientbirthplacemapunit}/>}
                  {VOpop && showonmap ==1 && <GeoJSON data = {VOpop} style={gradientpopulationmapunit}/>}
                  {localStorage.setItem('defineddistricts', JSON.stringify(array))}
                
                </MapContainer>

        </div>
        
        
       
      );


}

export default DrawMap