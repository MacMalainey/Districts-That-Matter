import { Draw } from "leaflet"
import React, {useEffect, useState} from "react"
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Polyline, GeoJSON, LayersControl} from 'react-leaflet';
import TestPoly from "./TestGeo";
import L from 'leaflet';
import './Map.css';
import axios, { all } from 'axios';
import Sidebar from "./Sidebar";

// FR1: Map Render
// FR2: Map Fetch
// FR3: Map.Units.Render
// FR4: Map.Units.Fetch
// FR5: Map.Navigate
let array = [];
function DrawMap(){
  
    const center = [ 43.65107, - 79.347015];
    const [selectedmapunit, setselectedmapunit] = useState(null);
    const [selectedmapunitid, setselectedmapunitid] = useState(null);
    const [allda, setallda] = useState(null)
    const[dguid, setdguid] = useState(15)
    const coloractiveid = localStorage.getItem('coloractive')
    const colid = localStorage.getItem('colorid')
    const cursorid = localStorage.getItem('cursor')
    const eraseractiveid = localStorage.getItem('eraser')
    // set onselect color and onselect again, deselect and change back to grey
    const[state, setstate] = useState(false);
    const[Dmapid, setDmapid] = useState()
    const[Dcolorid, setDcolorid] = useState()
    
    
    const colormapunit = (mapunit) => {
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

    
    useEffect(()=>{

      const MapData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/units/all');
          const Alldata = response.data // storing the response data in a var which can be utilized. wrapped requirement.
          setallda(Alldata);
        }
        catch {
          console.log('Response data not appropriately handled:');
        }
      }

       MapData();
        
        
      }, [])
      
      const definedistrict= (val1, val2) =>{
          try { 
            setDmapid(val1)
            setDcolorid(val2)
            array.push(([Dmapid, parseInt(Dcolorid)]))
            console.log(array)
            
          }
          catch {
            console.log("Cant recieve id's on time")
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
                    {allda  &&  <GeoJSON data = {allda} style={{ fillColor: 'transparent', color: 'grey', weight: 0.5}} eventHandlers={{click: (e) =>{setselectedmapunitid(e.layer.feature.properties.dguid)} }} />}

                    </LayersControl.BaseLayer>
                    <LayersControl.Overlay name = 'ColorLayer'>
                    {allda && coloractiveid == 1 && <GeoJSON data = {allda} style={{fillColor: 'transparent',color:'grey',weight: 2,fillOpacity: 0.6,}} />}
                    {allda && coloractiveid == 1 && <GeoJSON data = {allda} style={colormapunit} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature);
                  setselectedmapunitid(e.layer.feature.properties.dguid);
                  definedistrict(selectedmapunitid, colid)
                  console.log("selected map unit id is ", selectedmapunitid)
                  }}} />}
                    </LayersControl.Overlay>

                    </LayersControl>                             
                  
                  
                  {/* {allda && <GeoJSON data = {allda} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature.properties.dguid)}}} />} */}
                  {/* {allda && eraseractiveid==1 && coloractiveid == 0 && <GeoJSON data = {allda} style={decolormapunit} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature)}}} />} */}
                  
                  {localStorage.setItem('mapid', selectedmapunitid)}
                  {localStorage.setItem('defineddistricts', JSON.stringify(array))}
                
                </MapContainer>

        </div>
        
        
       
      );


}

export default DrawMap