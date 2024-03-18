import { Draw } from "leaflet"
import React, {useEffect, useState} from "react"
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Polyline, GeoJSON} from 'react-leaflet';
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
function DrawMap(){
  
    const center = [ 43.65107, - 79.347015];
    const [selectedmapunit, setselectedmapunit] = useState(null);
    const [allda, setallda] = useState(null)
    const[dguid, setdguid] = useState(15)
    const coloractiveid = localStorage.getItem('coloractive')
    // set onselect color and onselect again, deselect and change back to grey
    const colormapunit = (mapunit) => {
      if (coloractiveid == 1 && mapunit == selectedmapunit) {
         
        return {
          fillColor: 'green',  
          weight: 0.5, 
          fillOpacity: 0.6,
           
        };
        
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

      
      
    
    return (
      
        <div className="map">  
          
            
          
            
                  <MapContainer center={center} zoom={10} style={{ height: '1000px' }}>
                  <TileLayer
                    
                    url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
                    
                  />
                  
                
              
            
                  {/* //coordinates.map((coord) => [coord.lat, coord.lng])} */}
                  {/* <Polyline positions={coord} color="black" />  */}
                  
                  {allda && <GeoJSON data = {allda} style={{color: 'grey', weight: 0.5}} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature.properties.dguid)}}} />}
                  {allda && <GeoJSON data = {allda} style={colormapunit} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature)}}} />}
                  {/* {allda && <GeoJSON data = {allda} eventHandlers={{click: (e) =>{setselectedmapunit(e.layer.feature.properties.dguid)}}} />} */}
                  {/* {console.log(selectedmapunit)} */}
                  {localStorage.setItem('mapid', selectedmapunit)}
                  {/* {selectedmapunit && <Sidebar DGUID = {selectedmapunit}/>} */}
                
                  {/* {selectedmapunit && <Sidebar DGUID = {selectedmapunit}/>} */}
                  {/* {console.log(allda)} */}
                  {/* {allda && <GeoJSON data = {allda} style={colormapunit} eventHandlers={{click: (e)=>{setselectedmapunit(e.layer.feature)
                  {valuetransfer(e.layer.feature.properties.dguid)}

                }
                  
                  }}
                  
                  />} */}
                  {/* {console.log(allda)} */}
                  {/* <GeoJSON data = {TestPoly} style={colormapunit} eventHandlers={{click: (e) => {
                    setselectedmapunit(e.layer.feature); // Update selected feature
                  },}} />  */}
                
                </MapContainer>
                
            
              

               
             
             
            

        </div>
        
        
       
      );


}

export default DrawMap