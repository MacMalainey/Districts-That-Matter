import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState, createContext } from 'react';
import DrawMap from './Map';
import Sidebar from './Sidebar';
import axios from 'axios';
import { MAP_MODE_HAND } from './config';

// import DataLayer from './DataLayer';
// import Inspect from './Inspect';

export const MapUnitsAllContext = createContext(null);
export const MapUnitDemoContext = createContext(null);
export const COIContext = createContext(null);
export const SchemaContext = createContext(null);
export const DistrictsContext = createContext(null);
export const GradientSelectContext = createContext(null);
export const MapModeContext = createContext(null);

async function MapUnitsAllApi(onUpdate, category) {
  const response = await axios.get('http://127.0.0.1:5000/api/units/all', {
    params: {
      include: category
    }
  })
  onUpdate(response.data)
  
}

async function COIApi(onUpdate, category) {
  const response = await axios.get('http://127.0.0.1:5000/api/cois/all')
  onUpdate(response.data)
}

async function DistrictsContextApi(onUpdate, category) {
  const response = await axios.get('http://127.0.0.1:5000/api/districts')
  onUpdate("App.js", response.data)
}

let category = null;

let expectedCategory = null;

function App() {
  const [COIData, setCOIData] = useState(null);
  const [mapUnitData, setMapUnitData] = useState(null);
  const [districtData, setDistrictData] = useState(null);
  const [gradientSelect, setGradientSelect] = useState(null);
  const [mapMode, setMapMode] = useState(MAP_MODE_HAND);

  useEffect(() => {
    MapUnitsAllApi(setMapUnitData, expectedCategory)
    category = expectedCategory
  }, [expectedCategory]);

  useEffect(() => {
    COIApi(setCOIData)
  }, []);

  useEffect(() => {
    DistrictsContextApi(setDistrictData)
  }, []);
  return (
    <div className='container'>
      <MapUnitsAllContext.Provider value={{data:mapUnitData, category:category}}>
        <COIContext.Provider value={COIData}>
          <DistrictsContext.Provider value={{data: districtData, callback: setDistrictData}}>
            <GradientSelectContext.Provider value={{
                data: gradientSelect,
                callback: (data) => {
                  if (data != null && data != "population" && data != "landarea") {
                    expectedCategory = (data.split('_'))[0]
                    

                  }
                  setGradientSelect(data);
                  
                },
                category: expectedCategory
              }}>
                <MapModeContext.Provider value = {{data: mapMode, callback: setMapMode}}>
                  <DrawMap/>
                  <Sidebar/>
                </MapModeContext.Provider>
            </GradientSelectContext.Provider>
          </DistrictsContext.Provider>
        </COIContext.Provider>
      </MapUnitsAllContext.Provider>
    </div>
  );
}

export default App;
