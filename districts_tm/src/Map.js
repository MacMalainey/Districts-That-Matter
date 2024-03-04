import { Draw } from "leaflet"
import React, {useState} from "react"
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Polyline, GeoJSON} from 'react-leaflet';
import data from './polycords-pretty.json'
import Poly from './PolyGeo';
import TestPoly from "./TestGeo";
import L from 'leaflet';
import './Map.css';

// FR1: Map Render
// FR2: Map Fetch
// FR3: Map.Units.Render
// FR4: Map.Units.Fetch
// FR5: Map.Navigate
function DrawMap(){
  
    const center = [-79, 43];
    const [selectedmapunit, setselectedmapunit] = useState(null);
    const [colorstate, setcolorstate] = useState(false);
    // set onselect color and onselect again, deselect and change back to grey
    const colormapunit = (mapunit) => {
      if (mapunit == selectedmapunit) {
         
        return {
          fillColor: 'green',  
          weight: 1, 
          fillOpacity: 0.6, 
        };
        
      }
      if( selectedmapunit == 'green'){
        return {
          fillColor: 'grey',  
          weight: 2, 
          fillOpacity: 0.6, 
        };
      }
      
    };
    
    return (
        <div className="map">  
             
            <MapContainer center={center} zoom={2} style={{ height: '1000px' }}>
          <TileLayer
            
            url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
            
          />
          {/* //coordinates.map((coord) => [coord.lat, coord.lng])} */}
           {/* <Polyline positions={coord} color="black" />  */}
          
          <GeoJSON data = {TestPoly} style={{color: 'grey'}} />
          <GeoJSON data = {TestPoly} style={colormapunit} eventHandlers={{click: (e) => {
            setselectedmapunit(e.layer.feature); // Update selected feature
          },}} /> 

        </MapContainer>

        </div>
        
       
      );


}

export default DrawMap