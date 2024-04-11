//This component is the parent component for our webapp which handles most of api calls


import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState, createContext } from 'react';
import DrawMap from './Map';
import Sidebar from './Sidebar';
import axios from 'axios';
import { MAP_MODE_HAND } from './config';
import { callback } from 'chart.js/helpers';
// import DataLayer from './DataLayer';
// import Inspect from './Inspect';

export const MapUnitsAllContext = createContext(null);
export const MapUnitDemoContext = createContext(null);
export const COIContext = createContext(null);
export const SchemaContext = createContext(null);
export const DistrictsContext = createContext(null);
export const GradientSelectContext = createContext(null);
export const MapModeContext = createContext(null);
export const MapUnitsAllCategoryApiContext = createContext(null);
export const COISelectContext = createContext(null)



//This function handles data for FR3 and FR4
async function MapUnitsAllApi(onUpdate) {
  const response = await axios.get('http://127.0.0.1:5000/api/units/all', {
   
  })
  onUpdate(response.data)
  
}
//This function handles data for FR 10 as visualoverlay of certain demographic data
async function MapUnitsAllCategoryApi(onUpdate, category) {
  if(category!=null){
    const response = await axios.get('http://127.0.0.1:5000/api/units/category/' + category)
    onUpdate(response.data)
    
  }
  
}


// This function handles data for FR 13, FR 14, FR 15
async function COIApi(onUpdate, category) {
  const response = await axios.get('http://127.0.0.1:5000/api/cois/all')
  onUpdate(response.data)
}

//This function handles data for FR 21 for loading districts on application launch 
async function DistrictsContextApi(onUpdate, category) {
  const response = await axios.get('http://127.0.0.1:5000/api/districts')
  onUpdate(response.data)
}

let category = null;

let expectedCategory = null; // user selected category gets parsed for the api call

function App() {
  const [COIData, setCOIData] = useState(null);
  const [mapUnitData, setMapUnitData] = useState(null);
  const [districtData, setDistrictData] = useState(null);
  const [gradientSelect, setGradientSelect] = useState(null);
  const [mapMode, setMapMode] = useState(MAP_MODE_HAND);
  const [categoryData, setcategoryData] = useState(null);
  const [showcoionmap, setshowcoionmap] = useState(false)
  
  // underlined useEffects are for constantly checking the state of the data and providing updates

  useEffect(() => {
    MapUnitsAllApi(setMapUnitData)
    
  }, []);

  
  
  useEffect(() => {
    MapUnitsAllCategoryApi(setcategoryData, expectedCategory)
    category = expectedCategory
  }, [expectedCategory]);
  useEffect(() => {
    COIApi(setCOIData)
  }, []);

  useEffect(() => {
    DistrictsContextApi(setDistrictData)
  }, []);
  // return will have multiple component rendering with different useability 
  // MapUnitsAllContext -> Mapunits data 
  //COIContenxt -> COI data
  //DistrictContext -> Loading saved districts
  //MapunitsAllCategoryApiContext -> Gradient Overlay data for selected category
  //GradientSelectContext -> Gets user selected cagetory and parsing it
  //MapModeContenxt -> checks for which mode is active from paint, cursor, earse
  //COISelectContext -> Checks for if COI show on map is active or not and if it is, it shows COI on the map
  return (
    <div className='container'>
      <MapUnitsAllContext.Provider value={{data:mapUnitData}}>
        <COIContext.Provider value={COIData}>
            <DistrictsContext.Provider value={{data: districtData, callback: setDistrictData}}>
             <MapUnitsAllCategoryApiContext.Provider value = {{data: categoryData, category:category}}>
               <GradientSelectContext.Provider value={{
                  data: gradientSelect,
                  callback: (data) => {
                    if (data != null && data != "population" && data != "landarea" ) {
                      expectedCategory = (data.split('_'))[0]
                      if(expectedCategory == "visible"){
                        expectedCategory = "visible_minority"
                      }

                    }
                    setGradientSelect(data);
                    
                  },
                  category: expectedCategory
                  }}>
                  <MapModeContext.Provider value = {{data: mapMode, callback: setMapMode}}>
                    <COISelectContext.Provider value={{data:showcoionmap, callback: setshowcoionmap}}>
                        <DrawMap/>
                      
                   
                                
                        <Sidebar/>

                          
                    </COISelectContext.Provider>
                  </MapModeContext.Provider>
               </GradientSelectContext.Provider>
              </MapUnitsAllCategoryApiContext.Provider>
            </DistrictsContext.Provider>
        </COIContext.Provider>
      </MapUnitsAllContext.Provider>
    </div>
  );
}

export default App;
